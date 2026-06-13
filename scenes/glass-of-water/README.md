# Glass of Water

![Glass of Water reference](source/TungstenRender.png)

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

- Use the extended glTF for transmission and IOR material properties.
- The core glTF uses alpha-blended fallbacks for transparent materials.
- The PBRT area light is represented with emissive mesh geometry.
- Spectral metal and dielectric behavior are approximations; exact mappings are in the conversion report.
