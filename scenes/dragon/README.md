# Dragon

![Dragon reference](source/TungstenRender.png)

A dragon model scene converted from PBRT v4 to glTF. This is a dense mesh import case, with simple diffuse material.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [Dragon on Blend Swap](https://blendswap.com/blend/15891)
- Original author: Delatronic
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/dragon_core.gltf`
- Extended glTF: `gltf/dragon_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- The scene uses diffuse materials only.
- The PBRT distant light is preserved as metadata.
- Render settings and camera film parameters are preserved in glTF extras and the conversion report.
