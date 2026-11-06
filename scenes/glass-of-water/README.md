# Glass of Water

![Glass of Water reference](gltf/glass-of-water.png)

A transparent-material test scene converted from PBRT v4 to glTF. Useful for checking layered glass materials, refraction, IOR handling, and specular light paths with metallic background material.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [Glass of Water on Blend Swap](https://blendswap.com/blend/10186)
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/glass_of_water_core.gltf`
- Extended glTF: `gltf/glass_of_water_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for transmission, IOR, and volume material properties.
- The water, ice, and glass materials use `KHR_materials_volume` so renderers treat them as solid refractive volumes instead of the default thin-walled surfaces. `thicknessFactor` is set to the largest bounding-box extent of the meshes using each material, the same convention as the other scenes; it only approximates thickness for rasterizers and has no effect on path tracers that trace the actual geometry.
- The core glTF uses alpha-blended fallbacks for transparent materials.
- The PBRT area light is represented with emissive mesh geometry.
- Spectral metal and dielectric behavior are approximations; exact mappings are in the conversion report.
