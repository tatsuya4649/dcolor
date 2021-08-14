import pytest
from dcolour.name import *
from dcolour.where import *

@pytest.fixture(scope="function", autouse=False)
def name_init():
    name = Name(
        colour="red",
        where=ColourWhere.CHARACTER,
    )
    yield name


def test_init_string():
    result = Name()
    assert isinstance(result, str)
    assert result == Name._MODESTR

def test_init_str_type():
    result = Name(
        colour="red",
    )
def test_init_int_type():
    result = Name(
        colour=1,
    )

@pytest.mark.parametrize(
    "where", [
    ColourWhere.CHARACTER,
    ColourWhere.BACKGROUND,
])
def test_init_where(where):
    result = Name(
        colour="red",
        where=where,
    )

@pytest.mark.parametrize(
    "colour", [
    10.0,
    b"colour",
    ["red"],
    {"colour": "red"},
])
def test_colour_type_err(colour):
    with pytest.raises(
        TypeError
    ):
        Name(
            colour=colour,
            where=ColourWhere.CHARACTER,
        )

def test_colour_value_err():
    with pytest.raises(
        ValueError
    ):
        Name(
            colour="colour",
            where=ColourWhere.CHARACTER,
        )

def test_colour_value_err2():
    with pytest.raises(
        ValueError
    ):
        Name(
            colour=300,
            where=ColourWhere.CHARACTER,
        )

def test_colour_str(name_init):
    result = str(name_init)
    assert isinstance(result, str)
    assert result == Name._MODESTR

def test_call(name_init):
    result = name_init()
    assert isinstance(result, str)
