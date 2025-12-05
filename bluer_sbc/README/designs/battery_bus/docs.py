from bluer_sbc.README.design import design_doc
from bluer_sbc.README.designs.battery_bus import parts
from bluer_sbc.README.designs.battery_bus.items import items
from bluer_sbc.README.designs.battery_bus.body import docs as body

docs = (
    [
        design_doc(
            "battery_bus",
            items,
            own_folder=True,
            parts_reference="../parts",
            cols=2,
        )
    ]
    + body.docs
    + parts.docs
)
