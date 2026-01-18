from bluer_sbc.README.design import design_doc
from bluer_sbc.README.designs.isatis import parts
from bluer_sbc.README.designs.isatis.body import docs as body
from bluer_sbc.README.designs.isatis.items import items

docs = (
    [
        {
            "path": "../docs/isatis",
            "items": items,
        }
    ]
    + body.docs
    + parts.docs
)
