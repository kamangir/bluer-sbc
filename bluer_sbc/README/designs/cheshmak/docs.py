from bluer_sbc.README.designs.cheshmak.items import items
from bluer_sbc.README.designs.cheshmak import operation, v1
from bluer_sbc.README.design import design_doc


docs = (
    [
        design_doc(
            "cheshmak",
            items,
            own_folder=True,
        ),
    ]
    + operation.docs
    + v1.docs
)
