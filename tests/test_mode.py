import pytest
from dcolour.mode import *


def test_mode():
    ColourMode.mode("name")

def test_mode_error():
    with pytest.raises(
        ValueError
    ):
        ColourMode.mode("mode")

def test_mode_str():
    result = ColourMode._mode_str(
        ColourMode.NAME
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
        ColourMode._mode_str(
            mode
        )

def test_mode_str_type_error():

    class A:
        def __init__(self):
            self.value = 10

    a = A()
    with pytest.raises(
        TypeError
    ):
        ColourMode._mode_str(
            a
        )
