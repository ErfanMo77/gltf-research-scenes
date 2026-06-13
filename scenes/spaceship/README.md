# Spaceship

![Spaceship reference](source/TungstenRender.png)

A compact science-fiction model converted from PBRT v4 to glTF. Good for checking metallic materials, glass fallback behavior, emissive area-light approximations.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [4060.b Spaceship on Blend Swap](https://blendswap.com/blend/13489)
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/spaceship_core.gltf`
- Extended glTF: `gltf/spaceship_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for clearcoat, transmission, IOR, and emissive-strength data.
- Area lights are represented with emissive mesh geometry.
- The infinite light is preserved as metadata.
- Spectral metals and glass behavior are approximations; exact mappings are in the conversion report.
