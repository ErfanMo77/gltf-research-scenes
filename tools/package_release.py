#!/usr/bin/env python3
"""Build the release zip of generated GLBs, reports, environment maps, licenses, and reference images."""
from __future__ import annotations

import argparse
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFERENCE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp"}
ENVIRONMENT_FIELDS = re.compile(r'^\s+(uri|license_uri|file|license_file): "(.+)"$')


def scene_files(scene_dir: Path) -> list[Path]:
    base_name = scene_dir.name.replace("-", "_")
    gltf_dir, source_dir = scene_dir / "gltf", scene_dir / "source"
    if not source_dir.is_dir():
        raise SystemExit(f"missing source directory: {source_dir}")
    single_glb = gltf_dir / f"{base_name}.glb"
    files = [single_glb] if single_glb.is_file() else [gltf_dir / f"{base_name}_{variant}.glb" for variant in ("core", "extended")]
    files.append(gltf_dir / "conversion.yaml")
    for path in files:
        if not path.is_file():
            raise SystemExit(f"missing generated file: {path}")
    files += sorted(gltf_dir.glob(f"{base_name}_environment*"))
    licenses = sorted(path for path in source_dir.iterdir() if path.is_file() and "license" in path.name.lower())
    references = sorted(path for path in source_dir.iterdir() if path.is_file() and path.suffix.lower() in REFERENCE_SUFFIXES)
    if not licenses:
        raise SystemExit(f"missing source license: {source_dir}")
    if not references:
        raise SystemExit(f"missing source reference image: {source_dir}")
    return files + licenses + references


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


def build_package(scenes_root: Path, dist: Path) -> Path:
    package_root = dist / "gltf_research_scenes"
    zip_path = dist / "gltf_research_scenes_glb.zip"
    if package_root.exists():
        shutil.rmtree(package_root)
    for scene_dir in sorted(path for path in scenes_root.iterdir() if (path / "gltf").is_dir()):
        for source in scene_files(scene_dir):
            target = package_root / "scenes" / source.relative_to(scenes_root)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    common = scenes_root / "common"
    if common.is_dir():
        shutil.copytree(common, package_root / "scenes" / "common")
    check_environment_references(package_root)
    dist.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(package_root.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(dist).as_posix())
    return zip_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--scenes", type=Path, default=ROOT / "scenes")
    parser.add_argument("--dist", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    print(build_package(args.scenes, args.dist).as_posix())


if __name__ == "__main__":
    main()
