# Veach Bidir

![Veach Bidir reference](source/TungstenRender.png)

A small Veach bidirectional-lighting test scene converted from PBRT v4 to glTF. It is useful for checking diffuse, metallic, and glass materials with two area-light fallbacks.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/veach_bidir_core.gltf`
- Extended glTF: `gltf/veach_bidir_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for transmission, IOR, and emissive-strength data.
- Area lights are represented with emissive mesh geometry.
- The shared PBRT material on light rectangles is split into dedicated glTF light materials.
- Spectral metals and glass behavior are approximations; exact mappings are in the conversion report.
