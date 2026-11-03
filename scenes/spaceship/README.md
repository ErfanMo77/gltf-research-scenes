# Spaceship

![Spaceship reference](gltf/spaceship.png)

A compact science-fiction model converted from PBRT v4 to glTF. Good scene for checking metallic materials, glass and emissive area-light.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [4060.b Spaceship on Blend Swap](https://blendswap.com/blend/13489)
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/spaceship_core.gltf`
- Extended glTF: `gltf/spaceship_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for clearcoat, transmission, IOR, volume, and emissive-strength data.
- The glass material uses `KHR_materials_volume` so renderers treat it as a solid refractive volume instead of the default thin-walled surface. `thicknessFactor` is the largest bounding-box extent of the meshes using the material, the same convention as the other scenes.
- Area lights are represented with emissive mesh geometry.
- The infinite light is preserved as metadata.
- Spectral metals and glass behavior are approximations; exact mappings are in the conversion report.
