# Classroom 2

![Classroom 2 reference](gltf/classroom2.png)

Christophe Seux's Classroom demo, exported from Blender to glTF. This is a different scene from the [Japanese classroom](../classroom/).

The scene is supplied as [classroom2.glb](gltf/classroom2.glb), with its textures, camera, and a directional light embedded in one file.

Source: [Blender demo files](https://www.blender.org/download/demo-files/). License: [CC0](source/LICENSE.txt). The original [ReadMe](source/ReadMe.txt) is included.

The GLB was exported from Blender 5.3.

- Directional light: `KHR_lights_punctual`, intensity **85**, linear RGB **[1, 0.9, 0.8]**. Import/export uses **Unitless (`COMPAT`)** so intensity is preserved.
- Environment: [shared Sunflowers HDRI](../common/sunflowers_environment.hdr), strength **8**, equirectangular, with no rotation. Attribution and CC0 license: [environment license](../common/sunflowers_environment_LICENSE.txt).
