# Cornell Caustic

![Cornell Caustic PBRT v4 SPPM reference](gltf/cornell-caustic_pbrt-sppm.png)

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
- The generated reference render comes from PBRT v4 using its stochastic progressive photon mapping (SPPM) integrator.
- The rectangular PBRT area light is represented with emissive mesh geometry.
- Blender Cycles could not produce good-quality caustics for this scene, even at 4096 samples per pixel with MNEE shadow caustics enabled. The result remained substantially too dark and missed important caustic illumination.
- Reproducing this scene's reference quality requires a photon-mapping renderer, such as PBRT v4 with SPPM.
- Caustics are not preserved directly in glTF; the water material and lighting are approximations documented in the conversion report.
