# Crown

![Crown PBRT reference](source/crown.png)

The Austrian Imperial Crown converted from PBRT v4 to glTF. It is useful for checking gold conductors, refractive and dispersive gemstones, absorbing ruby and sapphire media, texture-masked material mixes, fine height-map detail, and emissive mesh lighting.

## Source

- Collection: [mmp/pbrt-v4-scenes](https://github.com/mmp/pbrt-v4-scenes)
- Original model: Austrian Imperial Crown
- Original author: [Martin Lubich](http://www.loramel.net/)
- License: CC-BY-3.0; see `source/LICENSE.txt`
- Full-resolution PBRT references: `source/crown.png`, `source/crown.exr`

## Outputs

- Core glTF: `gltf/crown_core.gltf`
- Extended glTF: `gltf/crown_extended.gltf`
- Conversion report: `gltf/conversion.yaml`

## Notes

- Use the extended glTF. It adds the clearcoat, transmission, IOR, volume, and dispersion data that the gems and gold rely on.
- Render with a high maximum bounce count. Light passes through many diamond facets before it leaves, so the diamonds turn dark with too few bounces. The PBRT reference uses a maximum depth of 100.
- The diamonds and small rubies use wavelength-dependent IOR in PBRT. The glTF approximates it with an IOR of 3.39 and `KHR_materials_dispersion`.
- Ruby and sapphire absorption uses `KHR_materials_volume`.
- The height maps are baked into the geometry, so there are no normal maps.
