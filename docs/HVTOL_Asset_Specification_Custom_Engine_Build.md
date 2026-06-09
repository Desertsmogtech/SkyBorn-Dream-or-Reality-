> ** NDA NOTICE  SOLO TECH DESIGN STUDIO**
> This technical specification is released for contributor and contractor reference under the Solo Tech Design Studio Non-Disclosure Agreement. Proprietary engine integration details are marked `[OPERATOR PRIVATE  NDA]`.

---

# HVTOL Asset Specification  Custom Engine Build
**High-Velocity Takeoff and Landing | AAA Tactical Aircraft**
**Author:** Jason  Solo Tech Design Studio
**Classification:** Contributor-Ready | Contractor Reference

---

# 1.0 Overview & Scope

## 1.1 Asset Definition
HVTOL  High-Velocity Takeoff and Landing  is a hybrid aerospace vehicle combining vertical lift capability with high-speed forward thrust. The asset represents a militarized, next-generation tactical aircraft designed for rapid deployment, close air support, and high-altitude intercept roles.

## 1.2 Asset Purpose
- Real-time rendering within the custom game engine
- Cinematic sequences (in-engine and pre-rendered)
- Gameplay integration as a player-controllable and AI-driven vehicle

## 1.3 Target Platforms
`[OPERATOR PRIVATE  NDA]`

## 1.4 Quality & Delivery
- Quality Tier: AAA-grade fidelity with performance-optimized variants per platform
- Primary Delivery Format: FBX
- Secondary Delivery Format: USD
- Engine-Native Format: TBD (confirmed during integration phase)

---

# 2.0 3D Model Package

## 2.1 Exterior Shell
- Hero mesh (full aerodynamic body)
- Modular panel system (removable/swappable hull segments)
- Landing gear assembly (front tricycle + rear dual gear)
- Engine nacelles (left/right, articulated for thrust vectoring)
- Weapon hardpoints (underwing and bay-mounted, optional)

## 2.2 Interior Cockpit
- Pilot seat with harness geometry
- Instrument panel (multi-function displays, analog backup gauges)
- HUD projection surface (world-space render target)
- Canopy frame (interior ribbing, seal gasket detail)

## 2.3 Polygon Budgets
`[OPERATOR PRIVATE  NDA]`

## 2.4 Topology Requirements
- Topology: Quad-dominant; triangles permitted only where necessary
- Edge Flow: Clean edge loops at all deformation zones
- Normals: Smooth shading with hard edges at material boundaries only

## 2.5 UV Layout
- Non-overlapping UVs required for all bake targets
- UV density target: 10.24 px/cm at 4K resolution
- Minimal UV seam placement on visible surfaces

## 2.6 Modular Component List
`[OPERATOR PRIVATE  NDA]`

---

# 3.0 Rigging & Skeleton

## 3.1 Bone Naming Convention
- Format: {region}_{descriptor}_{side} (e.g., wing_flap_L)
- All lowercase snake_case
- Side suffixes: _L, _R, _C

## 3.2 Joint Limits & Constraints
`[OPERATOR PRIVATE  NDA]`

## 3.3 IK & Physics Bones
- IK Targets: Landing gear compression uses two-bone IK chains per strut
- Physics Bones: Antenna mast, cable bundles, panel edges  spring-damper constraints

---

# 4.0 Textures & Materials

## 4.1 Workflow
PBR Metallic-Roughness pipeline. No Specular-Glossiness maps.

## 4.2 Texture Set Per Component
`[OPERATOR PRIVATE  NDA]`

## 4.3 Resolution Targets
`[OPERATOR PRIVATE  NDA]`

## 4.4 Decal System
Modular decal atlas for runtime application. Single 4096x4096 atlas with pre-multiplied alpha.
- Unit insignia and squadron markings
- Airframe serial numbers and manufacturing stamps
- Warning labels (intake hazard, ejection seat, no step)
- Damage overlays (scorch marks, bullet impacts, panel buckling)

## 4.5 Damage States
`[OPERATOR PRIVATE  NDA]`

---

# 5.0 Animation Set

## 5.1 Blend Tree & State Machine
- Base Layer: Idle_Ground  Startup  VTOL_Liftoff  Cruise_Flight  Landing_Approach  Touchdown  Shutdown
- Combat Layer (Additive): Bank_L, Bank_R, Pitch_Up, Pitch_Down
- Damage Layer (Additive): Damage_Hit_Light, Damage_Hit_Heavy
- Environmental Layer (Additive): Turbulence noise (procedural), wind shear reaction

## 5.2 Required Animations
`[OPERATOR PRIVATE  NDA]`

---

# 6.0 UI & HUD Assets

## 6.1 HUD Style Specification
- Aesthetic: Vector-line rendering, monochrome base with accent color highlights
- Primary Accent Color: Chromed Electric Neon Blue (#00D4FF)
- Warning Color: #FF3333 (critical), #FFAA00 (caution)
- Resolution: All UI elements at 2x target resolution for downsampling

## 6.2 Font Specification
- HUD Font: Monospaced, military/aerospace style (custom DIN-condensed mono variant)
- Delivery: SDF font atlas for resolution-independent rendering

## 6.3 HUD Elements
`[OPERATOR PRIVATE  NDA]`

---

# 7.0 Cinematic Assets

## 7.1 Cinematic Mesh
- Cinematic LOD0: Up to 150,000 tris
- Topology: Motion-blur compatible
- Materials: Depth-of-field friendly

## 7.2 Pre-Lit Beauty Renders
Deliver at 4K (3840x2160), PNG format:
- 3/4 front view (hero angle)
- Profile (left side)
- Top-down orthographic
- Cockpit interior (pilot POV)

---

# 8.0 Audio Suite

## 8.1 Audio Format & Delivery
- Source: WAV, 48 kHz, 24-bit
- Runtime: OGG Vorbis (quality 6 minimum); WAV for one-shots under 500ms

## 8.2 RTPC Hooks
`[OPERATOR PRIVATE  NDA]`

---

# 9.0 Technical Integration Package

## 9.1 File Naming Convention
```
HVTOL_{Component}_{Variant}_{LOD}.{ext}
```
Examples:
- HVTOL_Fuselage_Default_LOD0.fbx
- HVTOL_Wing_L_Default_LOD2.fbx
- HVTOL_Fuselage_Default_BC.png
- HVTOL_Cockpit_Default_ORM.png

## 9.2 Collision Meshes
- Physics Collision: Simplified convex hull, max 32 convex shapes per vehicle
- Projectile Raycast: Separate slightly inflated mesh for hit detection

## 9.3 Metadata & Tagging
- AssetType: Vehicle
- VehicleClass: HVTOL
- LODLevel: [0-3]
- DamageState: [Clean|LightDamage|HeavyDamage|Destroyed]
- ContentTier: AAA

## 9.4 Performance Budget
`[OPERATOR PRIVATE  NDA]`

---

# 10.0 Optional Expansions

## 10.1 Weapon Loadout Swaps
- Missile Rack: Underwing pylon with 4x guided missile geometry
- Gatling Pod: Chin-mounted rotary cannon with spinning barrel rig
- EW Antenna: Electronic warfare pod
- Cargo Pod: Ventral cargo container for transport variant

## 10.2 Destruction System
- Pre-Fractured Meshes: Voronoi fracture (8-16 fragments per major panel)
- Fragment Physics: Convex collision, mass, and initial impulse vector
- Trigger Points: Engine pods, fuel tank (center fuselage), cockpit

## 10.3 Weathering & Aging System
- Procedural Dirt: World-space gradient mask
- Rain Streaks: Vertex-color-driven streak mask
- Panel Wear: Edge-wear mask driven by curvature map

---

# 11.0 Appendix

## 11.1 Sign-Off & Approval

Lead Artist: ____________________________  Date: __________

Technical Director: ____________________________  Date: __________

Project Lead: ____________________________  Date: __________

---

*HVTOL Asset Specification v1.0  Solo Tech Design Studio*
*Classification: Contributor-Ready | Contractor Reference*
