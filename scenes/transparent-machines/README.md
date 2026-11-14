# Transparent Machines

![Transparent Machines reference](gltf/transparent-machines.png)

**Set the path tracer to at least 64 max bounces**, and the same for separate
transmission or transparency limits. The overlapping glass needs long paths;
PBRT uses 256.

Five static frames from Beeple's *Transparent Machines* short film, converted
from PBRT v4. Each frame is a glTF scene with its own camera, and the asset
opens on frame 812. Render at **16:7**, the PBRT framing.

| Scene and camera | PBRT frame | Placed triangles | Vertical FOV | Sky HDR |
| --- | --- | ---: | ---: | --- |
| **0** | **812** | 3,635,494 | 15° | `transparent_machines_environment.hdr` |
| 1 | 542 | 1,313,664 | 12° | `transparent_machines_environment_frame542.hdr` |
| 2 | 675 | 1,583,772 | 4.509713° | `transparent_machines_environment_frame542.hdr` |
| 3 | 888 | 4,022,418 | 8° | `transparent_machines_environment.hdr` |
| 4 | 1266 | 6,218,468 | 8° | `transparent_machines_environment.hdr` |

## Lighting

- **Sky**, at intensity **6**: a procedural cyan sky with a high sun, inspired
  by the scene's original `sky.exr`, whose redistribution terms could not be
  verified. It has the original's mean luminance, so 6 is the PBRT light scale.
  Each frame's geometry and sky are rotated so that its camera is upright,
  which needs two sky HDRs.
- **Prism studio**, at intensity **1**, an alternative for every frame:
  [`transparent_machines_environment_prism.hdr`](gltf/transparent_machines_environment_prism.hdr).
  Narrow strips and bright spots in a dark studio outline the glass and bring
  out its dispersion. It is aligned to the camera, which all frames share, and
  tuned for an exposure of −0.75 EV with Khronos PBR Neutral.

Both maps are procedurally generated with scripts and released under CC0. See
the [sky license](source/sky_LICENSE.txt) and the
[prism license](gltf/transparent_machines_environment_prism_LICENSE.txt).

## Reference renders

Blender Cycles with the sky, at 1920 × 840, 16,384 samples per pixel, and 256
bounces. The `reference_render` section of the
[conversion report](gltf/conversion.yaml) records the settings for each frame.
The original PBRT renders of frames 542, 675, 812, and 888, lit by the original
sky, are in `source/` as EXR and PNG.

### frame812

![frame812 reference render](gltf/transparent-machines.png)

### frame542

![frame542 reference render](gltf/transparent-machines_frame542.png)

### frame675

![frame675 reference render](gltf/transparent-machines_frame675.png)

### frame888

![frame888 reference render](gltf/transparent-machines_frame888.png)

### frame1266

![frame1266 reference render](gltf/transparent-machines_frame1266.png)

## Conversion

- Both variants require `EXT_mesh_gpu_instancing` and share one 62.1 MB
  geometry buffer across the five frames.
- The extended variant uses smooth BK7 glass at IOR **1.516803**. Closed shells
  add `KHR_materials_volume` and dispersion **0.312557**. The core variant uses
  an alpha blend.
- About a third of the glass parts are open surfaces, such as uncapped tubes
  and the claw at the right of frame 812. They use the double-sided material
  `dielectric_00` without a volume, which glTF renders as thin glass, so they
  look fainter than in PBRT, which refracts at every surface.
- Six closed shells per frame face inward in the source. The converter turns
  them outward, so they render as solid glass.
- With the same sky, the Cycles render of frame 812 is within 2% of PBRT's mean
  luminance.

## Source and attribution

Models by Mike Winkelmann (Beeple), under his published
[project terms](source/LICENSE.txt). [Provenance](source/provenance.yaml) names
the exact PBRT checkout, the original sky, and the PBRT renders.
[PBRT scene documentation](https://github.com/mmp/pbrt-v4-scenes#transparent-machines)
