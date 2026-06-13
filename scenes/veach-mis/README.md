# Veach MIS

![Veach MIS reference](source/TungstenRender.png)

A compact Veach multiple-importance-sampling test scene converted from PBRT v4 to glTF. It is built around glossy metal plates lit by small sphere area lights with different sizes and intensities, making it a useful scene for checking direct-light sampling, MIS behavior, and rough conductor materials.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/veach_mis_core.gltf`
- Extended glTF: `gltf/veach_mis_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for emissive-strength data on the sphere lights.
- PBRT analytic sphere lights are tessellated to mesh geometry.
- Sphere area lights are represented with emissive materials.
- Spectral metal behavior is approximated; exact mappings are in the conversion report.
