# Breakfast Room

![Breakfast Room reference](source/TungstenRender.png)

A warm interior scene converted from PBRT v4 to glTF. It is useful for checking textured PLY geometry, coated furniture materials, metallic fixtures, and indirect lighting in an environment-lit room.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [The Breakfast Room on Blend Swap](https://blendswap.com/blend/13363)
- Original author: Wig42
- Environment map: `source/textures/Skydome.pfm`, included in the CC-BY Breakfast Room source package
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/breakfast_room_core.gltf`
- Extended glTF: `gltf/breakfast_room_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for the richer clearcoat material data.
- Textures are converted from TGA to embedded PNG.
- Distant and infinite lights are preserved as metadata.
- Spectral metal behavior is approximated with glTF metallic materials.
