from bluer_sbc.README.design import design_doc
from bluer_sbc.README.designs.kulej import parts
from bluer_sbc.README.designs.kulej.body import docs as body
from bluer_sbc.README.designs.kulej.items import items

docs = (
    [
        {
            "path": "../docs/kulej",
            "items": items,
        }
    ]
    + body.docs
    + parts.docs
)
