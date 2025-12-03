from bluer_sbc.README.design import design_doc
from bluer_sbc.README.designs.cheshmak import operation, validations
from bluer_sbc.README.designs.cheshmak.items import items
from bluer_sbc.README.designs.cheshmak.body import docs as body
from bluer_sbc.README.designs.cheshmak.parts import parts


docs = (
    [
        design_doc(
            "cheshmak",
            items,
            parts,
            own_folder=True,
        ),
    ]
    + body.docs
    + operation.docs
    + validations.docs
)
