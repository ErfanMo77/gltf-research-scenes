# glTF Research Scenes

[![glTF Validation](https://github.com/ErfanMo77/gltf-research-scenes/actions/workflows/validate-gltf.yml/badge.svg)](https://github.com/ErfanMo77/gltf-research-scenes/actions/workflows/validate-gltf.yml)

glTF 2.0 versions of commonly used graphics research scenes, with conversion metadata and documented limitations.

<p align="center">
  <img src="docs/preview.jpg" width="100%" alt="Collage of glTF research scene reference renders">
</p>

<p align="center">
  <em>A preview of selected glTF scenes included in the repository.</em>
</p>

Many well-known research scenes are distributed in renderer-specific formats such as PBRT. Those formats are useful for offline renderers, but less convenient to use in real-time engines, and web experiments.

This repository provides glTF 2.0 adaptations of those scenes so they are easier to inspect, load, and reuse. The glTF outputs are close approximations of the original scenes.

Each scene includes glTF assets and metadata describing how the conversion was done. PBRT scenes were converted with Python scripts, then manually checked against the original files and reference renders.

glTF scenes are validated in GitHub Actions with the Khronos glTF Validator.

## glTF variants

PBRT scenes include two generated glTF variants:

- `*_core.gltf`: standard glTF 2.0 material model, for easier loading in engines.
- `*_extended.gltf`: a richer material mapping using supported glTF extensions.

For basic importer and engine testing, use the `core` version. And use the `extended` version for richer material representation.

Classroom 2 is supplied as a single `classroom2.glb`, with its textures and camera embedded.

[Transparent Machines](scenes/transparent-machines/) requires `EXT_mesh_gpu_instancing` in both variants. Its five frames are separate glTF scenes, each with its own camera.

## Download

Download the [`latest release`](https://github.com/ErfanMo77/gltf-research-scenes/releases/latest) if you only need the packaged `.glb` files.

Clone the repository for the full asset set: sources, .gltf files, textures, metadata, and licenses.

## Scenes

Each scene's reference image is a Blender 5.3 Cycles render of its extended glTF, saved in the scene's gltf/ folder. Render settings are recorded in the `reference_render` section of each `conversion.yaml`. With them, you can reproduce the render in Blender and compare your own renderer's output against the reference.

Cornell Caustic is the exception: its reference is a PBRT v4 render using photon mapping (SPPM), because Cycles could not reproduce its caustics.

| Scene | Reference | License | Notes |
| --- | --- | --- | --- |
| [`breakfast-room`](scenes/breakfast-room/) | <a href="scenes/breakfast-room/gltf/breakfast-room.png"><img src="scenes/breakfast-room/breakfast_room_thumbnail.png" width="160" alt="Breakfast Room reference"></a> | CC-BY-3.0 | Textured interior with metallic fixtures, environment map data, and a directional light |
| [`bathroom`](scenes/bathroom/) | <a href="scenes/bathroom/gltf/bathroom.png"><img src="scenes/bathroom/bathroom_thumbnail.png" width="160" alt="Bathroom reference"></a> | CC0-1.0 | Large bathroom interior with glass, alpha masking, and emissive mesh lighting |
| [`bathroom2`](scenes/bathroom2/) | <a href="scenes/bathroom2/gltf/bathroom2.png"><img src="scenes/bathroom2/bathroom2_thumbnail.png" width="160" alt="Bathroom 2 reference"></a> | CC-BY-3.0 | Bathroom interior with textured coated wood, rough glass, mirrors, and emissive mesh lighting |
| [`bmw-m6`](scenes/bmw-m6/) | <a href="scenes/bmw-m6/gltf/bmw-m6.png"><img src="scenes/bmw-m6/bmw_m6_thumbnail.png" width="160" alt="BMW M6 reference"></a> | CC0-1.0 | Vehicle scene with clearcoat paint, dielectric glass, aluminum metals, coated conductors, and environment map data |
| [`classroom`](scenes/classroom/) | <a href="scenes/classroom/gltf/classroom.png"><img src="scenes/classroom/classroom_thumbnail.png" width="160" alt="Classroom reference"></a> | CC-BY-3.0 | Classroom interior with textured wood, clearcoat materials, metals, environment map data, and a directional light |
| [`classroom2`](scenes/classroom2/) | <a href="scenes/classroom2/gltf/classroom2.png"><img src="scenes/classroom2/classroom2_thumbnail.png" width="160" alt="Classroom 2 reference"></a> | CC0-1.0 | Blender Classroom by Christophe Seux, supplied as one GLB with embedded textures and camera |
| [`coffee-maker`](scenes/coffee-maker/) | <a href="scenes/coffee-maker/gltf/coffee-maker.png"><img src="scenes/coffee-maker/coffee_maker_thumbnail.png" width="160" alt="Coffee Maker reference"></a> | CC-BY-3.0 | Compact appliance scene with coated plastics, glass, metal, and emissive mesh lighting |
| [`cornell-box`](scenes/cornell-box/) | <a href="scenes/cornell-box/gltf/cornell-box.png"><img src="scenes/cornell-box/cornell_box_thumbnail.png" width="160" alt="Cornell Box reference"></a> | CC0-1.0 | Small diffuse box scene with emissive mesh lighting |
| [`cornell-caustic`](scenes/cornell-caustic/) | <a href="scenes/cornell-caustic/gltf/cornell-caustic_pbrt-sppm.png"><img src="scenes/cornell-caustic/cornell_caustic_thumbnail.png" width="160" alt="Cornell Caustic reference"></a> | CC0-1.0 | Cornell Box caustics scene with dielectric water and emissive mesh lighting |
| [`crown`](scenes/crown/) | <a href="scenes/crown/gltf/crown.png"><img src="scenes/crown/crown_thumbnail.png" width="160" alt="Crown reference"></a> | CC-BY-3.0 | Austrian Imperial Crown with gold conductors, gemstones with dispersion, iridescent pearls, sheen velvet, height map baked into geometry, and emissive mesh lighting |
| [`dragon`](scenes/dragon/) | <a href="scenes/dragon/gltf/dragon.png"><img src="scenes/dragon/dragon_thumbnail.png" width="160" alt="Dragon reference"></a> | CC-BY-3.0 | Dense dragon model scene with diffuse materials and a directional light |
| [`glass-of-water`](scenes/glass-of-water/) | <a href="scenes/glass-of-water/gltf/glass-of-water.png"><img src="scenes/glass-of-water/glass_of_water_thumbnail.png" width="160" alt="Glass of Water reference"></a> | CC0-1.0 | Transparent glass, water, ice, and emissive mesh lighting test |
| [`house`](scenes/house/) | <a href="scenes/house/gltf/house.png"><img src="scenes/house/house_thumbnail.png" width="160" alt="House reference"></a> | CC0-1.0 | Large Victorian house with glass, environment map data, and a directional light |
| [`kitchen`](scenes/kitchen/) | <a href="scenes/kitchen/gltf/kitchen.png"><img src="scenes/kitchen/kitchen_thumbnail.png" width="160" alt="Kitchen reference"></a> | CC-BY-3.0 | Detailed kitchen with textures, glass, metals, and emissive mesh lighting |
| [`lamp`](scenes/lamp/) | <a href="scenes/lamp/gltf/lamp.png"><img src="scenes/lamp/lamp_thumbnail.png" width="160" alt="Lamp reference"></a> | CC0-1.0 | Desk lamp with coated plastic, metals, bulb glass, emissive mesh lighting, and a directional light |
| [`living-room`](scenes/living-room/) | <a href="scenes/living-room/gltf/living-room.png"><img src="scenes/living-room/living_room_thumbnail.png" width="160" alt="Living Room reference"></a> | CC-BY-3.0 | Textured interior with leaf cutouts, mirrors, glass, and environment map data |
| [`living-room-2`](scenes/living-room-2/) | <a href="scenes/living-room-2/gltf/living-room-2.png"><img src="scenes/living-room-2/living_room_2_thumbnail.png" width="160" alt="Living Room 2 reference"></a> | CC-BY-3.0 | White living room interior with textured props, clearcoat materials, glass, and emissive mesh lighting |
| [`material-testball`](scenes/material-testball/) | <a href="scenes/material-testball/gltf/material-testball.png"><img src="scenes/material-testball/material_testball_thumbnail.png" width="160" alt="Material Testball reference"></a> | CC0-1.0 | Compact material ball with baked checkerboard and environment map data |
| [`modern-hall`](scenes/modern-hall/) | <a href="scenes/modern-hall/gltf/modern-hall.png"><img src="scenes/modern-hall/modern_hall_thumbnail.png" width="160" alt="Modern Hall reference"></a> | CC-BY-3.0 | Modern hallway interior with textured surfaces, volumetric glass, and disk emissive mesh lighting |
| [`pontiac-gto`](scenes/pontiac-gto/) | <a href="scenes/pontiac-gto/gltf/pontiac-gto.png"><img src="scenes/pontiac-gto/pontiac_gto_thumbnail.png" width="160" alt="Pontiac GTO reference"></a> | CC0-1.0; environment map CC-BY-3.0 | Vehicle scene with clearcoat car paint, glass, chrome, and environment map data |
| [`spaceship`](scenes/spaceship/) | <a href="scenes/spaceship/gltf/spaceship.png"><img src="scenes/spaceship/spaceship_thumbnail.png" width="160" alt="Spaceship reference"></a> | CC0-1.0 | Sci-fi model with metals, glass, emissive mesh lighting, and environment map data |
| [`staircase`](scenes/staircase/) | <a href="scenes/staircase/gltf/staircase.png"><img src="scenes/staircase/staircase_thumbnail.png" width="160" alt="Staircase reference"></a> | CC-BY-3.0 | Wooden staircase interior with portrait camera and emissive mesh lighting |
| [`teapot`](scenes/teapot/) | <a href="scenes/teapot/gltf/teapot.png"><img src="scenes/teapot/teapot_thumbnail.png" width="160" alt="Teapot reference"></a> | CC0-1.0 | Teapot with baked checkerboard and environment map data |
| [`teapot-full`](scenes/teapot-full/) | <a href="scenes/teapot-full/gltf/teapot-full.png"><img src="scenes/teapot-full/teapot_full_thumbnail.png" width="160" alt="Full teapot reference"></a> | CC0-1.0 | Teapot and liquid scene with volume, medium settings, and environment map data |
| [`transparent-machines`](scenes/transparent-machines/) | <a href="scenes/transparent-machines/gltf/transparent-machines.png"><img src="scenes/transparent-machines/transparent_machines_thumbnail.png" width="160" alt="Transparent Machines reference"></a> | Beeple project terms | Five instanced BK7 glass frames with matching cameras, a reference render of each, and CC0 procedural sky and studio HDRs. Render with **64 or more max bounces**. Separate download |
| [`veach-ajar`](scenes/veach-ajar/) | <a href="scenes/veach-ajar/gltf/veach-ajar.png"><img src="scenes/veach-ajar/veach_ajar_thumbnail.png" width="160" alt="Veach Ajar reference"></a> | CC0-1.0 | Veach lighting scene with transformed meshes, glass, and emissive mesh lighting |
| [`veach-bidir`](scenes/veach-bidir/) | <a href="scenes/veach-bidir/gltf/veach-bidir.png"><img src="scenes/veach-bidir/veach_bidir_thumbnail.png" width="160" alt="Veach Bidir reference"></a> | CC0-1.0 | Small bidirectional-lighting scene with emissive mesh lighting |
| [`veach-mis`](scenes/veach-mis/) | <a href="scenes/veach-mis/gltf/veach-mis.png"><img src="scenes/veach-mis/veach_mis_thumbnail.png" width="160" alt="Veach MIS reference"></a> | CC0-1.0 | Compact MIS scene with tessellated emissive mesh lighting |
| [`vintage-car`](scenes/vintage-car/) | <a href="scenes/vintage-car/gltf/vintage-car.png"><img src="scenes/vintage-car/vintage_car_thumbnail.png" width="160" alt="Vintage Car reference"></a> | CC0-1.0 | Vehicle scene with clearcoat car paint, glass, chrome, rough steel, and environment map data |

## Limitations

Some PBRT scene features are outside the current conversion scope because glTF cannot represent them directly and a practical approximation is not always available. B-spline curves used for fur, hair, or carpet fibers are the main example: converting them to triangle meshes can make the generated assets too large, so scenes that depend on them are not currently included.

The included scenes were selected because their important geometry, materials, textures, lighting, cameras, and render settings can be represented in glTF or approximated with supported glTF features. PBRT-only details are recorded in glTF `extras` and `conversion.yaml`.

PBRT distant lights are included as `KHR_lights_punctual` directional lights in the extended glTF files. PBRT area lights are converted to emissive mesh geometry using the source emitter shape and size, which better matches how path tracing engines model finite-area emitters. glTF has no environment light, so PBRT image-based infinite lights are exported as separate HDR files beside the glTF. Light intensities use the same relative units as emissive strength; when importing into Blender, choose the **Unitless** lighting mode to keep that balance.

## Generated Outputs

Each PBRT scene's `gltf/` directory contains:

- `scenes/<scene-id>/gltf/<scene_id>_core.gltf`
- `scenes/<scene-id>/gltf/<scene_id>_extended.gltf`
- `scenes/<scene-id>/gltf/<scene_id>.bin`
- `scenes/<scene-id>/gltf/conversion.yaml`
- `scenes/<scene-id>/gltf/<scene_id>_environment.hdr` and `<scene_id>_environment_LICENSE.txt`, for scenes with their own image environment map

The `conversion.yaml` report may include:

- source files and license
- generated outputs
- geometry statistics
- material mapping
- light mapping
- render presets
- unsupported and approximated features

## References

- [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/) is the main source for most scenes in this repository. Thanks to Benedikt Bitterli for collecting and publishing the resources behind many of these conversions.
- [mmp/pbrt-v4-scenes](https://github.com/mmp/pbrt-v4-scenes) is another source for some of the PBRT v4 scenes used in this repository.
- [glTF 2.0 Specification](https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html): target asset format for the core outputs.
- [Khronos glTF Extension Registry](https://registry.khronos.org/glTF/): reference for optional glTF extensions used by richer outputs.
- [PBRT v4 File Format](https://www.pbrt.org/fileformat-v4): source format reference for PBRT scene parsing.
- [Physically Based Rendering: From Theory to Implementation, 4th Edition](https://www.pbr-book.org/4ed/contents): rendering reference for PBRT concepts and behavior.

## Contributing

Contributions are welcome. Before starting a pull request, please [open an issue](https://github.com/ErfanMo77/gltf-research-scenes/issues) so we can discuss the scope and the planned changes first. Issues are also the place to report problems with a scene, such as materials, lighting, or geometry issues.

More scenes will be added gradually. Each conversion takes time, because I check its materials and rendering manually against the original scene to keep it as accurate as possible.

## License

Project-authored docs and metadata are MIT licensed.

Third-party scene assets keep their original licenses. Converted glTF assets are derivative scene assets and retain the source scene license unless a scene-specific note says otherwise.
