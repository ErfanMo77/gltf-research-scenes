# Pontiac GTO

![Pontiac GTO reference](source/TungstenRender.png)

A 1967 Pontiac GTO car model converted from PBRT v4 to glTF. It is useful for checking large vehicle geometry, clearcoat car paint, glass transmission, chrome and steel metal approximation, and leather materials.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [Pontiac GTO 67 on Blend Swap](https://blendswap.com/blend/13575)
- Original author: thecali
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/pontiac_gto_core.gltf`
- Extended glTF: `gltf/pontiac_gto_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for clearcoat, transmission, IOR, and specular data.
- The scene contains 63 meshes and about 1.06 million triangles.
- The infinite light is preserved as metadata.
- The original `textures/envmap.pfm` is not redistributed here because no separate redistributable environment-map license was included; use the source links above to obtain the original assets.
- Spectral metals, glass behavior, and coated diffuse materials are approximations; exact mappings are in the conversion report.
