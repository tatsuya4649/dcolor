import pytest
from dcolor.color import *
from dcolor.where import *
from dcolor.mode import *

@pytest.fixture(scope="function", autouse=False)
def color_init():
    color = Color(
        color="red",
        mode=ColorMode.NAME.value(),
        where=ColorWhere.CHARACTER,
    )
    yield color

def test_init():
    Color(
        color="red",
        mode=ColorMode.NAME.value(),
        where=ColorWhere.CHARACTER,
    )

def test_init_colormode():
    Color(
        color="red",
        mode=ColorMode.NAME,
        where=ColorWhere.CHARACTER,
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
        Color(
            color="red",
            mode=mode,
            where=ColorWhere.CHARACTER,
        )

def test_start(color_init):
    result = color_init.start()
    assert isinstance(result, str)


def test_call(color_init):
    result = color_init.__call__()
    assert isinstance(result, str)
