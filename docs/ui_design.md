# SkyBorn — UI Design Document

**Project:** SkyBorn-Dream-or-Reality-
**Version:** 1.0.0
**Status:** Placeholder — pending full design spec
**Last Updated:** 2026-06-09

---

## Overview

This document outlines the user interface design guidelines, layout structure, and component specifications for the SkyBorn platform. It serves as the central reference for all UI development and visual design decisions.

---

## Design Principles

- **Clarity** — Information is presented cleanly and without clutter.
- **Atmosphere** — Visual language reflects the desert sky environment: deep blues, warm amber, and dusty neutrals.
- **Responsiveness** — All views must function across desktop, tablet, and mobile.
- **Accessibility** — WCAG 2.1 AA compliance required across all components.

---

## Color Palette

| Name         | Hex       | Usage                        |
|--------------|-----------|------------------------------|
| Sky Blue     | #4A90D9   | Primary accent, links        |
| Desert Amber | #E8A020   | Alerts, highlights           |
| Dusk Purple  | #2D2A45   | Background, dark mode base   |
| Dust White   | #F5F0E8   | Light mode background        |
| Smog Gray    | #8C8C8C   | Secondary text, borders      |

---

## Typography

- **Headings:** Inter Bold, 24–48px
- **Body:** Inter Regular, 14–16px
- **Monospace / Data:** JetBrains Mono, 13px

---

## Layout Structure

```
[ Header / Nav Bar          ]
[ Sidebar ] [ Main Content  ]
           [ Data Panels    ]
[ Footer                    ]
```

### Header
- Logo (left)
- Navigation links: Dashboard, Sensors, Reports, Docs
- User avatar + settings (right)

### Sidebar
- Mission status indicator
- Active sensor feed list
- Quick-access links to /assets and /docs

### Main Content Area
- Real-time air quality dashboard
- Map view of sensor locations
- Alerts panel

---

## Components

| Component       | Description                                      | Status      |
|-----------------|--------------------------------------------------|-------------|
| NavBar          | Top navigation with logo and user controls       | Placeholder |
| SensorCard      | Displays individual sensor readings              | Placeholder |
| AlertBanner     | Full-width banner for threshold breaches         | Placeholder |
| DataChart       | Line/bar chart for atmospheric trend data        | Placeholder |
| MapView         | Interactive sensor location map                  | Placeholder |
| ReportPanel     | Filterable report viewer linked to /docs         | Placeholder |

---

## Assets Reference

All UI assets (icons, images, logos) are stored in the `/assets` directory.
See `assets/assets_manifest.md` for a full inventory.

---

## Notes

> This is a placeholder document. Replace each section with finalized design specifications as the project progresses.
