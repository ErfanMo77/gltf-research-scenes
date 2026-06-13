# Veach Ajar

![Veach Ajar reference](source/TungstenRender.png)

A Veach lighting test scene converted from PBRT v4 to glTF. It contains three teapot instances with different materials. This is a good scene for checking indirect lighting, since light reaches the visible objects mostly through multiple bounces from the area light behind the door.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/veach_ajar_core.gltf`
- Extended glTF: `gltf/veach_ajar_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for transmission, IOR, and emissive-strength data.
- Texture image maps are converted from TGA to embedded PNG.
- The local source PBRT `Floor` material was changed from metallic to diffuse to match the reference image; the corrected floor checkerboard is baked to a PNG texture.
- The rectangular PBRT area light is represented with emissive mesh geometry.
- Spectral metals and glass behavior are approximations; exact mappings are in the conversion report.
