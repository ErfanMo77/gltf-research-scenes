# Teapot Full

![Full teapot reference](source/TungstenRender.png)

A fuller Utah teapot scene converted from PBRT v4 to glTF. This is useful for checking glass and liquid volume approximation.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/teapot_full_core.gltf`
- Extended glTF: `gltf/teapot_full_extended.gltf`
- Environment map: `../common/sunflowers_environment.hdr`, shared by several scenes and licensed as described in `../common/sunflowers_environment_LICENSE.txt`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for transmission, IOR, and volume attenuation data.
- Medium interfaces are preserved in metadata, not reproduced as full PBRT boundary tracking.
- The procedural checkerboard is baked to a PNG texture.
- The environment map is exported as an equirectangular HDR in glTF world orientation. glTF has no environment light, so load the provided HDR environment map separately. It substitutes the CC0 [Sunflowers HDRI](https://polyhaven.com/a/sunflowers) shared with `bmw-m6`; apply the `intensity_scale` in the conversion report, which matches the original light probe's mean luminance.
- The original environment map is not redistributed here; it can be obtained from Bernhard Vogl's light probe collection at <http://dativ.at/lightprobes/>.
- `source/LICENSE.txt` excludes the original environment map from CC0. That map is not included here, so the scene's files in this repository are CC0.
