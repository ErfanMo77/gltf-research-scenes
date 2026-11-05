# Pontiac GTO

![Pontiac GTO reference](gltf/pontiac-gto.png)

A 1967 Pontiac GTO car model converted from PBRT v4 to glTF. It is useful for checking large vehicle geometry, clearcoat car paint, glass transmission, chrome and steel metal approximation, and leather materials.

## Source

- Collection: [Benedikt Bitterli Rendering Resources](https://benedikt-bitterli.me/resources/)
- Original model: [Pontiac GTO 67 on Blend Swap](https://blendswap.com/blend/13575)
- Original author: thecali
- Environment map: `source/textures/envmap.pfm`, from zbyg's [HDRi Pack 3](https://www.deviantart.com/zbyg/art/HDRi-Pack-3-112847728), CC-BY-3.0; see `source/ENVMAP_LICENSE.txt`
- License: `source/LICENSE.txt`

## Outputs

- Core glTF: `gltf/pontiac_gto_core.gltf`
- Extended glTF: `gltf/pontiac_gto_extended.gltf`
- Environment map: `gltf/pontiac_gto_environment.hdr`, licensed as described in `gltf/pontiac_gto_environment_LICENSE.txt`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF for clearcoat, transmission, IOR, and specular data.
- The scene contains 63 meshes and about 1.06 million triangles.
- The environment map is exported as an equirectangular HDR in glTF world orientation. glTF has no environment light, so load the provided HDR environment map separately.
- Spectral metals, glass behavior, and coated diffuse materials are approximations; exact mappings are in the conversion report.
- The reference render uses an exposure multiplier of 1.25 (+0.32 stops) instead of 1.0, so the car paint is closer to the Tungsten reference's brightness. Its hue still differs. The setting is recorded in the conversion report's `reference_render` section.
