from bluer_sbc.README.designs.kulej import description, parts
from bluer_sbc.README.designs.kulej.body import docs as body
from bluer_sbc.README.designs.kulej.items import items

docs = (
    [
        {
            "path": "../docs/kulej",
            "items": items,
            "macros": {
                "description_long_en:::": description["long"]["en"],
                "description_long_fa:::": description["long"]["fa"],
                "description_short_en:::": description["short"]["en"],
                "description_short_fa:::": description["short"]["fa"],
            },
        }
    ]
    + body.docs
    + parts.docs
)
