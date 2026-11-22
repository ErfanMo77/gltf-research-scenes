# SSS Dragon

![SSS Dragon reference at scale 50](gltf/sss_dragon_vk_50.png)

The Stanford Asian Dragon scan, converted from PBRT v4 with three `Skin1` subsurface-scattering densities.

## Source

- [PBRT v4 SSS Dragon scene](https://github.com/mmp/pbrt-v4-scenes/tree/30cf4a0346ae5a80a2d7a530a3ef7d0fa4f70572/sssdragon)
- [XYZ RGB Inc. scan attribution and Stanford 3D Scanning Repository terms](source/LICENSE.txt)
- [Original PBRT render at scale 10](source/dragon_10.png)

## Outputs

The release collection, `gltf_research_scenes_glb.zip`, includes `sss_dragon_core.glb` and `sss_dragon_extended.glb`.

- [Core glTF](gltf/sss_dragon_core.gltf) and [extended glTF](gltf/sss_dragon_extended.gltf) share `sss_dragon.bin`.
- [Conversion report and reference render settings](gltf/conversion.yaml)
- [Small Rural Road environment map](gltf/sss_dragon_environment.hdr) with [CC0 attribution](gltf/sss_dragon_environment_LICENSE.txt)
- Reference renders for [scale 10](gltf/sss_dragon_vk_10.png), [scale 50](gltf/sss_dragon_vk_50.png), and [scale 250](gltf/sss_dragon_vk_250.png).

![PBRT v4 and vk_gltf_renderer compared at SSS Dragon scattering scales 10, 50, and 250](gltf/sss_dragon_vk_comparison.png)

Original PBRT v4 renders (left) and earlier vk_gltf_renderer previews (right) show scales 10, 50, and 250 from top to bottom.

## Notes

The core uses a diffuse approximation. The extended glTF opens at scale 50 and offers all three densities through `KHR_materials_variants`. Higher scales shorten the scattering distance. Loading the extended material requires support for the [draft `KHR_materials_scatter` extension](https://github.com/KhronosGroup/glTF/pull/2579).

The conversion removes a detached 139-triangle patch and preserves the closed 7,218,906-triangle dragon shell. The glTF camera keeps the PBRT eye position, viewing direction, roll, and film aspect ratio.

The Small Rural Road HDRI lights the scene at strength 1.0. The coated ground fills the background. All three reference renders use the same camera, environment, and settings. They were rendered at 1366 by 1024 with 384 samples per pixel and a 50-bounce limit. [vk_gltf_renderer at `a7d0747`](https://github.com/nvpro-samples/vk_gltf_renderer/commit/a7d0747f06df832e564ff3e93078e5c06a7b6f12)
