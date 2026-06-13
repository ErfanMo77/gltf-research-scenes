# House

![House reference](source/TungstenRender.png)

A large Victorian house scene converted from PBRT v4 to glTF. This scene contains large PLY geometry. It's useful for checking culling behavior, glass materials, GI, and indirect environment map lighting.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [Victorian Style House on Blend Swap](https://blendswap.com/blend/12687)
- Environment map: `source/textures/Skydome.pfm`, included with the CC0 House source package
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/house_core.gltf`
- Extended glTF: `gltf/house_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Materials are emitted double-sided for engine culling compatibility.
- The texture image map is converted from TGA to embedded PNG.
- Use the extended glTF for transmission and IOR data on glass materials.
- Infinite and distant lights are preserved as metadata.
