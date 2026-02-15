from bluer_sbc.README.designs.shelter.jacket import design, parts
from bluer_sbc.README.designs.shelter.jacket.items import items

docs = (
    [
        {
            "path": "../docs/shelter/jacket/",
            "items": items,
        }
    ]
    + design.docs
    + parts.docs
)
