# Lamp

![Lamp reference](source/TungstenRender.png)

A small desk lamp scene converted from PBRT v4 to glTF. Useful for checking dense object geometry, coated black plastic, metallic conductor approximation, dielectric bulb glass, and emissive area-light conversion.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [Little Lamp on Blend Swap](https://blendswap.com/blend/6885)
- Original author: UP3D
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/lamp_core.gltf`
- Extended glTF: `gltf/lamp_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for clearcoat, transmission, IOR, specular, and emissive-strength data.
- The scene contains 50 meshes and 619,358 triangles.
- Two PBRT area lights are converted to emissive meshes.
- The distant light is preserved as metadata.
- Spectral metals, bulb glass behavior, and coated diffuse materials are approximations; exact mappings are in the conversion report.
