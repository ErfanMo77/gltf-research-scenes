# Material Testball

![Material Testball reference](source/TungstenRender.png)

A small material testball scene converted from PBRT v4 to glTF. Useful scene to check materials with clearcoat.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/material_testball_core.gltf`
- Extended glTF: `gltf/material_testball_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for the richer clearcoat material data.
- The procedural checkerboard is baked to a PNG texture.
- The infinite environment light is preserved as metadata.
- The original environment map is not redistributed here; it can be obtained from Bernhard Vogl's light probe collection at <http://dativ.at/lightprobes/>.
- This scene has mixed source licensing; check the local license file before reuse.
