# Vintage Car

![Vintage Car reference](source/TungstenRender.png)

An old vintage car model converted from PBRT v4 to glTF. It is useful for checking large vehicle geometry, clearcoat car paint, glass transmission, and chrome and steel metal approximation.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [Old vintage car on Blend Swap](https://blendswap.com/blend/14205)
- Original author: piopis
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/vintage_car_core.gltf`
- Extended glTF: `gltf/vintage_car_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for clearcoat, transmission, IOR, and specular data.
- The scene contains 48 meshes and 771,776 triangles.
- The infinite light is preserved as metadata.
- The original environment map is not redistributed here; it is from Bernhard Vogl's light probe collection at <http://dativ.at/lightprobes/> and has separate attribution/non-commercial terms.
- Spectral metals, glass behavior, and coated diffuse materials are approximations; exact mappings are in the conversion report.
