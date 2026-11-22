#!/usr/bin/env python3
"""Build the release archives of generated scenes, reports, environment maps, licenses, and reference images.

gltf_research_scenes_glb.zip mirrors the repository layout. A scene's gltf folder holds its assets and
the reference images named by the conversion report. Its source folder holds the original reference images.

Scenes listed in scene_packages.json keep their glTF variants beside their shared buffers. They join
the collection archive unless their rule supplies a separate archive filename.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENE_PACKAGES = Path(__file__).with_name("scene_packages.json")
REFERENCE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp"}
ENVIRONMENT_FIELDS = re.compile(r'^\s+(uri|license_uri|file|license_file): "(.+)"$')
REFERENCE_RENDER_IMAGE = re.compile(r'(?m)^reference_render:\n(?:[ \t].*\n)*?  image: "([^"]+)"$')
REFERENCE_RENDER_SECTION = re.compile(r"(?m)^reference_render:\n(?:[ \t].*\n|\n)*")
# Image fields in the reference_render.frames and reference_render.variants lists.
FRAME_RENDER_IMAGE = re.compile(r'(?m)^ {6}image: "([^"]+)"$')


def scene_packages(rules: Path = SCENE_PACKAGES) -> dict[str, dict]:
    """Scenes packaged as glTF with shared buffers, by scene id."""
    return json.loads(rules.read_text(encoding="utf-8"))["scenes"] if rules.is_file() else {}


def separate_packages(rules: Path = SCENE_PACKAGES) -> dict[str, dict]:
    return {scene_id: rule for scene_id, rule in scene_packages(rules).items() if "archive" in rule}


def reference_render_pending(scene_id: str) -> bool:
    return scene_packages().get(scene_id, {}).get("reference_render") == "pending"


def reference_render(report: Path, required: bool = True) -> Path | None:
    match = REFERENCE_RENDER_IMAGE.search(report.read_text(encoding="utf-8"))
    if not match:
        if required:
            raise SystemExit(f"missing reference_render image field: {report}")
        return None
    image = report.parent / match[1]
    if not image.is_file():
        raise SystemExit(f"missing reference render: {image}")
    return image


def frame_renders(report: Path) -> list[Path]:
    """Additional frame and material variant renders listed in the report, in order."""
    section = REFERENCE_RENDER_SECTION.search(report.read_text(encoding="utf-8").rstrip() + "\n")
    images = [report.parent / name for name in FRAME_RENDER_IMAGE.findall(section.group())] if section else []
    for image in images:
        if not image.is_file():
            raise SystemExit(f"missing reference render: {image}")
    return images


def scene_files(scene_dir: Path) -> list[Path]:
    base_name = scene_dir.name.replace("-", "_")
    gltf_dir, source_dir = scene_dir / "gltf", scene_dir / "source"
    if not source_dir.is_dir():
        raise SystemExit(f"missing source directory: {source_dir}")
    single_glb = gltf_dir / f"{base_name}.glb"
    files = [single_glb] if single_glb.is_file() else [gltf_dir / f"{base_name}_{variant}.glb" for variant in ("core", "extended")]
    report = gltf_dir / "conversion.yaml"
    files.append(report)
    for path in files:
        if not path.is_file():
            raise SystemExit(f"missing generated file: {path}")
    image = reference_render(report)
    files += [image, *(frame for frame in frame_renders(report) if frame != image)]
    files += sorted(gltf_dir.glob(f"{base_name}_environment*"))
    licenses = sorted(path for path in source_dir.iterdir() if path.is_file() and "license" in path.name.lower())
    references = sorted(path for path in source_dir.iterdir() if path.is_file() and path.suffix.lower() in REFERENCE_SUFFIXES)
    if not licenses:
        raise SystemExit(f"missing source license: {source_dir}")
    if not references:
        raise SystemExit(f"missing source reference image: {source_dir}")
    provenance = source_dir / "provenance.yaml"
    if provenance.is_file():
        files.append(provenance)
    return files + licenses + references


def shared_gltf_scene_files(scene_dir: Path, rule: dict) -> list[Path]:
    """Both glTF variants, their shared buffers, and accompanying files."""
    base_name = scene_dir.name.replace("-", "_")
    gltf_dir, source_dir = scene_dir / "gltf", scene_dir / "source"
    gltfs = [gltf_dir / f"{base_name}_{variant}.gltf" for variant in ("core", "extended")]
    report = gltf_dir / "conversion.yaml"
    for path in (*gltfs, report):
        if not path.is_file():
            raise SystemExit(f"missing generated file: {path}")
    buffers = sorted({gltf_dir / buffer["uri"] for gltf in gltfs for buffer in json.loads(gltf.read_text(encoding="utf-8"))["buffers"]})
    for path in buffers:
        if not path.is_file():
            raise SystemExit(f"missing buffer: {path}")
        with path.open("rb") as file:
            if file.read(40).startswith(b"version https://git-lfs"):
                raise SystemExit(f"buffer is a Git LFS pointer; run git lfs pull: {path}")
    image = reference_render(report, required=rule.get("reference_render") != "pending")
    images = [image, *(frame for frame in frame_renders(report) if frame != image)] if image else []
    sources = sorted(
        path for path in source_dir.iterdir()
        if path.is_file() and ("license" in path.name.lower() or path.suffix.lower() in REFERENCE_SUFFIXES or path.name == "provenance.yaml")
    ) if source_dir.is_dir() else []
    if not any("license" in path.name.lower() for path in sources):
        raise SystemExit(f"missing source license: {source_dir}")
    json_report = report.with_suffix(".json")
    return [*gltfs, *buffers, report, *([json_report] if json_report.is_file() else []),
            *images, *sorted(gltf_dir.glob(f"{base_name}_environment*")), *sources]


def environment_references(report: Path) -> list[tuple[str, str]]:
    # Fields inside each environment_map block of a conversion report.
    references, indent = [], None
    for line in report.read_text(encoding="utf-8").splitlines():
        stripped = line.lstrip()
        if stripped == "environment_map:":
            indent = len(line) - len(stripped)
        elif indent is not None and len(line) - len(stripped) > indent and (match := ENVIRONMENT_FIELDS.match(line)):
            references.append((match[1], match[2]))
        elif indent is not None and len(line) - len(stripped) <= indent:
            indent = None
    return references


def check_environment_references(package_root: Path):
    # uri fields are relative to the report's folder; file fields to the package root,
    # which mirrors the repository layout.
    for report in sorted(package_root.glob("scenes/*/gltf/conversion.yaml")):
        for field, value in environment_references(report):
            target = report.parent / value if field.endswith("uri") else package_root / value
            if not target.is_file():
                raise SystemExit(f"{report.relative_to(package_root).as_posix()}: {field} {value} is not in the package")


def write_zip(zip_path: Path, root: Path, base: Path) -> Path:
    zip_path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(root.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(base).as_posix())
    return zip_path


def build_package(scenes_root: Path, dist: Path, rules: Path = SCENE_PACKAGES) -> Path:
    package_root = dist / "gltf_research_scenes"
    packages = scene_packages(rules)
    if package_root.exists():
        shutil.rmtree(package_root)
    for scene_dir in sorted(path for path in scenes_root.iterdir() if (path / "gltf").is_dir()):
        rule = packages.get(scene_dir.name)
        if rule is not None and "archive" in rule:
            continue
        files = shared_gltf_scene_files(scene_dir, rule) if rule is not None else scene_files(scene_dir)
        for source in files:
            target = package_root / "scenes" / source.relative_to(scenes_root)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    common = scenes_root / "common"
    if common.is_dir():
        shutil.copytree(common, package_root / "scenes" / "common")
    check_environment_references(package_root)
    return write_zip(dist / "gltf_research_scenes_glb.zip", package_root, dist)


def build_scene_package(scenes_root: Path, dist: Path, scene_id: str, rule: dict) -> Path:
    """Archive one scene as a single top-level folder named after it."""
    scene_dir = scenes_root / scene_id
    staging = dist / "separate"
    package_root = staging / scene_id
    if package_root.exists():
        shutil.rmtree(package_root)
    for source in shared_gltf_scene_files(scene_dir, rule):
        target = package_root / source.relative_to(scene_dir)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    # The archive stands alone, so every environment file its report names must be inside it.
    report = package_root / "gltf" / "conversion.yaml"
    for field, value in environment_references(report):
        if field.endswith("uri") and not (report.parent / value).resolve().is_relative_to(package_root.resolve()):
            raise SystemExit(f"{scene_id}: {field} {value} is outside the scene's archive")
        if field.endswith("uri") and not (report.parent / value).is_file():
            raise SystemExit(f"{scene_id}: {field} {value} is not in the package")
    return write_zip(dist / rule["archive"], package_root, staging)


def build_packages(scenes_root: Path, dist: Path, rules: Path = SCENE_PACKAGES) -> list[Path]:
    packages = [build_package(scenes_root, dist, rules)]
    for scene_id, rule in sorted(separate_packages(rules).items()):
        if (scenes_root / scene_id / "gltf").is_dir():
            packages.append(build_scene_package(scenes_root, dist, scene_id, rule))
    return packages


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenes", type=Path, default=ROOT / "scenes")
    parser.add_argument("--dist", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    for package in build_packages(args.scenes, args.dist):
        print(package.as_posix())


if __name__ == "__main__":
    main()
