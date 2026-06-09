# Outer Space Defense — Full GDD (Hybrid Idle-Shooter)

**Version:** v2.0 — Full GDD | **Date:** June 8, 2026 | **Author:** Jason
**Engine:** GameMaker Studio 2 (Primary) / Unity (Secondary) | **Series:** 2 of 3
**Platforms:** Android (Primary), PC (Secondary) | **Rating Target:** E10+ | **Status:** In Development

---

## Table of Contents

1. Document Header & Version Control
2. Game Overview
3. Design Pillars
4. Core Gameplay Loops
5. Idle Systems
6. Active Shooter Systems
7. Enemy Design
8. Progression & Upgrade Systems
9. UI/UX Design
10. Audio Design
11. Technical Specifications
12. Monetization
13. Development Milestones
14. Open Questions & Design Notes

---

## 1. Document Header

| Field | Value |
|---|---|
| Game Title | Outer Space Defense: Hybrid Idle-Shooter |
| Document Version | v2.0 Full GDD |
| Date | June 8, 2026 |
| Author | Jason |
| Engine | GameMaker Studio 2 (primary) / Unity (secondary) |
| Platform | Android (primary), PC (secondary) |
| Status | In Development |

---

## 2. Game Overview

### 2.1 High-Concept Pitch
> A hybrid idle-shooter where your space defense station runs autonomously but activates overdrive when you pick up the controls.

### 2.2 Genre
- Primary: Idle/Incremental
- Secondary: Real-Time Space Shooter
- Hybrid mechanics: passive automation + active input create synergistic power spikes

### 2.3 Core Fantasy
The player commands a deep-space orbital defense station. Turrets hold the line while offline, but active engagement triggers combat bonuses that multiply all systems.

### 2.4 Target Audience
- Primary: Mobile gamers 16-35 who enjoy idle games but want more agency
- Secondary: PC casual-to-mid-core players who enjoy arcade shooters
- Psychographic: Optimizer player type

### 2.5 Platform Targets

| Platform | Orientation | Resolution | Input |
|---|---|---|---|
| Android | Portrait | 1080x1920 | Touch / tap |
| PC | Landscape | 1920x1080 | Mouse + keyboard |

### 2.6 Session Length
- Idle background: Infinite
- Active session: 5-30 minutes
- Offline gain cap: 8 hours

---

## 3. Design Pillars

| Pillar | Motto | Description |
|---|---|---|
| Dual-Mode Agency | Every player is rewarded | Idle and active play feel equally rewarding |
| Escalating Threat | The enemy never stops | Enemy waves always pressure player to engage |
| Tactile Polish | If it doesn't feel good, it isn't finished | Every action has satisfying feedback |
| Clear Progression | Always know what you're building toward | Upgrade paths are always visible |
| Depth Without Friction | Complexity is earned, not imposed | New mechanics revealed gradually |

---

## 4. Core Gameplay Loops

### 4.1 Three-Tier Loop Architecture

**Moment-to-Moment:** Idle turrets auto-fire -> player aims and fires -> resources drop -> player collects -> abilities deployed -> wave completes -> upgrade prompt

**Session Loop:** Enter game -> check offline gains -> upgrade -> engage waves manually -> boss wave -> boss reward -> save -> idle

**Long-Term Loop:** Unlock weapon tiers -> unlock turret tiers -> clear 5 sectors -> Ascension -> permanent multipliers -> repeat at higher ceiling

### 4.2 Loop Flow Diagram

```
[Player Opens Game]
  -> [Check Offline Gains] -> [Collect Credits/Energy]
  -> [Wave Begins]
      -> Active: Player aims + fires + deploys -> 2x resource gen
      -> Idle:   Turrets auto-fire only        -> 1x resource gen
  -> [Enemy Dies] -> [Drop Resource/Power-up]
  -> [Wave Complete] -> [Upgrade Menu]
  -> [Next Wave or Boss Wave]
  -> [Boss Cleared] -> [Sector Reward] -> [Continue or Ascend]
  -> [Player Exits] -> [Idle mode: gains accumulate up to 8h cap]
```

---

## 5. Idle Systems

### 5.1 Auto-Turret Tiers

| Tier | Name | Dmg/Shot | Fire Rate | Range | Upgrade Cost | Special |
|---|---|---|---|---|---|---|
| 1 | Pulse Cannon | 10 | 1.5/sec | 300 | Base | Standard auto-fire |
| 2 | Arc Blaster | 25 | 1.2/sec | 350 | 500 Credits | Chains to 1 nearby enemy |
| 3 | Plasma Array | 60 | 0.8/sec | 400 | 2,500 Credits | AoE burst on hit |
| 4 | Void Lance | 150 | 0.5/sec | 500 | 12,000 Credits | Pierces 3 enemies |
| 5 | Nova Sentinel | 400 | 0.3/sec | 600 | 60,000 Credits | Shockwave on kill |

Max turrets on screen: **8 simultaneously**.

### 5.2 Passive Resource Generation

| Resource | Base Rate | Max Multiplier | Notes |
|---|---|---|---|
| Credits | 10/sec | 50x | Primary upgrade currency |
| Energy Cores | 1/min | 20x | Tech research currency |
| Rare Alloys | 0.1/min | 10x | Drop and passive |

---

## 6. Active Shooter Systems

### 6.1 Player Weapon Arsenal

#### Primary Weapons

| # | Weapon | Dmg | Fire Rate | Ammo | Special |
|---|---|---|---|---|---|
| 1 | Laser Blaster | 15 | 5/sec | Infinite | Standard hitscan |
| 2 | Plasma Cannon | 45 | 2/sec | 120 | AoE on impact |
| 3 | Railgun | 120 | 0.8/sec | 40 | Pierces all enemies in line |
| 4 | Void Beam | 80/sec | Continuous | 8 sec | DoT, disables shields |
| 5 | Nova Launcher | 200 | 0.5/sec | 25 | Splits into 5 bomblets |

#### Secondary Weapons (Cooldown-Based)

| # | Ability | Effect | Cooldown |
|---|---|---|---|
| 1 | EMP Pulse | Stuns all enemies 2 sec | 15 sec |
| 2 | Shield Burst | Reflects 50% incoming dmg | 20 sec |
| 3 | Singularity Mine | Pulls enemies to center, detonates | 25 sec |
| 4 | Overdrive | All turrets fire 3x speed 5 sec | 30 sec |

#### Special Abilities (Charged)

| # | Ability | Effect | Charge Cost |
|---|---|---|---|
| 1 | Station Nova | Massive screen-clear explosion | 100 charge |
| 2 | Time Dilation | Slow all enemies 50% for 8 sec | 75 charge |
| 3 | Turret Storm | Deploy 4 bonus turrets 10 sec | 60 charge |
| 4 | Void Rift | Gravity well that deals 500 dmg/sec | 80 charge |

### 6.2 Active Engagement Bonus

When the player is actively firing:
- **Resource Generation:** +100% (2x multiplier)
- **Turret Fire Rate:** +25% from targeting assist
- **Combo Meter:** Builds on consecutive hits; x2 -> x3 -> x4 -> x5 multiplier
- **Combo breaks:** on hit taken or 2-second gap in firing

### 6.3 Active vs Idle Comparison

| Metric | Idle Mode | Active Mode |
|---|---|---|
| Resource Gen | 1x base | 2x base |
| Turret Rate | 100% | 125% |
| Boss DPS | Turrets only | Turrets + player |
| Ability Access | None | Full |
| Combo Multiplier | None | Up to 5x |

---

## 7. Enemy Design

### 7.1 Standard Enemy Types

| # | Name | HP | Speed | Dmg | Behavior | Drops |
|---|---|---|---|---|---|---|
| 1 | Drone Scout | 50 | Fast | 5 | Linear rush | 10 Credits |
| 2 | Swarm Cluster | 20 x5 | Medium | 3 each | Splits on death | 5 x5 Credits |
| 3 | Heavy Marauder | 300 | Slow | 25 | Tanks fire, charges | 80 Credits |
| 4 | Stealth Viper | 100 | Fast | 15 | Cloaks every 5 sec | 40 Credits |
| 5 | Void Carrier | 400 | Very Slow | 0 | Spawns 3 Drones/sec | 150 Credits |

### 7.2 Elite Enemy Types

| Name | HP | Modifier | Special |
|---|---|---|---|
| Armored Drone | 200 | Armored | Takes 50% dmg from non-piercing |
| Shielded Marauder | 500 | Shielded | Immune until shield broken (200 HP shield) |
| Phase Viper | 250 | Phasing | Teleports 3 random positions |
| Turret Buster | 350 | Targeted | Focuses turrets, ignores player |

### 7.3 Boss Roster — Full Phase Breakdown

#### Boss 1 — The Dreadnought (Sector 1)
- **HP:** 5,000 | **Reward:** 1,000 Credits + Rare Alloy x3
- **Phase 1 (100-60% HP):** Fires homing missiles every 4 sec; deploys 2 Drones every 8 sec
- **Phase 2 (60-25% HP):** Activates frontal shield (blocks 70% dmg from front); begins strafe movement
- **Phase 3 (25-0% HP):** Charges station directly; drops shield; fires rapid scatter missiles
- **Weak Point:** Rear exhaust port — 2x damage

#### Boss 2 — The Hive Mother (Sector 2)
- **HP:** 12,000 | **Reward:** 3,000 Credits + Energy Core x5
- **Phase 1:** Spawns 3 Swarm Clusters every 6 sec
- **Phase 2 (below 50% HP):** Accelerates spawn rate to every 3 sec; gains Regeneration (+200 HP/sec)
- **Phase 3 (below 20% HP):** Self-destruct countdown (30 sec) — must be killed; spawns 10 Drones immediately
- **Weak Point:** Egg sac on underside — 3x damage

#### Boss 3 — Pulsar Prime (Sector 3)
- **HP:** 25,000 | **Reward:** 8,000 Credits + Tech Blueprint
- **Phase 1:** EMP pulses every 5 sec (disables turrets 2 sec)
- **Phase 2 (below 50% HP):** Splits into 2 cores (12,500 HP each) — must kill both within 10 sec or Pulsar Prime reforms at 30% HP
- **Phase 3:** Reunified — gains Overcharge mode; rapid-fire EMP barrage every 2 sec
- **Weak Point:** Central crystal core — 2.5x damage

#### Boss 4 — The Void Leviathan (Sector 4)
- **HP:** 55,000 | **Reward:** 20,000 Credits + Ascension Key Fragment
- **Phase 1:** Fires void bolts that create lingering damage zones
- **Phase 2 (below 60% HP):** Submerges — immune for 8 sec; surfaces at random position
- **Phase 3 (below 30% HP):** Exposes weak point core — takes 4x damage during window (5 sec window, 15 sec cooldown)
- **Phase 4 (below 10% HP):** Enrage — all attacks fire 2x; movement speed 2x

#### Boss 5 — The Omega Sentinel (Sector 5)
- **HP:** 120,000 | **Reward:** Ascension Unlock + 100,000 Credits
- **Form 1 (100-67% HP):** Orbital cannon barrage; summons Armored Drones; creates gravity well
- **Form 2 (67-33% HP):** Transforms — gains flight; fires void beam sweep (full screen); deploys Turret Busters
- **Form 3 (33-0% HP):** Time distortion field — player movement slowed 50%; attacks every 1 sec; kills grant +20% boss HP back (Drain)
- **On Defeat:** Ascension sequence triggers

---

## 8. Progression & Upgrade Systems

### 8.1 Station Module Upgrade Tree

| Module | Tier 1 | Tier 2 | Tier 3 | Cost Scale |
|---|---|---|---|---|
| Power Core | +20% all dmg | +40% all dmg | +100% all dmg | 500/2K/10K |
| Shield Grid | +500 HP | +1500 HP | Regen 5 HP/sec | 300/1.5K/8K |
| Targeting AI | +10% fire rate | +25% fire rate | Auto-aim assist | 400/1.8K/9K |
| Resource Collector | +15% drop rate | +35% drop rate | Magnet range x3 | 200/1K/5K |
| Charge Capacitor | -10% ability CD | -25% ability CD | +25% charge gen | 600/2.5K/12K |

### 8.2 Tech Research Tree (Energy Core Currency)

- **Weapons Branch:** Unlock Plasma Cannon (15 Cores) -> Railgun (40 Cores) -> Void Beam (80 Cores) -> Nova Launcher (150 Cores)
- **Turret Branch:** Unlock Arc Blaster (10 Cores) -> Plasma Array (30 Cores) -> Void Lance (70 Cores) -> Nova Sentinel (140 Cores)
- **Idle Branch:** Offline Cap +2h (20 Cores) -> Efficiency x1.5 (50 Cores) -> Auto-Collect (100 Cores)
- **Station Branch:** Shield Grid T3 prerequisite (25 Cores) -> Emergency Warp (60 Cores) -> Dual Core Mode (120 Cores)

### 8.3 Ascension / Prestige System

**Trigger:** Defeat Boss 5 — The Omega Sentinel.

**What resets on Ascension:**
- Credits and Energy Cores
- All Station Module tiers
- Tech Research progress
- Wave/Sector progress

**What persists:**
- Ascension Points (AP) — earned each run based on sectors cleared
- Cosmetic unlocks
- Ascension Perks purchased with AP

**Ascension Perk Tree (sample):**

| Perk | AP Cost | Effect |
|---|---|---|
| Veteran Start | 5 AP | Begin each run with 500 Credits |
| Extended Watch | 8 AP | Offline cap 8h -> 12h |
| Turret Loyalty | 10 AP | All turrets +15% permanent dmg |
| Dual Assault | 15 AP | Fire 2 weapons simultaneously |
| Void Touched | 20 AP | All abilities cost 20% less charge |
| Legacy Arsenal | 25 AP | Start with Railgun unlocked |

**Ascension run count** displayed on main screen as prestige badge.

---

## 9. UI/UX Design

### 9.1 Color Palette

| Role | Hex | Usage |
|---|---|---|
| Background | #0A0A1A | Deep space black — all screens |
| Accent Blue | #00BFFF | UI highlights, selected states |
| Plasma Orange | #FF6B35 | Enemies, warnings, dangers |
| Text Primary | #FFFFFF | All labels and values |
| Panel BG | #1A1A3E | HUD panels, cards, overlays |

### 9.2 HUD Layout (Portrait)

```
[Station HP Bar]    [Wave Timer]    [Boss HP Bar]
[Turret Slots x8 ]
           [GAME AREA]
[Credits]  [Energy] [Alloys]   [Active Bonus]
[Weapon Select] [Secondary] [Special Charge]
```

### 9.3 Key Screens

- **Main Menu:** Station art, Play / Research / Ascend / Shop buttons
- **Wave Screen:** HUD overlay + game area; pause button top-right
- **Upgrade Screen:** Tabbed: Turrets / Weapons / Statio

---

## 10. Audio Design

### 10.1 Adaptive Music State Machine

| State | Trigger | Track Style | Transition |
|---|---|---|---|
| Idle Ambient | No enemies in wave | Slow synth pad, 70 BPM | Crossfade 3 sec |
| Combat Low | Wave active, <25 enemies | Mid-tempo electronic, 95 BPM | Crossfade 1.5 sec |
| Combat High | >25 enemies OR elite present | Intense industrial, 130 BPM | Hard cut |
| Boss Battle | Boss wave active | Cinematic orchestral + synth | Hard cut in |
| Victory | Wave clear / Boss defeated | Triumphant stinger + ambient | Stinger + fade |
| Ascension | Omega Sentinel defeated | Epic swell, full orchestra | 10-sec ceremony |

### 10.2 SFX Categories

| Category | Examples |
|---|---|
| Weapon Fire | Laser zap, plasma thud, railgun crack, void hum |
| Turret | Pulse fire, arc crackle, plasma array burst |
| Enemy | Drone buzz, swarm scatter, marauder roar, void carrier horn |
| Boss | Phase transition swell, boss death explosion |
| UI | Button tap, upgrade ping, wave start countdown, credit earn |
| Ambient | Station hum, space wind, distant explosions |

### 10.3 Haptic Feedback Map (Mobile)

| Event | Haptic Pattern |
|---|---|
| Enemy death (standard) | Light tap |
| Elite enemy death | Medium pulse |
| Boss phase transition | Double medium pulse |
| Boss defeat | Long rumble (500ms) |
| Player hit taken | Short sharp vibration |
| Ascension trigger | Escalating rumble pattern |
| Upgrade purchased | Light tick |
| Special ability activated | Medium burst |

---

## 11. Technical Specifications

### 11.1 Performance Targets

| Platform | Resolution | Target FPS | Max Entities | Memory Budget |
|---|---|---|---|---|
| Android (primary) | 1080x1920 portrait | 60 FPS | 200 | 512 MB |
| iOS | 1170x2532 portrait | 60 FPS | 200 | 512 MB |
| PC (secondary) | 1920x1080 landscape | 120 FPS | 500 | 2 GB |

### 11.2 Engine Configuration

- **Primary Engine:** GameMaker Studio 2 (Android/iOS builds)
- **Secondary Engine:** Unity 6 (PC/Steam build, future console ports)
- **Physics:** Custom lightweight 2D physics (no built-in engine)
- **Rendering:** Sprite batching; max 4 draw calls per frame on mobile
- **Audio Engine:** FMOD Studio (adaptive music state machine)

### 11.3 Save System Architecture

| Layer | Data Stored | Storage Method |
|---|---|---|
| Local Save | All game state, upgrades, progress | Encrypted JSON (AES-128) |
| Cloud Save | Snapshot sync every wave clear | Google Play / iCloud / Steam Cloud |
| Backup Export | Manual player export | Base64 encoded save string |
| Anti-Cheat | Server-side wave validation | Checksum hash per session |

**Save Events:**
- Auto-save: every wave completion
- Auto-save: every upgrade purchase
- Auto-save: on app background / close

### 11.4 Data Export Layer

Players can export/import save data as a text string for:
- Device migration
- Backup before device wipe
- Community sharing (leaderboard screenshots validated by hash)

### 11.5 Memory Budget Breakdown (Mobile)

| Asset Type | Budget |
|---|---|
| Sprite Sheets | 128 MB |
| Audio (compressed) | 64 MB |
| UI Assets | 32 MB |
| Code + Logic | 48 MB |
| Particles + FX | 32 MB |
| Save Data Buffer | 8 MB |
| System Reserve | 200 MB |

---

## 12. Monetization Strategy

### 12.1 Core Principles

- **Free to Play** — all content accessible without payment
- **Cosmetic Only** — zero gameplay advantage purchasable
- **No Pay-to-Win** — resources, upgrades, abilities NOT purchasable
- **No Energy Gates** — play as long as desired
- **Optional Ads** — rewarded ads available but never mandatory

### 12.2 Cosmetic Shop Categories

| Category | Examples | Price Range |
|---|---|---|
| Station Skins | Neon Chrome, Void Dark, Retro Pixel, Galaxy Rose | $1.99 - $4.99 |
| Turret Skins | Crystal Pulse, Flame Arc, Shadow Void, Gold Nova | $0.99 - $2.99 |
| Projectile Trails | Rainbow, Ice, Fire, Shadow, Void | $0.99 - $1.99 |
| UI Themes | Dark Mode, Neon Synthwave, Military Green | $1.99 - $3.99 |
| Boss Kill Banners | Animated victory art per boss defeated | $0.99 each |
| Ascension Badges | Prestige level display icons (1-10) | Free earn + $1.99 premium |

### 12.3 Monetization Events

- **Battle Pass (optional):** Seasonal cosmetic track, 60 days, $4.99 — cosmetics only
- **Starter Pack (one-time):** 3 station skins + 2 turret skins at 60% discount on first launch
- **Rewarded Ads:** Double offline rewards (once per 4h); +200 Credits (once per session) — fully optional

### 12.4 Revenue Projections (Targets)

| Month | MAU Target | Conversion Target | ARPU | Monthly Revenue Target |
|---|---|---|---|---|
| Launch (M1) | 5,000 | 3% | $3.50 | $525 |
| M3 | 15,000 | 4% | $4.00 | $2,400 |
| M6 | 40,000 | 5% | $4.50 | $9,000 |
| M12 | 100,000 | 6% | $5.00 | $30,000 |

---

## 13. Development Milestones

### Roadmap Overview

| Phase | Duration | Target Date | Deliverables |
|---|---|---|---|
| Pre-Production | 4 weeks | Jul 2026 | GDD finalized, art style locked, prototype loop |
| Alpha | 8 weeks | Sep 2026 | Core loop playable, 3 enemy types, 2 bosses, no UI polish |
| Beta | 8 weeks | Nov 2026 | All 5 sectors, all bosses, progression complete, basic shop |
| Soft Launch | 4 weeks | Dec 2026 | Limited regional release (AU/CA), live data, bug fixes |
| Global Launch | — | Jan 2027 | Full iOS + Android release, marketing push |
| Post-Launch v1.1 | 6 weeks | Mar 2027 | PC/Steam build, Season 1 Battle Pass, balance patch |

### Key Milestones Detail

**M1 — Prototype (Jul 2026)**
- Auto-turret idle loop functional
- Player weapon firing functional
- 10-wave test sector with Drone + Marauder
- Basic resource accumulation working

**M2 — Alpha (Sep 2026)**
- 3 sectors, 3 bosses (The Dreadnought, Hive Mother, Pulsar Prime)
- Station Module upgrade tree (Tier 1-3)
- Tech Research tree (Weapons + Turret branches)
- UI: HUD + basic menus (no polish)
- Android build testable on device

**M3 — Beta (Nov 2026)**
- All 5 sectors complete
- All 5 bosses including The Omega Sentinel
- Ascension / Prestige system
- Cosmetic shop (5 station skins, 3 turret skins)
- Full audio with adaptive music
- Accessibility options implemented
- Leaderboard (wave score)

**M4 — Soft Launch (Dec 2026)**
- Regional release: Australia, Canada
- Analytics events firing (Firebase)
- Rewarded ads integrated
- Balance tuning from live data
- Crash rate target: <0.5%

**M5 — Global Launch (Jan 2027)**
- Full App Store + Play Store release
- Press kit + gameplay trailer
- Discord community launch
- Live ops team monitoring

**M6 — Post-Launch v1.1 (Mar 2027)**
- PC/Steam build released
- Season 1 Battle Pass live
- New enemy type: Void Phantom (cloaks + reflects)
- Balance patch based on 30-day data
- Cloud save cross-platform sync

---

## 14. Open Design Questions

1. **Multiplayer Co-op:** Is a 2-player co-op mode worth the added complexity? If yes, does Player 2 control a second station or assist the primary? Target for v1.2 if greenlit.

2. **Endless Mode:** Should an Endless mode exist beyond Sector 5 post-Ascension, or is Ascension itself the repeating endgame loop? Leaning toward Endless as optional unlockable.

3. **Daily Challenges:** Fixed-seed daily challenge waves with global leaderboard? Low dev cost, high engagement — recommend implementing in v1.1.

4. **PC Controls:** Mouse-aim for active shooting on PC? Keyboard shortcuts for ability hotkeys? Needs UX testing — do not block mobile launch.

5. **Platform Parity:** Should Android and iOS share identical save data via cross-save? Yes — requires Google Play Games Services + Game Center integration. Plan for v1.1.

6. **Boss Rush Mode:** Unlockable mode: fight all 5 bosses consecutively with limited heals. High replayability — recommend for v1.2.

7. **Balance — Active vs Idle Gap:** The 2x active bonus may not be compelling enough to pull idle players into active play. Playtesting required in Alpha. May need tuning to 2.5x or 3x.

8. **Monetization Cap:** Is the Battle Pass at $4.99 correctly positioned? Competitive analysis suggests $4.99-$9.99 is the sweet spot for mobile F2P strategy games. Recommend A/B testing at launch.

---

## Appendix A — Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 0.1 | 2026-03-01 | Jason (Desertsmogtech) | Initial draft — core concept |
| 1.0 | 2026-04-15 | Jason (Desertsmogtech) | First complete GDD |
| 2.0 | 2026-06-09 | Jason (Desertsmogtech) | Full production-grade expansion — all 14 sections |

---

*Outer Space Defense — Hybrid Idle-Shooter | GDD v2.0 | © 2026 Desertsmogtech. All rights reserved.*n / Research
- **Boss Warning:** Full-screen cinematic intro card (2 sec) before boss appears
- **Ascension Screen:** Cinematic sequence + AP earned display + Perk selection
- **Offline Return:** "Welcome Back" card showing total gains with tap-to-collect

### 9.4 Accessibility

- Colorblind mode: alternate palette substituting orange with yellow-green
- Text scaling: 80% / 100% / 120%
- Tap area minimum: 44x44 dp on mobile
- Haptic feedback: enemy death, boss phase transition, Ascension trigger

### 5.3 Offline Progression Formula
`Offline Gain = Base Rate x Efficiency Multiplier x min(Time_Away_in_hours, 8)`

- Efficiency Multiplier: starts 1.0; upgradable to 3.0 via Idle Efficiency Tree
- Offline cap (8h) upgradable to 12h via Prestige perk "Extended Watch"
- "Welcome Back" screen shows total gains on return with tap-to-collect

### 5.4 Idle Efficiency Upgrade Tree
- **Branch A:** Offline Cap Extension (8h -> 10h -> 12h)
- **Branch B:** Efficiency Multiplier (+0.5/node up to +2.0 bonus)
- **Branch C:** Auto-Collect Radius (increasing range per node)
Each branch has 3 nodes; costs escalate x3 per node.
