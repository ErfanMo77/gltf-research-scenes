# Living Room

![Living Room reference](source/TungstenRender.png)

A textured living-room interior converted from PBRT v4 to glTF. It is useful for checking image textures, leaf cutouts, mirrors, glass, and clearcoat materials.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [The Grey & White Room on Blend Swap](https://blendswap.com/blend/13552)
- Original author: Wig42
- Environment map: the source's `textures/Sky 19.pfm` is not redistributed. Its origin and license cannot be verified, and the original Blend Swap author removed the DOSCH HDRI used for the scene.
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/living_room_core.gltf`
- Extended glTF: `gltf/living_room_extended.gltf`
- Environment map: `../common/sunflowers_environment.hdr`, shared by several scenes and licensed as described in `../common/sunflowers_environment_LICENSE.txt`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for clearcoat, transmission, and IOR data.
- Texture image maps are converted from TGA to embedded PNG.
- Leaf alpha is derived from the source texture's white backing; transmittance remains metadata.
- The environment map is exported as an equirectangular HDR in glTF world orientation. glTF has no environment light, so load the provided HDR environment map separately. It substitutes the CC0 [Sunflowers HDRI](https://polyhaven.com/a/sunflowers) shared with `bmw-m6`; apply the `intensity_scale` in the conversion report, which matches the original map's mean luminance.
- Spectral metals and glass behavior are approximations; exact mappings are in the conversion report.
