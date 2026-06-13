# Teapot

![Teapot reference](source/TungstenRender.png)

A compact Utah teapot scene converted from PBRT v4 to glTF. Useful for checking clearcoat-style materials.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/teapot_core.gltf`
- Extended glTF: `gltf/teapot_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for the richer clearcoat material data.
- The procedural checkerboard is baked to a PNG texture.
- The infinite environment light is preserved as metadata.
- The original environment map is not redistributed here; it can be obtained from Bernhard Vogl's light probe collection at <http://dativ.at/lightprobes/>.
- This scene has mixed source licensing; check the local license file before reuse.
