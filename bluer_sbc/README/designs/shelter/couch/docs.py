from bluer_sbc.README.designs.shelter.couch import parts
from bluer_sbc.README.designs.shelter.couch.items import items

docs = [
    {
        "path": f"../docs/shelter/couch",
        "items": items,
    },
    {
        "path": f"../docs/shelter/couch/validation.md",
    },
] + parts.docs
