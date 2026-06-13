# Bathroom 2

![Bathroom 2 reference](source/TungstenRender.png)

A bathroom interior converted from PBRT v4 to glTF. Good for checking textured coated wood, rough glass, metallic fixtures, mirrors, and emissive mesh lighting.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [Salle de bain on Blend Swap](https://blendswap.com/blend/12584)
- Original author: nacimus
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/bathroom2_core.gltf`
- Extended glTF: `gltf/bathroom2_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for clearcoat, transmission, IOR.
- Texture image maps are converted from TGA to embedded PNG.
- The PBRT area light is represented with emissive mesh geometry.
- Spectral metals, rough glass, and clearcoat behavior are approximations; exact mappings are in the conversion report.
