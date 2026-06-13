from __future__ import annotations

import argparse
import json
import struct
from pathlib import Path
from urllib.parse import unquote, urlparse


GLB_MAGIC = 0x46546C67
GLB_VERSION = 2
JSON_CHUNK = 0x4E4F534A
BIN_CHUNK = 0x004E4942


def pad4(size: int) -> int:
    return (-size) & 3


def local_uri_path(base_dir: Path, uri: str) -> Path:
    parsed = urlparse(uri)
    if parsed.scheme or parsed.netloc or parsed.query or parsed.fragment:
        raise ValueError(f"unsupported buffer uri: {uri}")
    return base_dir / unquote(parsed.path)


def pack_glb(gltf: dict, bin_payload: bytes) -> bytes:
    buffers = gltf.get("buffers")
    if not isinstance(buffers, list) or len(buffers) != 1:
        raise ValueError("expected exactly one glTF buffer")

    gltf = dict(gltf)
    gltf["buffers"] = [dict(buffers[0])]
    gltf["buffers"][0].pop("uri", None)
    gltf["buffers"][0]["byteLength"] = len(bin_payload)

    json_payload = json.dumps(gltf, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    json_payload += b" " * pad4(len(json_payload))
    bin_payload += b"\0" * pad4(len(bin_payload))

    total_size = 12 + 8 + len(json_payload) + 8 + len(bin_payload)
    return b"".join(
        (
            struct.pack("<III", GLB_MAGIC, GLB_VERSION, total_size),
            struct.pack("<II", len(json_payload), JSON_CHUNK),
            json_payload,
            struct.pack("<II", len(bin_payload), BIN_CHUNK),
            bin_payload,
        )
    )


def convert_gltf(gltf_path: Path, output_path: Path | None = None) -> Path:
    gltf_path = gltf_path.resolve()
    with gltf_path.open("r", encoding="utf-8") as file:
        gltf = json.load(file)

    buffers = gltf.get("buffers")
    if not isinstance(buffers, list) or len(buffers) != 1:
        raise ValueError(f"{gltf_path}: expected exactly one glTF buffer")

    uri = buffers[0].get("uri")
    if not isinstance(uri, str):
        raise ValueError(f"{gltf_path}: expected buffer uri")

    bin_path = local_uri_path(gltf_path.parent, uri)
    output_path = output_path or gltf_path.with_suffix(".glb")
    payload = pack_glb(gltf, bin_path.read_bytes())
    temporary = output_path.with_suffix(output_path.suffix + ".tmp")
    temporary.write_bytes(payload)
    temporary.replace(output_path)
    return output_path


def scene_gltf_paths(scene_id_or_dir: str, variant: str) -> list[Path]:
    scene_dir = Path(scene_id_or_dir)
    if not scene_dir.exists():
        scene_dir = Path("scenes") / scene_id_or_dir

    base_name = scene_dir.name.replace("-", "_")
    variants = ("core", "extended") if variant == "both" else (variant,)
    return [scene_dir / "gltf" / f"{base_name}_{name}.gltf" for name in variants]


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Pack generated glTF JSON and BIN files into GLB files.",
        epilog=(
            "Examples:\n"
            "  python tools/gltf_to_glb.py cornell-box\n"
            "  python tools/gltf_to_glb.py cornell-box --variant extended\n"
            "  python tools/gltf_to_glb.py scenes/cornell-box/gltf/cornell_box_core.gltf"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("inputs", nargs="+", help="Scene ids, scene directories, or .gltf files.")
    parser.add_argument("--variant", choices=("core", "extended", "both"), default="both")
    args = parser.parse_args()

    for item in args.inputs:
        path = Path(item)
        gltf_paths = [path] if path.suffix == ".gltf" else scene_gltf_paths(item, args.variant)
        for gltf_path in gltf_paths:
            output = convert_gltf(gltf_path)
            print(output.as_posix())


if __name__ == "__main__":
    main()
