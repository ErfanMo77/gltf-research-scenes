# Teapot Full

![Full teapot reference](source/TungstenRender.png)

A fuller Utah teapot scene converted from PBRT v4 to glTF. This is useful for checking glass and liquid volume approximation.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/teapot_full_core.gltf`
- Extended glTF: `gltf/teapot_full_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for transmission, IOR, and volume attenuation data.
- Medium interfaces are preserved in metadata, not reproduced as full PBRT boundary tracking.
- The procedural checkerboard is baked to a PNG texture.
- The infinite environment light is preserved as metadata.
- The original environment map is not redistributed here; it can be obtained from Bernhard Vogl's light probe collection at <http://dativ.at/lightprobes/>.
- This scene has mixed source licensing; check the local license file before reuse.
