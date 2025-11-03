from typing import Dict, List

from bluer_objects import markdown

from bluer_sbc.parts.db import db_of_parts


def design_doc(
    design_name: str,
    items: List[str] = [],
    dict_of_parts: dict = {},
    macros: dict = {},
    own_folder: bool = False,
) -> Dict:
    macros_ = {}
    if dict_of_parts:
        macros_ = {
            "parts_images:::": markdown.generate_table(
                db_of_parts.as_images(
                    dict_of_parts,
                    reference="./parts",
                ),
                cols=10,
                log=False,
            ),
            "parts_list:::": db_of_parts.as_list(
                dict_of_parts,
                reference="./parts",
                log=False,
            ),
        }

    macros_.update(macros)

    return {
        "path": "../docs/{}{}".format(design_name, "" if own_folder else ".md"),
        "items": items,
        "macros": macros_,
    }
