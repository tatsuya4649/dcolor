import pytest
from dcolor.mode import *


def test_mode():
    ColorMode.mode("name")

def test_mode_error():
    with pytest.raises(
        ValueError
    ):
        ColorMode.mode("mode")

def test_mode_str():
    result = ColorMode._mode_str(
        ColorMode.NAME
    )
    assert isinstance(result, str)

@pytest.mark.parametrize(
    "mode",[
    True,
    10,
    10.0,
    ["mode"],
    {"mode": 1},
])
def test_mode_str_attribute_error(mode):
    with pytest.raises(
        AttributeError
    ):
        ColorMode._mode_str(
            mode
        )

def test_mode_str_type_error2():
    class B:
        pass
    class A:
        def __init__(self):
            self.value = B

    with pytest.raises(
        TypeError
    ):
        result = ColorMode._mode_str(
            A()
        )
