from bluer_objects import file

from bluer_sbc.parts.classes.part import Part


def test_part():
    part = Part(
        name="resistor",
        info=[
            "Resistor, 1/4 watt, 5% tolerance",
        ],
        images=["resistor.png"],
    )

    filename = part.filename()
    assert file.exists(filename)

    url = part.image_url(
        url_prefix="/url/",
    )
    assert isinstance(url, str)

    url = part.image_url(
        url_prefix="/url/",
        filename="test.jpg",
    )
    assert isinstance(url, str)

    README = part.README(
        url_prefix="/url/",
    )
    assert isinstance(README, list)
    for line in README:
        assert isinstance(line, str)
