import pytest
from dcolour._dcolour import *

_STRING = "Hello World"

def test_colours():
    result = colours(
        string=_STRING,
        colour="red",
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
        colour="red",
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
def test_colours_string_type_err(string):
    with pytest.raises(
        TypeError
    ):
        colours(
            string=string,
            colour="red",
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
    
