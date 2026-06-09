# Outer Space Defense — Hybrid Idle-Shooter GDD

**Version:** v1.0 | **Date:** June 8, 2026 | **Author:** Jason
**Engine:** GameMaker Studio 2 (Primary) / Unity (Secondary) | **Series:** 2 of 3
**Platforms:** Android (Primary), PC (Secondary) | **Status:** Active — Internal Developer Reference

---

## Table of Contents

1. Game Overview
2. Core Design Pillars
3. Core Gameplay Loop
4. Idle Systems
5. Active Shooter Systems
6. Enemy Design
7. Progression & Upgrade Systems
8. UI/UX Design
9. Audio Design
10. Technical Specifications
11. Monetization (Future)
12. Development Milestones
13. Open Questions & Design Notes

---

## 1. Game Overview

### 1.1 High-Concept Pitch
> Outer Space Defense is a hybrid idle-shooter where you command an evolving space defense station that fights on its own but rewards every second you step in personally.

### 1.2 Genre & Target Audience

| Field | Detail |
|---|---|
| Genre (Primary) | Hybrid Idle Game |
| Genre (Secondary) | Real-Time Space Shooter |
| Tone | Sci-fi, strategic, satisfying |
| Audience | Idle fans who want more agency; shooter fans who want persistent progression |
| Age Rating Target | E10+ |

### 1.3 Session Length & Platform Strategy

| Mode | Duration | Notes |
|---|---|---|
| Active Session | 5-30 min | Manual combat, upgrades, boss runs |
| Idle Background | Infinite | Passive auto-fire, resource gen |
| Offline Gain Cap | 8 hours | Upgradable via Idle Efficiency Tree |

---

## 2. Core Design Pillars

| Pillar | Motto | Description |
|---|---|---|
| Dual-Mode Agency | Every player is rewarded | Idle and active play feel equally meaningful |
| Escalating Threat | The enemy never stops | Waves always pressure the player to engage |
| Tactile Polish | If it does not feel good, it is not done | Every action has satisfying feedback |
| Clear Progression | Always know what is next | Upgrade paths and unlock gates are visible |
| Depth Without Friction | Complexity is earned | New mechanics revealed gradually |

---

## 3. Core Gameplay Loop

### 3.1 Moment-to-Moment
Idle turrets auto-fire -> Player aims and fires -> Resources drop -> Player collects and deploys abilities -> Wave completes -> Upgrade prompt

### 3.2 Session Loop
Open game -> Collect offline gains -> Spend upgrades -> Run waves manually -> Boss wave -> Boss reward -> Save -> Return to idle

### 3.3 Long-Term Loop
Unlock weapon tiers -> Unlock turret tiers -> Clear 5 sectors -> Ascend (Prestige) -> Permanent multiplier -> Repeat at higher ceiling

### 3.4 Loop Flow Diagram

```
[Open Game]
  -> [Collect Offline Gains]
  -> [Wave Begins]
      -> Active: Player aims + fires + deploys -> 2x resource gen
      -> Idle:   Turrets auto-fire only        -> 1x resource gen
  -> [Enemy Dies] -> [Resource Drop]
  -> [Wave Complete] -> [Upgrade Menu]
  -> [Boss Wave] -> [Sector Reward]
  -> [Exit] -> [Idle Mode: Gains accumulate up to 8h cap]
```

---

## 4. Idle Systems

### 4.1 Auto-Turret Tiers

| Tier | Name | Dmg/Shot | Fire Rate | Range | Upgrade Cost | Special |
|---|---|---|---|---|---|---|
| 1 | Pulse Cannon | 10 | 1.5/sec | 300 | Base | Standard auto-fire |
| 2 | Arc Blaster | 25 | 1.2/sec | 350 | 500 Credits | Chains to 1 nearby enemy |
| 3 | Plasma Array | 60 | 0.8/sec | 400 | 2,500 Credits | AoE burst on hit |
| 4 | Void Lance | 150 | 0.5/sec | 500 | 12,000 Credits | Pierces 3 enemies |
| 5 | Nova Sentinel | 400 | 0.3/sec | 600 | 60,000 Credits | Shockwave on kill |

Max turrets on screen: **8 simultaneously**.

### 4.2 Passive Resource Generation

| Resource | Base Rate | Max Multiplier | Use |
|---|---|---|---|
| Credits | 10/sec | 50x | Primary upgrade currency |
| Energy Cores | 1/min | 20x | Tech research |
| Rare Alloys | 0.1/min | 10x | Station modules, Tier 4-5 |

### 4.3 Offline Progression
`Offline Gain = Base Rate x Efficiency Multiplier x min(Time_Away_in_hours, 8)`

- Efficiency Multiplier: starts 1.0; upgradable to 3.0
- Offline cap upgradable to 12h via Prestige perk Extended Watch
- Welcome Back screen animates total gains on return

### 4.4 Idle Efficiency Upgrade Tree
- **Branch A:** Offline Cap (8h -> 10h -> 12h)
- **Branch B:** Efficiency Multiplier (+0.5/node up to +2.0 bonus)
- **Branch C:** Auto-Collect Radius (increasing range)

---

## 5. Active Shooter Systems

### 5.1 Player Ship
- 3 loadout slots: Primary Weapon, Secondary Weapon, Special Ability
- HP: 500 base (upgradable to 2,000); Shield: 100 (regen 10/sec out of combat)
- Movement: ship auto-positions at screen bottom; player controls aim direction only

### 5.2 Primary Weapons

| Weapon | Damage | Fire Rate | Projectile | Unlock | Special |
|---|---|---|---|---|---|
| Laser Pulse | 30 | 3/sec | Hitscan | Default | None |

### 5.4 Special Abilities

| Ability | Effect | Cooldown | Unlock |
|---|---|---|---|
| Orbital Strike | Destroys all non-boss enemies | 60 sec | Wave 10 |
| Time Dilation | Slows enemies 50% for 5 sec | 45 sec | Wave 18 |
| Shield Overcharge | +1,000 HP temp shield | 50 sec | Wave 14 |
| Warp Burst | Teleports enemies back to spawn edge | 40 sec | Sector 2 |

### 5.5 Aiming System
- **Mobile:** tap to fire at position; drag to aim continuously
- **PC:** mouse = crosshair; left-click fire; right-click secondary
- **Auto-aim assist:** optional toggle - snaps to nearest enemy within 60px
- Auto-aim does NOT apply to boss weak points (manual required)

### 5.6 Active Combat Bonus
- **2x resource generation** on all passive sources while player fires
- Activates on first shot; deactivates 3 sec after last shot
- Visual: neon blue ring pulses around station when active

---

## 6. Enemy Design

### 6.1 Standard Enemies

| Name | Behavior | HP | Dmg | Credits | Energy | Special |
|---|---|---|---|---|---|---|
| Drone Scout | Rushes station | 80 | 15 | 5 | 0 | Fast movement |
| Swarm Cluster | Splits into 3 on death | 200 | 10 | 15 | 1 | Split mechanic |
| Void Cruiser | Slow; fires 3-spread projectile | 500 | 30 | 40 | 3 | Ranged |
| Pulsar Satellite | Orbits station; EMP pulse every 8 sec | 350 | 0 | 30 | 5 | Disables turrets 2 sec |
| Nebula Walker | Invisible for 3 sec intervals | 600 | 50 | 60 | 8 | Stealth |

### 6.2 Elite Variants (Wave 26+)
Each standard type has an elite (3x HP, 2x damage, 1.5x speed) with a unique elite ability.

### 6.3 Wave System

| Range | Tier | Notes |
|---|---|---|
| 1-10 | Tutorial | Guided; limited enemy types; reduced speed |
| 11-25 | Core | Full roster; scaling HP; elites from Wave 20 |
| 26-50 | Hard | Elite-only waves possible; modifier every 5 waves |
| 51+ | Infinite | Procedural: +2% speed, +3% HP, +5% reward per wave |

### 6.4 Boss Design

**Boss 1 - The Dreadnought (Sector 1)** | HP: 5,000
- Phase 1 (100%): Homing missile salvos of 3
- Phase 2 (60%): Frontal shield; flank required
- Phase 3 (25%): Charge attack + missile swarm
- Drop: Void Core (unlocks Tier 3 Turret)

**Boss 2 - The Hive Mother (Sector 2)** | HP: 12,000
- Phase 1: Spawns 6 Drone Scouts every 10 sec
- Phase 2 (70%): 2 Elite Swarm Clusters every 8 sec
- Phase 3 (35%): Self-destructs into 20 drones if not killed in 30 sec
- Drop: Hive Core (unlocks Drone Swarm)

**Boss 3 - Pulsar Prime (Sector 3)** | HP: 25,000
- Phase 1: 360-degree EMP pulse every 6 sec
- Phase 2 (65%): Splits into 2 Pulsar Satellites (12K HP each)
- Phase 3: Reforms at 6K HP; enraged; all abilities combined
- Drop: Pulsar Core (unlocks Ion Scatter)

**Boss 4 - The Void Leviathan (Sector 4)** | HP: 55,000
- Phase 1: 8-direction void bolt spread
- Phase 2 (50%): Submerges; attacks from perimeter 20 sec
- Phase 3 (25%): Reveals 200 HP weak point core
- Drop: Leviathan Scale (+10% permanent weapon damage)

**Boss 5 - The Omega Sentinel (Sector 5)** | HP: 120,000 (3 forms x 40,000)
- Form 1: Standard attacks + 2 Elite Cruisers every 15 sec
- Form 2: Time dilation field (70% projectile slow) + homing plasma orbs
- Form 3: All previous attacks + screen-wide annihilation beam (cancel with Orbital Strike)
- Drop: Omega Core (enables Ascension)

---

## 7. Progression & Upgrade Systems

| Currency | Rarity | Source | Use |
|---|---|---|---|
| Credits | Common | Enemy drops, passive gen | Turret/ship upgrades |
| Energy Cores | Uncommon | Elite drops, boss rewards | Tech research |
| Rare Alloys | Rare | Boss drops, passive gen | Station modules, Tier 4-5 |
| Void Shards | Prestige-only | Ascension reward | Ascension-tier upgrades |

**Prestige - Ascension:** Unlocked after defeating Omega Sentinel. Resets Credits/Cores/Alloys/levels. Carries over Void Shards, Ascension upgrades, weapon roster. Formula: `(wave / 10) x Ascension multiplier`. Multiplier starts 1x; +0.25x per Ascension.

---

## 8-10. UI, Audio & Technical

**Color Palette:** #0A0A1A (BG), #00BFFF (Neon Blue Accent), #FF6B35 (Enemy/Danger), #FFFFFF (UI Text)

**Adaptive Music:** Idle 70 BPM -> Combat Low 95 BPM -> Combat Mid 120 BPM -> Combat High 140 BPM -> Boss 150+ BPM

**Engine:** GMS2 (Android primary), Unity (PC secondary) | **FPS Target:** 60 FPS mid-range Android

**Save:** JSON auto-save every 60 sec; Google Play Games cloud save; last 3 states kept as backup

---

## 12. Development Milestones

| Milestone | Description | Target |
|---|---|---|
| Prototype | Core idle loop + turret auto-fire + wave spawner | July 15, 2026 |
| Alpha | Full 10 waves + player ship + 3 weapons + Dreadnought | September 1, 2026 |
| Beta | All 5 sectors + prestige + mobile HUD + cloud save | November 15, 2026 |
| Soft Launch | Select markets for live balance testing | January 10, 2027 |
| Global Launch | All platforms, monetization live | March 1, 2027 |

---

## 13. Open Questions

1. Should Ascension reset turret tiers?
2. Max turret count: 8? (performance vs. tactical depth)
3. PvP leaderboard? (requires backend)
4. Should player ship have movement (not just aim)?
5. Boss weak points: manual-only or auto-targetable?

---
*Outer Space Defense - Hybrid Idle-Shooter GDD v1.0 | Author: Jason | June 8, 2026 | Internal Use Only*
| Plasma Burst | 80 | 1.2/sec | Slow orb | Wave 5 | AoE on impact |
| Railgun | 300 | 0.4/sec | Piercing slug | Wave 15 | Pierces all in line |
| Ion Scatter | 20x5 | 1.5/sec | Spread | Wave 20 | Multi-target |
| Nova Cannon | 600 | 0.2/sec | Charged shell | Sector 2 | 1.5s charge-up |

### 5.3 Secondary Weapons

| Weapon | Effect | Cooldown | Unlock |
|---|---|---|---|
| Homing Missiles | 3 missiles, 100 dmg each, auto-track | 8 sec | Wave 3 |
| EMP Burst | Stuns all enemies 2 sec | 15 sec | Wave 8 |
| Shield Projector | +300 HP shield for 5 sec | 20 sec | Wave 12 |
| Drone Swarm | 4 drones, 20 dmg/sec each, 10 sec | 25 sec | Sector 2 |
