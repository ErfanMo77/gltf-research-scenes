# Classroom

![Classroom reference](source/TungstenRender.png)

A Japanese classroom interior converted from PBRT v4 to glTF. Useful for checking textured classroom furniture, clearcoat-style plastic and whiteboard materials, metallic chair and window frames.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [JapaneseClassroom on Blend Swap](https://blendswap.com/blend/13632)
- Original author: NovaZeeke
- Environment map: `source/textures/Skydome.pfm`, a render of the procedural sky in the Tungsten version, included in the CC-BY Japanese Classroom source package
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/classroom_core.gltf`
- Extended glTF: `gltf/classroom_extended.gltf`
- Environment map: `gltf/classroom_environment.hdr`, licensed as described in `gltf/classroom_environment_LICENSE.txt`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for clearcoat and specular data.
- Texture image maps are converted from TGA to embedded PNG.
- The scene contains 79 meshes and 103,832 triangles.
- The PBRT distant light is a `KHR_lights_punctual` directional light in the extended glTF. glTF has no environment light, so load the provided HDR environment map separately.
- Spectral metals and coated diffuse materials are approximations; exact mappings are in the conversion report.
