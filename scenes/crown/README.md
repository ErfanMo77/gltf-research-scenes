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
- The gems use their real indices: diamond 2.417 with `KHR_materials_dispersion` 0.362 (Abbe number 55), ruby and sapphire 1.768, zirkon 1.95. The PBRT scene uses larger values (diamond 3.3 to 3.5, ruby and sapphire 3.0).
- Gold has base color (1.0, 0.773, 0.307), the F0 of the [Physically Based database](https://physicallybased.info) (red 1.059 clamped to 1.0). The PBRT RGB eta and k give (0.923, 0.847, 0.386), which is the Fresnel reflectance at three RGB values only.
- Ruby and sapphire absorption uses `KHR_materials_volume`.
- The pearls are glossy (roughness 0.15, with a 0.15-roughness clearcoat on `pearl`) and use `KHR_materials_iridescence` (IOR 2.0, 420 nm) for the nacre shimmer. The base color and these values follow MaterialX's pearl material, which matches the [Physically Based database](https://physicallybased.info). The velvet uses `KHR_materials_sheen` instead of a clearcoat so it reads as fabric, and the zirkon stones use `KHR_materials_volume` so they refract as solid gems like the diamonds. These extension values are tuned against the PBRT reference, not converted from it.
- To compare with the PBRT reference in vk_gltf_renderer, use the Filmic tonemapper with auto-exposure off and exposure 1.0 (`--tmMethod 0 --tmAutoExposure 0 --tmExposure 1.0`). The default auto-exposure renders the scene about twice as bright as the reference.
- The PBRT scene attaches the ruby and sapphire media to the outside of the gem surface, so light is absorbed along the whole path after it leaves the stone. `KHR_materials_volume` only absorbs inside the mesh, so the `attenuationDistance` is 40x shorter (0.05 instead of 2.0) than the literal PBRT `sigma_a`. This matches the saturated look of the PBRT reference, but the PBRT absorption is not physical, so these values are a calibration to that look, not physical absorption coefficients. In PBRT the light reflections on the stones are also tinted; in glTF they stay white.
- The height maps are baked into the geometry, so there are no normal maps.
- The sapphire is in the scene twice, as in the PBRT source (nodes 776 and 783 have identical geometry, from `mesh_00776.ply` and `mesh_00783.ply`). Every ray crosses two coincident surfaces at the stone. It is left as is.
