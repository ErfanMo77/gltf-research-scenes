# glTF Research Scenes

[![glTF Validation](https://github.com/ErfanMo77/gltf-research-scenes/actions/workflows/validate-gltf.yml/badge.svg)](https://github.com/ErfanMo77/gltf-research-scenes/actions/workflows/validate-gltf.yml)

glTF 2.0 versions of commonly used graphics research scenes, with conversion metadata and documented limitations.

<p align="center">
  <img src="docs/preview.jpg" width="100%" alt="Collage of glTF research scene reference renders">
</p>

<p align="center">
  <em>A preview of selected glTF scenes included in the repository.</em>
</p>

Many well-known research scenes are distributed in renderer-specific formats such as PBRT. Those formats are useful for offline rendering, but less convenient for real-time engines, ray-tracing and path-tracing experiments, importer tests, and custom renderer prototypes.

This repository provides glTF 2.0 adaptations of those scenes so they are easier to inspect, load, compare, and reuse. The original source scenes remain the reference; the glTF outputs are documented approximations.

Each scene includes the generated glTF assets and metadata describing how the conversion was done. The scenes are converted with Python scripts, then manually checked against the original files and available reference renders.

glTF scenes are validated in GitHub Actions with the Khronos glTF Validator.

## glTF variants

Each scene includes two generated glTF variants:

- `*_core.gltf`: standard glTF 2.0 material model, for easier loading in engines.
- `*_extended.gltf`: a richer material mapping using supported glTF extensions, with PBRT-specific information preserved in `extras` and `conversion.yaml`

For basic importer and engine testing, use the `core` version. And use the `extended` version for richer material representation and PBRT conversion details.

## Download

Download the [`v1.0.0 release`](https://github.com/ErfanMo77/gltf-research-scenes/releases/tag/v1.0.0) if you only need the packaged `.glb` files and do not need the source PBRT files or separate `.gltf` outputs.

Clone the repository for the full asset set: sources, .gltf files, buffers, textures, metadata, and licenses.

## Scenes

| Scene | Reference | License | Notes |
| --- | --- | --- | --- |
| [`breakfast-room`](scenes/breakfast-room/) | <img src="scenes/breakfast-room/breakfast_room_thumbnail.png" width="160" alt="Breakfast Room reference"> | CC-BY-3.0 | Textured interior with metallic fixtures, environment map data, and distant-light data |
| [`bathroom`](scenes/bathroom/) | <img src="scenes/bathroom/bathroom_thumbnail.png" width="160" alt="Bathroom reference"> | CC0-1.0 | Large bathroom interior with glass, alpha masking, and emissive mesh lighting |
| [`bathroom2`](scenes/bathroom2/) | <img src="scenes/bathroom2/bathroom2_thumbnail.png" width="160" alt="Bathroom 2 reference"> | CC-BY-3.0 | Bathroom interior with textured coated wood, rough glass, mirrors, and emissive mesh lighting |
| [`bmw-m6`](scenes/bmw-m6/) | <img src="scenes/bmw-m6/bmw_m6_thumbnail.png" width="160" alt="BMW M6 reference"> | CC0-1.0 | Vehicle scene with clearcoat paint, dielectric glass, aluminum metals, coated conductors, and environment map data |
| [`classroom`](scenes/classroom/) | <img src="scenes/classroom/classroom_thumbnail.png" width="160" alt="Classroom reference"> | CC-BY-3.0 | Classroom interior with textured wood, clearcoat materials, metals, environment map data, and distant-light data |
| [`coffee-maker`](scenes/coffee-maker/) | <img src="scenes/coffee-maker/coffee_maker_thumbnail.png" width="160" alt="Coffee Maker reference"> | CC-BY-3.0 | Compact appliance scene with coated plastics, glass, metal, and emissive mesh lighting |
| [`cornell-box`](scenes/cornell-box/) | <img src="scenes/cornell-box/cornell_box_thumbnail.png" width="160" alt="Cornell Box reference"> | CC0-1.0 | Small diffuse box scene with emissive mesh lighting |
| [`cornell-caustic`](scenes/cornell-caustic/) | <img src="scenes/cornell-caustic/cornell_caustic_thumbnail.png" width="160" alt="Cornell Caustic reference"> | CC0-1.0 | Cornell Box caustics scene with dielectric water and emissive mesh lighting |
| [`dragon`](scenes/dragon/) | <img src="scenes/dragon/dragon_thumbnail.png" width="160" alt="Dragon reference"> | CC-BY-3.0 | Dense dragon model scene with diffuse materials and distant-light data |
| [`glass-of-water`](scenes/glass-of-water/) | <img src="scenes/glass-of-water/glass_of_water_thumbnail.png" width="160" alt="Glass of Water reference"> | CC0-1.0 | Transparent glass, water, ice, and emissive mesh lighting test |
| [`house`](scenes/house/) | <img src="scenes/house/house_thumbnail.png" width="160" alt="House reference"> | CC0-1.0 | Large Victorian house with glass, environment map data, and distant-light data |
| [`kitchen`](scenes/kitchen/) | <img src="scenes/kitchen/kitchen_thumbnail.png" width="160" alt="Kitchen reference"> | CC-BY-3.0 | Detailed kitchen with textures, glass, metals, and emissive mesh lighting |
| [`lamp`](scenes/lamp/) | <img src="scenes/lamp/lamp_thumbnail.png" width="160" alt="Lamp reference"> | CC0-1.0 | Desk lamp with coated plastic, metals, bulb glass, and emissive mesh lighting |
| [`living-room`](scenes/living-room/) | <img src="scenes/living-room/living_room_thumbnail.png" width="160" alt="Living Room reference"> | CC-BY-3.0 | Textured interior with leaf cutouts, mirrors, glass, and environment map data |
| [`living-room-2`](scenes/living-room-2/) | <img src="scenes/living-room-2/living_room_2_thumbnail.png" width="160" alt="Living Room 2 reference"> | CC-BY-3.0 | White living room interior with textured props, clearcoat materials, glass, and emissive mesh lighting |
| [`material-testball`](scenes/material-testball/) | <img src="scenes/material-testball/material_testball_thumbnail.png" width="160" alt="Material Testball reference"> | Mixed; see scene license | Compact material ball with baked checkerboard and environment map data |
| [`modern-hall`](scenes/modern-hall/) | <img src="scenes/modern-hall/modern_hall_thumbnail.png" width="160" alt="Modern Hall reference"> | CC-BY-3.0 | Modern hallway interior with textured surfaces, volumetric glass, and disk emissive mesh lighting |
| [`pontiac-gto`](scenes/pontiac-gto/) | <img src="scenes/pontiac-gto/pontiac_gto_thumbnail.png" width="160" alt="Pontiac GTO reference"> | CC0-1.0 | Vehicle scene with clearcoat car paint, glass, chrome, and environment map data |
| [`spaceship`](scenes/spaceship/) | <img src="scenes/spaceship/spaceship_thumbnail.png" width="160" alt="Spaceship reference"> | CC0-1.0 | Sci-fi model with metals, glass, emissive mesh lighting, and environment map data |
| [`staircase`](scenes/staircase/) | <img src="scenes/staircase/staircase_thumbnail.png" width="160" alt="Staircase reference"> | CC-BY-3.0 | Wooden staircase interior with portrait camera and emissive mesh lighting |
| [`teapot`](scenes/teapot/) | <img src="scenes/teapot/teapot_thumbnail.png" width="160" alt="Teapot reference"> | Mixed; see scene license | Teapot with baked checkerboard and environment map data |
| [`teapot-full`](scenes/teapot-full/) | <img src="scenes/teapot-full/teapot_full_thumbnail.png" width="160" alt="Full teapot reference"> | Mixed; see scene license | Teapot and liquid scene with volume, medium settings, and environment map data |
| [`veach-ajar`](scenes/veach-ajar/) | <img src="scenes/veach-ajar/veach_ajar_thumbnail.png" width="160" alt="Veach Ajar reference"> | CC0-1.0 | Veach lighting scene with transformed meshes, glass, and emissive mesh lighting |
| [`veach-bidir`](scenes/veach-bidir/) | <img src="scenes/veach-bidir/veach_bidir_thumbnail.png" width="160" alt="Veach Bidir reference"> | CC0-1.0 | Small bidirectional-lighting scene with emissive mesh lighting |
| [`veach-mis`](scenes/veach-mis/) | <img src="scenes/veach-mis/veach_mis_thumbnail.png" width="160" alt="Veach MIS reference"> | CC0-1.0 | Compact MIS scene with tessellated emissive mesh lighting |
| [`vintage-car`](scenes/vintage-car/) | <img src="scenes/vintage-car/vintage_car_thumbnail.png" width="160" alt="Vintage Car reference"> | Mixed; see scene license | Vehicle scene with clearcoat car paint, glass, chrome, rough steel, and environment map data |

## Limitations

Some PBRT scene features are outside the current conversion scope because glTF cannot represent them directly and a practical approximation is not always available. B-spline curves used for fur, hair, or carpet fibers are the main example: converting them to triangle meshes can make the generated assets too large, so scenes that depend on them are not currently included.

The included scenes were selected because their important geometry, materials, textures, lighting, cameras, and render settings can be represented in glTF or approximated with supported glTF features. PBRT-only details are recorded in glTF `extras` and `conversion.yaml`.

The generated glTF files do not use explicit light objects. Base glTF 2.0 has no light object, and `KHR_lights_punctual` only supports `directional`, `point`, and `spot` lights. This repository does not emit that extension. PBRT area lights are converted to emissive mesh geometry using the source emitter shape and size, which better matches how path tracing engines model finite-area emitters. PBRT distant and infinite lights are preserved as metadata.

## Generated Outputs

Each scene's `gltf/` directory contains:

- `scenes/<scene-id>/gltf/<scene_id>_core.gltf`
- `scenes/<scene-id>/gltf/<scene_id>_extended.gltf`
- `scenes/<scene-id>/gltf/<scene_id>.bin`
- `scenes/<scene-id>/gltf/conversion.yaml`

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

## License

Project-authored docs and metadata are MIT licensed.

Third-party scene assets keep their original licenses. Converted glTF assets are derivative scene assets and retain the source scene license unless a scene-specific note says otherwise.
