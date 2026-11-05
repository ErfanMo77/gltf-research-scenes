# BMW M6

![BMW M6 reference](gltf/bmw-m6.png)

A BMW M6 car scene converted from PBRT v4 to glTF. Good for checking dense vehicle mesh import, clearcoat car paint, dielectric glass, aluminum conductors, and coated conductors.

## Source

- Collection: `mmp/pbrt-v4-scenes`
- Upstream scene: BMW M6
- Original model: BMW M6 2006 on Blend Swap
- Original author: tyrant monkey
- Environment map: [Sunflowers HDRI on Poly Haven](https://polyhaven.com/a/sunflowers), CC0
- License: `source/BLENDSWAP_LICENSE.txt`

## Outputs

- Core glTF: `gltf/bmw_m6_core.gltf`
- Extended glTF: `gltf/bmw_m6_extended.gltf`
- Environment map: `../common/sunflowers_environment.hdr`, shared by several scenes and licensed as described in `../common/sunflowers_environment_LICENSE.txt`
- Conversion report: `gltf/conversion.yaml`

## Notes

- glTF has no environment light, so load the provided HDR environment map separately. It is stored once in `scenes/common`.
- `coatedconductor` materials are approximated as metallic glTF materials, with clearcoat in the extended output.
- The `mix` material is approximated as a weighted base color.
- PBRT named aluminum spectra are sampled to RGB for glTF metallic base color.
