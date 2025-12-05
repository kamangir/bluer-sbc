from bluer_sbc.README.design import design_doc
from bluer_sbc.README.designs.anchor import parts
from bluer_sbc.README.designs.anchor.items import items
from bluer_sbc.README.designs.anchor.body import docs as body

docs = (
    [
        design_doc(
            "anchor",
            items,
            own_folder=True,
        )
    ]
    + body.docs
    + parts.docs
)
