from bluer_sbc.README.designs.shelter.couch import docs as couch
from bluer_sbc.README.designs.shelter.jacket import docs as jacket

docs = (
    [
        {
            "path": "../docs/shelter/",
        }
    ]
    + couch.docs
    + jacket.docs
)
