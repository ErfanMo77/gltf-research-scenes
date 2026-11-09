# Crown

![Crown reference](gltf/crown.png)

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
- The pearls are glossy (roughness 0.15, with a 0.15-roughness clearcoat on `pearl`) and use `KHR_materials_iridescence` (IOR 2.0, 420 nm) for the nacre shimmer. The base color and these values follow MaterialX's pearl material, which matches the [Physically Based database](https://physicallybased.info). The velvet uses `KHR_materials_sheen` instead of a clearcoat so it reads as fabric, and the zirkon stones use `KHR_materials_volume` so they refract as solid gems like the diamonds. These extension values are tuned against the PBRT reference, not converted from it.
- To compare with the PBRT reference in vk_gltf_renderer, use the Filmic tonemapper with auto-exposure off and exposure 1.0 (`--tmMethod 0 --tmAutoExposure 0 --tmExposure 1.0`). The default auto-exposure renders the scene about twice as bright as the reference.
- The PBRT scene attaches the ruby and sapphire media to the outside of the gem surface, so light is absorbed along the whole path after it leaves the stone. `KHR_materials_volume` only absorbs inside the mesh, so the `attenuationDistance` is 40x shorter (0.05 instead of 2.0) than the literal PBRT `sigma_a`. This matches the saturated look of the PBRT reference.
- The sapphire has a dark blue `specularColorFactor` (0.075, 0.137, 0.2). The PBRT scene uses an IOR of 3.0, while a real sapphire is about 1.77, so the reflections of the lights on the stone are too bright. The tint turns these white streaks into dark blue sparkles like the photo of the real crown. It only affects reflections, not the absorbed color.
- The height maps are baked into the geometry, so there are no normal maps.
