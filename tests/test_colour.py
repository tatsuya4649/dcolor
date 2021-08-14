import pytest
from dcolour.colour import *
from dcolour.where import *
from dcolour.mode import *

@pytest.fixture(scope="function", autouse=False)
def colour_init():
    colour = Colour(
        colour="red",
        mode=ColourMode.NAME.value(),
        where=ColourWhere.CHARACTER,
    )
    yield colour

def test_init():
    Colour(
        colour="red",
        mode=ColourMode.NAME.value(),
        where=ColourWhere.CHARACTER,
    )

def test_init_colourmode():
    Colour(
        colour="red",
        mode=ColourMode.NAME,
        where=ColourWhere.CHARACTER,
    )

@pytest.mark.parametrize(
    "mode", [
    b"mode",
    10,
    10.0,
    ["mode"],
    {"mode": "name"},
    True,
])
def test_mode_type_error(mode):
    with pytest.raises(
        TypeError
    ):
        Colour(
            colour="red",
            mode=mode,
            where=ColourWhere.CHARACTER,
        )

def test_start(colour_init):
    result = colour_init.start()
    assert isinstance(result, str)


def test_call(colour_init):
    result = colour_init.__call__()
    assert isinstance(result, str)
