from bluer_objects import file

from bluer_sbc.parts.db import db_of_parts
from bluer_sbc.parts.classes.db import PartDB
from bluer_sbc.parts.classes.part import Part


def test_db_of_parts():
    assert isinstance(db_of_parts, PartDB)

    for part in db_of_parts:
        assert isinstance(part, Part)

    # ---

    db_of_parts["template2"] = Part(
        info=[
            "template2",
        ],
        images=[
            "template2.jpg",
        ],
    )

    part = db_of_parts["template2"]
    assert isinstance(part, Part)

    del db_of_parts._db["template2"]  # pylint: disable=protected-access

    # ---

    for part_name, part in db_of_parts.items():
        assert isinstance(part_name, str)
        assert isinstance(part, Part)

    # ---

    README = db_of_parts.README
    assert isinstance(README, list)
    for line in README:
        assert isinstance(line, str)

    # ---

    assert db_of_parts.adjust(dryrun=True)

    # ---

    content = db_of_parts.as_images(dict_of_parts={})
    assert isinstance(content, list)
    for line in content:
        assert isinstance(line, str)

    # ---

    content = db_of_parts.as_list(dict_of_parts={})
    assert isinstance(content, list)
    for line in content:
        assert isinstance(line, str)
