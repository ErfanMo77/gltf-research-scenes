# Staircase

![Staircase reference](source/TungstenRender.png)

A wooden staircase interior converted from PBRT v4 to glTF. It is useful for checking dense textured geometry, portrait camera conversion, clearcoat-style materials, glass, GI, and emissive mesh lighting.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [The Wooden Staircase on Blend Swap](https://blendswap.com/blend/14449)
- Original author: Wig42
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/staircase_core.gltf`
- Extended glTF: `gltf/staircase_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for clearcoat, transmission, IOR, and emissive-strength data.
- Texture image maps are converted from TGA to embedded PNG.
- The portrait PBRT camera is converted using the source film aspect ratio.
- Area lighting is represented with emissive mesh geometry.
- Displacement, spectral metals, and glass behavior are approximations; exact mappings are in the conversion report.
