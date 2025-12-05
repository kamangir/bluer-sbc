import pytest
from typing import Dict, List

from bluer_sbc.README.design import design_doc, design_doc_parts
from bluer_sbc.README.designs.anchor.items import items
from bluer_sbc.README.designs.anchor.parts import parts as dict_of_parts


@pytest.mark.parametrize(
    ["items"],
    [
        [[]],
        [items],
    ],
)
@pytest.mark.parametrize(
    ["macros"],
    [
        [{}],
        [{"this": "That"}],
    ],
)
@pytest.mark.parametrize(
    ["own_folder"],
    [
        [False],
        [True],
    ],
)
def test_design_docs(
    items: List[str],
    macros: Dict[str, Dict],
    own_folder: bool,
):
    docs = design_doc(
        "anchor",
        items=items,
        dict_of_parts=dict_of_parts,
        macros=macros,
        own_folder=own_folder,
        parts_reference="./parts",
    )

    assert isinstance(docs, dict)

    for keyword in docs:
        assert isinstance(keyword, str)


def test_design_docs_parts():
    macros = design_doc_parts(
        dict_of_parts=dict_of_parts,
        parts_reference="./parts",
    )

    assert isinstance(macros, dict)

    for keyword in macros:
        assert isinstance(keyword, str)
