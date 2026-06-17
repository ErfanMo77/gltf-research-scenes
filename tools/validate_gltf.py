from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def command_escape(text: object, *, parameter: bool = False) -> str:
    escaped = str(text).replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    if parameter:
        escaped = escaped.replace(":", "%3A").replace(",", "%2C")
    return escaped


def annotation(level: str, path: Path, title: str, message: str) -> None:
    rel_path = path.relative_to(ROOT).as_posix() if path.is_absolute() else path.as_posix()
    print(
        f"::{level} file={command_escape(rel_path, parameter=True)},"
        f"title={command_escape(title, parameter=True)}::{command_escape(message)}"
    )


def discover_scenes() -> list[Path]:
    scenes_root = ROOT / "scenes"
    return sorted(path for path in scenes_root.iterdir() if path.is_dir() and (path / "README.md").is_file())


def expected_assets(scene_dir: Path) -> list[Path]:
    base = scene_dir.name.replace("-", "_")
    gltf_dir = scene_dir / "gltf"
    return [
        gltf_dir / f"{base}_core.gltf",
        gltf_dir / f"{base}_extended.gltf",
        gltf_dir / f"{base}.bin",
        gltf_dir / "conversion.yaml",
    ]


def run_validator(validator: str, gltf_path: Path) -> tuple[dict | None, str]:
    command = [
        validator,
        "--stdout",
        "--validate-resources",
        "--no-write-timestamp",
        "--no-absolute-path",
        str(gltf_path),
    ]
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True)
    try:
        return json.loads(result.stdout), result.stderr
    except json.JSONDecodeError:
        return None, result.stderr or result.stdout


def write_report(report_dir: Path | None, scene_id: str, gltf_path: Path, report: dict) -> None:
    if report_dir is None:
        return
    scene_report_dir = report_dir / scene_id
    scene_report_dir.mkdir(parents=True, exist_ok=True)
    report_path = scene_report_dir / f"{gltf_path.stem}.report.json"
    report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


def issue_counts(report: dict | None) -> tuple[int, int, int, int]:
    if report is None:
        return 1, 0, 0, 0
    issues = report.get("issues", {})
    return (
        int(issues.get("numErrors", 0)),
        int(issues.get("numWarnings", 0)),
        int(issues.get("numInfos", 0)),
        int(issues.get("numHints", 0)),
    )


def summarize(rows: list[dict], missing: list[Path]) -> str:
    total_errors = sum(row["errors"] for row in rows) + len(missing)
    total_warnings = sum(row["warnings"] for row in rows)
    total_infos = sum(row["infos"] for row in rows)
    total_hints = sum(row["hints"] for row in rows)

    lines = [
        "## glTF Validation",
        "",
        f"Validated {len(rows)} glTF files across {len({row['scene'] for row in rows})} scenes.",
        "",
        f"Errors: {total_errors}  ",
        f"Warnings: {total_warnings}  ",
        f"Infos: {total_infos}  ",
        f"Hints: {total_hints}",
        "",
        "| Scene | Variant | Errors | Warnings | Infos | Hints |",
        "| --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for row in rows:
        lines.append(
            f"| `{row['scene']}` | `{row['variant']}` | {row['errors']} | "
            f"{row['warnings']} | {row['infos']} | {row['hints']} |"
        )
    if missing:
        lines.extend(["", "### Missing Expected Files", ""])
        lines.extend(f"- `{path.relative_to(ROOT).as_posix()}`" for path in missing)
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate committed glTF scene outputs.")
    parser.add_argument("--validator", default="gltf_validator", help="Path to the Khronos glTF Validator CLI.")
    parser.add_argument("--report-dir", type=Path, help="Directory for full JSON validator reports.")
    parser.add_argument("--fail-on", choices=("errors", "warnings"), default="errors")
    parser.add_argument("--max-annotations", type=int, default=50)
    args = parser.parse_args()

    if args.report_dir is not None and not args.report_dir.is_absolute():
        args.report_dir = ROOT / args.report_dir

    rows: list[dict] = []
    missing: list[Path] = []
    annotations_left = args.max_annotations

    for scene_dir in discover_scenes():
        for path in expected_assets(scene_dir):
            if not path.is_file():
                missing.append(path)
                annotation("error", path, "Missing glTF scene asset", "Expected generated scene output is missing.")

        for gltf_path in expected_assets(scene_dir)[:2]:
            if not gltf_path.is_file():
                continue
            try:
                report, stderr = run_validator(args.validator, gltf_path)
            except FileNotFoundError:
                print(f"error: validator executable not found: {args.validator}", file=sys.stderr)
                return 2

            errors, warnings, infos, hints = issue_counts(report)
            rows.append(
                {
                    "scene": scene_dir.name,
                    "variant": "core" if gltf_path.name.endswith("_core.gltf") else "extended",
                    "errors": errors,
                    "warnings": warnings,
                    "infos": infos,
                    "hints": hints,
                }
            )

            if report is not None:
                write_report(args.report_dir, scene_dir.name, gltf_path, report)
                for issue in report.get("issues", {}).get("messages", []):
                    severity = issue.get("severity")
                    if severity not in (0, 1) or annotations_left <= 0:
                        continue
                    level = "error" if severity == 0 else "warning"
                    annotation(level, gltf_path, issue.get("code", "glTF Validator"), issue.get("message", ""))
                    annotations_left -= 1
            else:
                annotation("error", gltf_path, "glTF Validator failed", stderr.strip() or "Validator produced no JSON report.")

    summary = summarize(rows, missing)
    print(summary)
    step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if step_summary:
        with open(step_summary, "a", encoding="utf-8", newline="\n") as file:
            file.write(summary)

    errors = sum(row["errors"] for row in rows) + len(missing)
    warnings = sum(row["warnings"] for row in rows)
    if errors or (args.fail_on == "warnings" and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
