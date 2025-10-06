from bluer_sbc.designs.cheshmak import items as cheshmak_items
from bluer_sbc.designs.swallow import items as swallow_items
from bluer_sbc.designs.swallow_head import items as swallow_head_items
from bluer_sbc.designs.bryce import items as bryce_items
from bluer_sbc.designs.nafha import items as nafha_items
from bluer_sbc.designs.shelter import items as shelter_items
from bluer_sbc.designs.ultrasonic_sensor_tester import (
    items as ultrasonic_sensor_tester_items,
)

docs = [
    {
        "items": swallow_items,
        "path": "../docs/swallow.md",
    },
    {
        "items": swallow_head_items,
        "path": "../docs/swallow-head.md",
    },
    {
        "items": bryce_items,
        "path": "../docs/bryce.md",
    },
    {
        "items": ultrasonic_sensor_tester_items,
        "path": "../docs/ultrasonic-sensor-tester.md",
    },
    {
        "items": cheshmak_items,
        "path": "../docs/cheshmak.md",
    },
    {
        "cols": 4,
        "items": nafha_items,
        "path": "../docs/nafha.md",
    },
    {
        "cols": 4,
        "items": shelter_items,
        "path": "../docs/shelter.md",
    },
]
