from bluer_objects.README.items import ImageItems

from bluer_sbc.README.design import design_doc
from bluer_sbc.README.designs.consts import assets2
from bluer_sbc.README.designs.swallow import latest_version
from bluer_sbc.README.designs.swallow.parts import parts

docs = [
    design_doc(
        f"swallow/v{version}.md",
        ImageItems(
            {
                (assets2 + "swallow/design/v{}/{}?raw=true").format(
                    version,
                    f"{index+1:02}.jpg",
                ): ""
                for index in range(6)
            }
        ),
        parts,
        own_folder=True,
    )
    for version in range(1, latest_version)
]
