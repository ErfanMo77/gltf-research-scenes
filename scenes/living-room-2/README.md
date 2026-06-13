# Living Room 2

![Living Room 2 reference](source/TungstenRender.png)

A white living room interior converted from PBRT v4 to glTF. It is useful for checking many textured props, clearcoat materials, glass-like fixture parts, metallic details, and multiple emissive lighting geometries.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [The White Room Cycles on Blend Swap](https://blendswap.com/blend/5014)
- Original author: Jay-Artist
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/living_room_2_core.gltf`
- Extended glTF: `gltf/living_room_2_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for clearcoat, transmission, IOR, and emissive-strength data.
- Texture image maps are converted from TGA to embedded PNG.
- The local source PBRT `TvScreen` material was changed from dielectric glass to dark coated diffuse clearcoat so the television matches the black screen in the reference.
- The scene contains 185 meshes and 601,209 triangles.
- Rectangular PBRT area lights are represented with emissive mesh geometry.
- Spectral metals and glass behavior are approximations; exact mappings are in the conversion report.
