# Cornell Caustic

![Cornell Caustic reference](source/TungstenRender.png)

A Cornell Box caustics scene converted from PBRT v4 to glTF. Useful for checking dielectric transmission, IOR handling, emissive mesh lighting, and whether a renderer can reproduce the caustics patterns.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/cornell_caustic_core.gltf`
- Extended glTF: `gltf/cornell_caustic_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for transmission, IOR, and emissive-strength data.
- The PBRT source uses the SPPM integrator to render the scene.
- The rectangular PBRT area light is represented with emissive mesh geometry.
- Caustics are not preserved directly in glTF; the water material and lighting are approximations documented in the conversion report.
