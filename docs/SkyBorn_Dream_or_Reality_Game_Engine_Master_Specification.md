> ** NDA NOTICE  SOLO TECH DESIGN STUDIO**
> This specification is released for contributor and contractor reference. Sections marked `[OPERATOR PRIVATE  NDA]` contain classified mission content, proprietary engine details, or operator-only information withheld from this public release.

---

# SkyBorn  Dream or Reality
## Game Engine Master Specification  Unified Build
**Studio:** Solo Tech Design Studio | **Version:** 2.0 | **Date:** April 2026
**Classification:** Internal / Contributor Use

---

## Part I: Design Vision & Game Identity

### 1.1 Game Title & Branding
**Title:** SkyBorn  Dream or Reality
**Tagline Purpose:** The subtitle questions whether these advanced HVTOL craft exist in the real world or are the engineered dream of next-generation aerospace.

### 1.2 Design Philosophy
**Genre:** Hybrid helicopter-jet VTOL combat simulation.
**Accent Color:** Chromed Electric Neon Blue (#00CFFF)

**Visual Identity Pillars:**
- Dark Metallic Stealth: Low-reflectivity dark composites
- Angular Geometry: Faceted, hard-edged surfaces
- Neon Accent System: #00CFFF applied to engine glow, HUD, UI borders
- Militarized Precision: Every craft is a weapon platform

### 1.3 Core Gameplay Loop
Hangar  Mission Briefing  Flight (quad-mode)  Post-Mission Debrief  Hangar

**Progression Mechanics:**
- Manage a fleet of HVTOL craft in the Hangar
- Customize weapon loadouts, paint schemes, and decal configurations
- Deploy on missions across multiple operation theaters
- Earn credits and parts from mission performance
- Unlock new craft via the Certification Ladder

### 1.4 Vehicle Design Reference (Rev-B 12-ft Spec)
`[OPERATOR PRIVATE  NDA]` *Detailed dimensional tables available to authorized contributors.*

### 1.5 Quad-Mode Flight System

| Mode | Control Law |
|---|---|
| VTOL Hover | Differential fan thrust (roll/pitch), collective RPM (altitude) |
| Transition | Blended authority  fans + aerodynamic surfaces |
| Forward Cruise | Conventional aerodynamic control surfaces, afterburner throttle |
| Combat | Thrust vectoring, dynamic fan re-engagement, 9G structural limit |

### 1.6 Certification Ladder & Progression
`[OPERATOR PRIVATE  NDA]`

### 1.7 Mission Structure & Worldbuilding
**Setting:** Near-future military aerospace. Multiple theaters  desert, arctic, urban, maritime, mountainous.

### 1.8 Top Secret Edition  Classified Missions
`[OPERATOR PRIVATE  NDA]`

### 1.9 Target Platforms
`[OPERATOR PRIVATE  NDA]`

---

## Part II: 3D Model Package

### 2.1 Exterior Shell
- Hero Mesh: Full aerodynamic body shell
- Modular Panel System: Removable/swappable hull segments
- Landing Gear Assembly: Front tricycle + dual rear main gear, retraction animation
- Engine Nacelles: Left/right wing-mounted, 8-blade internal fans
- Weapon Hardpoints: 4 underwing pylons + 1 internal weapon bay

### 2.2 Interior Cockpit
- Pilot Seat: Ejection seat with harness geometry
- Instrument Panel: 3 MFDs, analog backup gauges, 12 animated toggle switches
- HUD Projection Surface: Transparent combiner glass, world-space render target
- Canopy Frame: 4 longitudinal ribs + 2 transverse frames

### 2.3 Polygon Budgets
`[OPERATOR PRIVATE  NDA]`

### 2.4 Topology Requirements
- Quad-dominant; triangles permitted only in non-deforming areas
- Clean edge loops at all deformation zones
- No n-gons, no isolated vertices, no flipped normals
- Symmetry maintained on X-axis

### 2.5 UV Layout
- Non-overlapping UVs for all bake targets
- UV Density: 10.24 px/cm at 4096x4096
- UV Channels: 0 = unique unwrap, 1 = tiled detail, 2 = lightmap

### 2.6 Modular Component List
`[OPERATOR PRIVATE  NDA]`

---

## Part III: Rigging & Skeleton

### 3.1 Bone Naming Convention
**Format:** `{region}_{descriptor}_{side}`  all lowercase snake_case
**Physics prefix:** `phys_` | **IK targets prefix:** `ik_`

### 3.2 Joint Limits & Constraints
`[OPERATOR PRIVATE  NDA]`

### 3.3 IK & Physics Bones
- Landing Gear IK: 2-bone chain per leg, spring 2,500 N/m, damping 800 Ns/m
- Physics Bones: Antenna tip, cable runs (4-bone chains), loose panel edges

---

## Part IV: Textures & Materials

### 4.1 PBR Workflow
PBR Metallic-Roughness (glTF 2.0 / Unreal / Unity standard).

### 4.2 Resolution Targets
`[OPERATOR PRIVATE  NDA]`

### 4.3 Decal System
- Atlas: 4096x4096, pre-multiplied alpha
- Types: Unit insignia, tail numbers, warning labels, maintenance stencils
- Damage Overlays: Bullet holes, scorch marks, paint scratches

### 4.4 Damage States
`[OPERATOR PRIVATE  NDA]`

---

## Part V: Animation System

### 5.1 Blend Tree & State Machine
- Base Layer: Flight state machine
- Combat Layer (Additive): Bank/pitch inputs blended by input magnitude
- Damage Layer (Additive): Hit reactions as triggered one-shots
- Environmental Layer (Additive): Turbulence and wind shear (weather RTPC-driven)

### 5.2 Required Animations
`[OPERATOR PRIVATE  NDA]`

---

## Part VI: Cockpit UI & HUD

### 6.1 HUD Style
- Rendering: Vector-line, 1-2px anti-aliased
- Base Palette: Monochrome white/gray for primary readouts
- Accent: #00D4FF (Chromed Electric Neon Blue)
- Warning Red: #FF3333 | Caution Amber: #FFAA00

### 6.2 Font Specificat
