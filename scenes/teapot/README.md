# Teapot

![Teapot reference](source/TungstenRender.png)

A compact Utah teapot scene converted from PBRT v4 to glTF. Useful for checking clearcoat-style materials.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/teapot_core.gltf`
- Extended glTF: `gltf/teapot_extended.gltf`
- Environment map: `../common/sunflowers_environment.hdr`, shared by several scenes and licensed as described in `../common/sunflowers_environment_LICENSE.txt`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for the richer clearcoat material data.
- The procedural checkerboard is baked to a PNG texture.
- glTF has no environment light, so load the provided HDR environment map separately. It substitutes the CC0 [Sunflowers HDRI](https://polyhaven.com/a/sunflowers) shared with `bmw-m6`; apply the `intensity_scale` in the conversion report, which matches the original light probe's mean luminance.
- The original environment map is not redistributed here; it can be obtained from Bernhard Vogl's light probe collection at <http://dativ.at/lightprobes/>.
- `source/LICENSE.txt` excludes the original environment map from CC0. That map is not included here, so the scene's files in this repository are CC0.
