from bluer_sbc.README.designs.shelter.couch import parts
from bluer_sbc.README.designs.shelter.couch.items import items

docs = [
    {
        "path": "../docs/shelter/couch",
        "items": items,
    },
    {
        "path": "../docs/shelter/couch/validation.md",
    },
] + parts.docs
