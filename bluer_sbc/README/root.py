from bluer_sbc.designs.cheshmak import marquee as cheshmak_marquee
from bluer_sbc.designs.blue_bracket import items as blue_bracket_items
from bluer_sbc.designs.swallow import marquee as swallow_marquee
from bluer_sbc.designs.swallow_head import marquee as swallow_head_marquee
from bluer_sbc.designs.bryce import marquee as bryce_marquee
from bluer_sbc.designs.nafha import marquee as nafha_marquee
from bluer_sbc.designs.shelter import marquee as shelter_marquee
from bluer_sbc.designs.ultrasonic_sensor_tester import (
    marquee as ultrasonic_sensor_tester_marquee,
)

docs = [
    {
        "items": swallow_marquee
        + swallow_head_marquee
        + ultrasonic_sensor_tester_marquee
        + bryce_marquee
        + cheshmak_marquee
        + nafha_marquee
        + shelter_marquee
        + blue_bracket_items,
        "path": "..",
    },
]
