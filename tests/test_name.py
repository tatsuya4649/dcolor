import pytest
from dcolor.name import *
from dcolor.where import *

@pytest.fixture(scope="function", autouse=False)
def name_init():
    name = Name(
        color="red",
        where=ColorWhere.CHARACTER,
    )
    yield name


def test_init_string():
    result = Name()
    assert isinstance(result, str)
    assert result == Name._MODESTR

def test_init_str_type():
    result = Name(
        color="red",
    )
def test_init_int_type():
    result = Name(
        color=1,
    )

@pytest.mark.parametrize(
    "where", [
    ColorWhere.CHARACTER,
    ColorWhere.BACKGROUND,
])
def test_init_where(where):
    result = Name(
        color="red",
        where=where,
    )

@pytest.mark.parametrize(
    "color", [
    10.0,
    b"color",
    ["red"],
    {"color": "red"},
])
def test_color_type_err(color):
    with pytest.raises(
        TypeError
    ):
        Name(
            color=color,
            where=ColorWhere.CHARACTER,
        )

def test_color_value_err():
    with pytest.raises(
        ValueError
    ):
        Name(
            color="color",
            where=ColorWhere.CHARACTER,
        )

def test_color_value_err2():
    with pytest.raises(
        ValueError
    ):
        Name(
            color=300,
            where=ColorWhere.CHARACTER,
        )

def test_color_str(name_init):
    result = str(name_init)
    assert isinstance(result, str)
    assert result == Name._MODESTR

def test_call(name_init):
    result = name_init()
    assert isinstance(result, str)
