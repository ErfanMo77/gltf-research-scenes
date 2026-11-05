# Breakfast Room

![Breakfast Room reference](gltf/breakfast-room.png)

A warm interior scene converted from PBRT v4 to glTF. It is useful for checking textured PLY geometry, coated furniture materials, metallic fixtures, and indirect lighting in an environment-lit room.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [The Breakfast Room on Blend Swap](https://blendswap.com/blend/13363)
- Original author: Wig42
- Environment map: `source/textures/Skydome.pfm`, a render of the procedural sky in the Tungsten version, included in the CC-BY Breakfast Room source package
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/breakfast_room_core.gltf`
- Extended glTF: `gltf/breakfast_room_extended.gltf`
- Environment map: `gltf/breakfast_room_environment.hdr`, licensed as described in `gltf/breakfast_room_environment_LICENSE.txt`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for the richer clearcoat material data.
- Textures are converted from TGA to embedded PNG.
- The PBRT distant light is a `KHR_lights_punctual` directional light in the extended glTF. The environment map is exported as an equirectangular HDR in glTF world orientation. glTF has no environment light, so load the provided HDR environment map separately.
- Spectral metal behavior is approximated with glTF metallic materials.
