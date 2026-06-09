# Outer Space Defense — Hybrid Idle-Shooter
# Short Jam-Ready GDD

**Version:** Jam Build v1.0 | **Date:** June 8, 2026 | **Author:** Jason | **Engine:** GameMaker Studio 2
**Platform:** Android (primary) / PC (secondary) | **Status:** Jam Submission

---

## 1. Elevator Pitch

> "A hybrid idle-shooter where your space defense station runs itself — but goes into overdrive when you pick up the controls."

---

## 2. Genre & Core Fantasy

| Element | Detail |
|---|---|
| Genre | Hybrid Idle + Real-Time Space Shooter |
| Core Fantasy | You are the last line of defense. Your turrets hold the line while you sleep — but when you wake up and take aim, everything changes. |
| Player Role | Station Commander — passive overseer and active combatant in one |
| Offline Gain | Accumulates passively while away; cap lifted for jam build |

---

## 3. Core Loop

**Step 1 → IDLE:** Turrets auto-fire. Resources accumulate. Waves advance passively.

**Step 2 → ENGAGE:** Player takes manual control: aim, shoot, deploy active abilities, collect drops.

**Step 3 → UPGRADE:** Spend resources between waves: upgrade turrets, weapons, station modules. Loop repeats.

---

## 4. Jam Scope

| ✓ IN — Jam Build | ✗ OUT — Post-Launch |
|---|---|
| 1 player ship with 2 weapon slots | Prestige / Ascension system |
| 3 auto-turret tiers | Full 5-sector campaign |
| 10 wave progression | Rare Alloy / Void Shard currencies |
| 3 enemy types (Drone Scout, Swarm Cluster, Void Cruiser) | All 5 boss types |
| 1 boss — Sector 1 (The Dreadnought) | Full weapon roster (Railgun, Nova Cannon, Ion Scatter) |
| Credits + Energy Cores currencies | Tech research tree |
| Basic idle offline gain (no cap for jam) | Cosmetic shop / season pass |
| Mobile portrait HUD | Cloud save |
| Adaptive music (idle vs. combat states) | |
| 3 active abilities: Orbital Strike, Shield Overcharge, EMP Burst | |

---

## 5. Player Controls

| Action | Mobile | PC |
|---|---|---|
| Aim & Shoot | Tap / drag | Mouse aim + click |
| Deploy Ability | Tap ability icon | Keys 1 / 2 / 3 |
| Collect Drop | Auto-collect | Auto-collect |
| Open Upgrade Menu | Tap menu button | Tab key |

---

## 6. Enemy Overview — Jam Build

| Enemy | Behavior | Health | Reward |
|---|---|---|---|
| Drone Scout | Fast movement, low health, basic forward shot | Low | +Credits |
| Swarm Cluster | Splits into 3 smaller units on death | Medium | +Energy Cores |
| Void Cruiser | Slow, high HP, fires spread shot pattern | High | +Credits + rare drop |

---

## 7. Sector 1 Boss — "The Dreadnought"

| Phase | Trigger | Behavior |
|---|---|---|
| Phase 1 | 100% HP | Fires homing missiles in salvos of 3 |
| Phase 2 | 50% HP | Activates frontal shield — must be flanked to deal damage |
| Phase 3 | 25% HP | Charge attack + missile swarm simultaneously |

**Boss Drop:** Void Core — unlocks the Tier 3 auto-turret upgrade.

---

## 8. Art Direction

| Element | Spec |
|---|---|
| Visual Style | Minimalist pixel-art / vector hybrid; dark space background with parallax star layers |
| Enemy Design | Geometric, angular forms — mechanical and alien |
| Kill Effects | Particle burst on kill; screen shake on boss hits; neon glow on active player shots |
| Palette | #0A0A1A (Deep Black BG), #00BFFF (Neon Blue Accent), #FF6B35 (Plasma Orange), #FFFFFF (UI Text) |

---

## 9. Audio Direction

| State | Audio Design |
|---|---|
| Idle State | Low ambient synth hum; slow pulse beat — calm, atmospheric |
| Combat State | Electronic percussion activates; tempo escalates with wave number |
| Boss Encounter | Full cinematic score track — distinct from all wave music |
| SFX Priorities | Weapon fire → Turret fire → Enemy death → Ability activation → Upgrade ding |

---

## 10. Jam Timeline

| Day / Block | Goals |
|---|---|
| Day 1 — AM | Core idle loop working: turrets auto-fire, resources tick, waves spawn |
| Day 1 — PM | Player ship movement, primary weapon, basic enemy AI |
| Day 2 — AM | Upgrade menu, wave 1–10 tuning, Dreadnought Phase 1 |
| Day 2 — PM | UI polish, sound integration, mobile portrait build test |
| Day 3 | Bug fix, balance pass, submission packaging |

---

## 11. Solo Dev Notes

- Build order: core loop first — art is always last.
- Placeholder neon shapes acceptable for jam; they communicate intent clearly.
- Prioritize feel over completeness — 10 tight waves beats 30 broken ones.
- Use GMS2 built-in particle system for all explosion and impact effects.
- Save system: local JSON only for jam build — no cloud dependency required.

---

*Outer Space Defense — Jam Build v1.0 | Author: Jason | June 8, 2026 | GameMaker Studio 2*
