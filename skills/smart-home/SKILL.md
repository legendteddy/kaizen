---
name: smart-home
description: Home Assistant integration (local-first) for controlling lights/climate/scenes via REST API.
---

# Protocol: Smart Home (Home Assistant)

This skill integrates with a Home Assistant instance via its REST API.

## Setup

Environment variables:
- `HOME_ASSISTANT_URL` (example: `http://homeassistant.local:8123`)
- `HOME_ASSISTANT_TOKEN` (Home Assistant long-lived access token)

Optional:
- `HOME_ASSISTANT_VERIFY_TLS` (`true`/`false`, default `true`)

## Tooling (Repo Local)

CLI helper:
```powershell
python tools\ha.py --help
```

Examples:
```powershell
# list all entity states (can be large)
python tools\ha.py states

# read one entity
python tools\ha.py state --entity light.living_room

# call a service
python tools\ha.py call --domain light --service turn_on --data "{\"entity_id\":\"light.living_room\",\"brightness_pct\":40}"

# toggle a light
python tools\ha.py toggle --entity light.living_room

# set thermostat temperature
python tools\ha.py set-temp --entity climate.thermostat --temp 72
```

## Safety Rules

- Default to **read-only**: prefer `states` and `state` before changing anything.
- Confirm the target `entity_id` exactly (copy/paste from `states` output).
- Avoid broad service calls like `light.turn_off` without an `entity_id`.
- For automations/scenes, prefer calling a specific `scene.turn_on` or `script.turn_on`.

## Common Home Assistant Endpoints

- `GET /api/` (status)
- `GET /api/states` (all states)
- `GET /api/states/{entity_id}` (one state)
- `POST /api/services/{domain}/{service}` (service call)

