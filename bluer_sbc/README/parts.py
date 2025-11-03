from bluer_sbc.parts.db import db_of_parts

docs = [
    {
        "path": "../docs/parts",
        "macros": {
            "parts_list:::": db_of_parts.README,
            "parts_images:::": db_of_parts.as_list(
                {part.name: "" for part in db_of_parts},
                reference="../parts",
                log=False,
            ),
        },
    }
] + [
    {
        "path": part.filename(create=True),
        "macros": {
            "info:::": part.README(db_of_parts.url_prefix),
        },
    }
    for part_name, part in db_of_parts.items()
    if part_name != "template"
]
