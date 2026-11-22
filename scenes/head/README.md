# Head

![Head reference rendered in vk_gltf_renderer](gltf/head_vk.png)

An Infinite Realities head scan converted from PBRT v4 to glTF. The extended scene uses textured subsurface scattering for the skin.

## Source

- [PBRT v4 Head scene](https://github.com/mmp/pbrt-v4-scenes/tree/30cf4a0346ae5a80a2d7a530a3ef7d0fa4f70572/head)
- [Scan and albedo attribution and license (CC BY 2.0)](source/LICENSE.txt)
- [Original PBRT render](source/head.png)

## Outputs

The release collection, `gltf_research_scenes_glb.zip`, includes `head_core.glb` and `head_extended.glb`.

- [Core glTF](gltf/head_core.gltf) and [extended glTF](gltf/head_extended.gltf) share `head.bin`.
- [Conversion report and reference render settings](gltf/conversion.yaml)
- [Small Rural Road environment map](gltf/head_environment.hdr) with [CC0 attribution](gltf/head_environment_LICENSE.txt)

## Notes

The core material uses the skin texture as diffuse base color. The extended material uses it as `multiscatterColorTexture` and derives extinction from PBRT's RGB mean free path to approximate its diffusion model. Loading the extended version requires support for the [draft `KHR_materials_scatter` extension](https://github.com/KhronosGroup/glTF/pull/2579). Blender 5.3 imports the core version. Rendering subsurface scattering in Cycles requires setting up the skin material separately.

The Small Rural Road HDRI lights the scene at strength 1.0 and appears in the reference background. [Environment map](gltf/head_environment.hdr)

The reference uses the extended glTF and its camera, with 2,048 samples per pixel and a 40-bounce limit. It was rendered at  1080p with [vk_gltf_renderer at `a7d0747`](https://github.com/nvpro-samples/vk_gltf_renderer/commit/a7d0747f06df832e564ff3e93078e5c06a7b6f12).

Set `ptShadowTransmission` to `0` for this scene. With the straight-through shadow approximation enabled, the skin's volume lighting showed distinct bands across the forehead. The report records the lens, denoiser, and exposure settings used for the reference.

The glTF camera preserves PBRT's eye position, viewing direction, roll, and film aspect ratio. The geometry and HDRI are reflected across the camera's vertical plane to convert handedness while preserving screen orientation. The glTF reference shows the full frame. The original PBRT render uses the crop recorded in the conversion report.
