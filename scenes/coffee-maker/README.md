# Coffee Maker

![Coffee Maker reference](gltf/coffee-maker.png)

A coffee maker model converted from PBRT v4 to glTF. It is useful for checking coated plastic, glass, and spectral metal approximation.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [Coffee Maker on Blend Swap](https://blendswap.com/blend/16368)
- Original author: cekuhnen
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/coffee_maker_core.gltf`
- Extended glTF: `gltf/coffee_maker_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for clearcoat, transmission, IOR, specular, volume, and emissive strength data.
- The glass material uses `KHR_materials_volume` so renderers treat it as a solid refractive volume instead of the default thin-walled surface. `thicknessFactor` is the largest bounding-box extent of the meshes using the material, the same convention as the other scenes.
- The scene contains 23 meshes and 235,271 triangles.
- Three PBRT area lights are converted to emissive meshes.
- Spectral metal, glass behavior, and coated diffuse materials are approximations; exact mappings are in the conversion report.
