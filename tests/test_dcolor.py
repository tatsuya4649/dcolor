import pytest
from dcolor._dcolor import *

_STRING = "Hello World"

def test_colors():
    result = colors(
        string=_STRING,
        color="red",
    )
    assert isinstance(result, str)
    print(f"RESULT: {result}")
    assert result == (
        "\033[;38;5;1m" +
        _STRING +
        "\033[;0m"
    )

def test_backgrounds():
    result = backgrounds(
        string=_STRING,
        color="red",
    )
    assert isinstance(result, str)
    print(f"RESULT: {result}")
    assert result == (
        "\033[;48;5;1m" +
        _STRING +
        "\033[;0m"
    )

@pytest.mark.parametrize(
    "string",[
    b"hello",
    True,
    10,
    10.0,
    ["string"],
    {"string": "hello"},
])
def test_colors_string_type_err(string):
    with pytest.raises(
        TypeError
    ):
        colors(
            string=string,
            color="red",
        )

@pytest.mark.parametrize(
    "string",[
    b"hello",
    True,
    10,
    10.0,
    ["string"],
    {"string": "hello"},
])
def test_attr_string_type_err(string):
    with pytest.raises(
        TypeError
    ):
        attributes(
            string=string,
            attr="bold"
        )

def test_attr():
    result = attributes(
        string=_STRING,
        attr="bold",
    )
    assert isinstance(result, str)
    print(f"RESULT: {result}")
    assert result == (
        "\033[1m" +
        _STRING +
        "\033[0m"
    )
    
