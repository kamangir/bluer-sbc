from bluer_sbc.README.designs.isatis import description, parts, power
from bluer_sbc.README.designs.isatis.body import docs as body
from bluer_sbc.README.designs.isatis.items import items

docs = (
    [
        {
            "path": "../docs/isatis",
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
    + power.docs
)
