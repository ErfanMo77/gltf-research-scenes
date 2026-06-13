# Modern Hall

![Modern Hall reference](source/TungstenRender.png)

A modern hallway interior converted from PBRT v4 to glTF. It is useful for checking textured clearcoat-style materials, metal approximation, glass with homogeneous medium data, and emissive area-light fallbacks including tessellated disk emitters.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [Modern hall on Blend Swap](https://blendswap.com/blend/6304)
- Original author: NewSee2l035
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/modern_hall_core.gltf`
- Extended glTF: `gltf/modern_hall_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for clearcoat, transmission, IOR, volume.
- Texture image maps are converted from TGA to embedded PNG.
- Area lighting is represented with emissive mesh geometry.
- PBRT disk shapes are tessellated to triangle meshes.
- Volumetric path tracing, spectral metals, and glass behavior are approximations; exact mappings are in the conversion report.
