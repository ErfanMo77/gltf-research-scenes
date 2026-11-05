# Cornell Box

![Cornell Box reference](gltf/cornell-box.png)

A compact Cornell Box conversion from PBRT v4 to glTF. Useful as a small test scene for diffuse global illumination, and color bleeding with emissive mesh lighting.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/cornell_box_core.gltf`
- Extended glTF: `gltf/cornell_box_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- This is the smallest scene in the set and is a good scene for quick glTF import testing.
- The rectangular PBRT area light is represented with emissive mesh geometry.
- Its glTF light material has `doubleSided: false`, matching PBRT's one-sided emission. The Cycles render also masks backface emission explicitly because material backface culling alone does not restrict it.
- Original light radiance and render settings are preserved in metadata.
