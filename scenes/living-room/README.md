# Living Room

![Living Room reference](source/TungstenRender.png)

A textured living-room interior converted from PBRT v4 to glTF. It is useful for checking image textures, leaf cutouts, mirrors, glass, and clearcoat materials.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [The Grey & White Room on Blend Swap](https://blendswap.com/blend/13552)
- Original author: Wig42
- Environment map: `source/textures/Sky 19.pfm`, included in the CC-BY Grey & White Room source package
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/living_room_core.gltf`
- Extended glTF: `gltf/living_room_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for clearcoat, transmission, and IOR data.
- Texture image maps are converted from TGA to embedded PNG.
- Leaf alpha is derived from the source texture's white backing; transmittance remains metadata.
- The infinite environment light is preserved as metadata.
- Spectral metals and glass behavior are approximations; exact mappings are in the conversion report.
