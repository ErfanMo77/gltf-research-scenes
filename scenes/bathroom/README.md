# Bathroom

![Bathroom reference](source/TungstenRender.png)

A large bathroom interior converted from PBRT v4 to glTF. It is useful for checking dense textured geometry, glass, metallic surfaces, alpha-masked materials, and emissive area-light fallbacks.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [Contemporary Bathroom on Blend Swap](https://blendswap.com/blend/13303)
- Original author: Mareck
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/bathroom_core.gltf`
- Extended glTF: `gltf/bathroom_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for clearcoat, transmission, IOR, and emissive-strength data.
- Texture image maps are converted from TGA to embedded PNG.
- The rug alpha mask is baked into a glTF alpha-masked texture.
- Area lighting is represented with emissive mesh geometry.
- Displacement, spectral metals, and glass behavior are approximations; exact mappings are in the conversion report.
