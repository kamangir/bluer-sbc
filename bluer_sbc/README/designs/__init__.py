from bluer_objects import markdown

from bluer_sbc.parts.db import db_of_parts
from bluer_sbc.README.designs.cheshmak import items as cheshmak_items
from bluer_sbc.README.designs.battery_bus import items as battery_bus_items
from bluer_sbc.README.designs.swallow import items as swallow_items
from bluer_sbc.README.designs.swallow_head import items as swallow_head_items
from bluer_sbc.README.designs.bryce import items as bryce_items
from bluer_sbc.README.designs.nafha import items as nafha_items
from bluer_sbc.README.designs.shelter import items as shelter_items
from bluer_sbc.README.designs.x import items as x_items
from bluer_sbc.README.designs.ultrasonic_sensor_tester import (
    items as ultrasonic_sensor_tester_items,
)
from bluer_sbc.designs.swallow.parts import dict_of_parts as swallow_parts
from bluer_sbc.designs.swallow_head.parts import dict_of_parts as swallow_head_parts

docs = [
    {
        "cols": 4,
        "items": design_info["items"],
        "path": f"../docs/{design_name}.md",
        "macros": design_info.get("macros", {}),
    }
    for design_name, design_info in {
        "battery-bus": {
            "items": battery_bus_items,
        },
        "bryce": {
            "items": bryce_items,
        },
        "cheshmak": {
            "items": cheshmak_items,
        },
        "nafha": {
            "items": nafha_items,
        },
        "shelter": {
            "items": shelter_items,
        },
        "swallow-head": {
            "items": swallow_head_items,
            "macros": {
                "parts_images:::": markdown.generate_table(
                    db_of_parts.as_images(
                        swallow_head_parts,
                        reference="../../../parts",
                    )
                ),
                "parts_list:::": db_of_parts.as_list(
                    swallow_head_parts,
                    reference="../../../parts",
                    log=False,
                ),
            },
        },
        "swallow": {
            "items": swallow_items,
            "macros": {
                "parts_images:::": markdown.generate_table(
                    db_of_parts.as_images(
                        swallow_parts,
                        reference="../../../parts",
                    )
                ),
                "parts_list:::": db_of_parts.as_list(
                    swallow_parts,
                    reference="../../../parts",
                    log=False,
                ),
            },
        },
        "ultrasonic-sensor-tester": {
            "items": ultrasonic_sensor_tester_items,
        },
        "x": {
            "items": x_items,
        },
    }.items()
]
