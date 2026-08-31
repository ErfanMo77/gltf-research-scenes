# Kitchen

![Kitchen reference](source/TungstenRender.png)

A detailed kitchen interior converted from PBRT v4 to glTF. It is useful for checking clearcoat materials, glass, metallic surfaces, and multiple emissive mesh lights.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [Country Kitchen on Blend Swap](https://blendswap.com/blend/5156)
- Original author: Jay-Artist
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/kitchen_core.gltf`
- Extended glTF: `gltf/kitchen_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for clearcoat, transmission, IOR, and emissive-strength data.
- Texture image maps are converted from TGA to embedded PNG.
- Blinds transmittance and displacement details are preserved as metadata (such as the Bread word on the toaster).
- Area lights are represented with emissive mesh geometry.
- Spectral metals and glass behavior are approximations; exact mappings are in the conversion report.
