import pytest
from dcolor.rgb import *

@pytest.fixture(scope="function", autouse=False)
def rgb_init():
    rgb = RGB(
        rgb="r=0,b=235,g=3",
    )
    yield rgb 

def test_init():
    RGB(
        rgb="r=0,b=235,g=3",
    )

@pytest.mark.parametrize(
    "rgb", [
    10,
    10.0,
    True,
])
def test_rgb_type_err(rgb):
    with pytest.raises(
        TypeError
    ):
        RGB(rgb=rgb)

def test_rgb_init_list():
    RGB(
        rgb=[
            10,
            10,
            10
        ]
   )

def test_rgb_init_dict():
    RGB(
        rgb={
            "r": 0,
            "g": 0,
            "b": 0,
        }
    )

def test_rgb_init_str():
    RGB(
        rgb="r=0, g=0, b=0"
    )

def test_rgb_init_str2():
    RGB(
        rgb="0, 0,0"
    )

def test_rgb_list_type_err():
    with pytest.raises(
        TypeError
    ):
        RGB(rgb=[
            10.0,
            10.0,
            10.0
        ])

def test_rgb_list_value_err():
    with pytest.raises(
        ValueError
    ):
        RGB(rgb=[
            1000,
            -100,
            100
        ])

def test_rgb_list_length_err():
    with pytest.raises(
        ValueError
    ):
        RGB(rgb=[
            100,
            100,
            100,
            100
        ])

def test_rgb_dict_key_type_err():
    with pytest.raises(
        TypeError
    ):
        RGB(rgb={
            1: 255,
            2: 233,
            4: 222,
        })

def test_rgb_dict_key_type_err2():
    with pytest.raises(
        TypeError
    ):
        RGB(rgb={
            "r": "255",
            "g": "255",
            "b": "255",
        })

def test_rgb_dict_len_err():
    with pytest.raises(
        ValueError
    ):
        RGB(rgb={
            "r": 255,
            "g": 255,
            "b": 255,
            "a": 255,
        })

def test_rgb_dict_key_err():
    with pytest.raises(
        KeyError
    ):
        RGB(rgb={
            "r": 255,
            "g": 255,
            "a": 255,
        })

@pytest.mark.parametrize(
    "dict_value",[
    1,
    1.0,
    "r=1, g=1, b=1",
    b"r=1, g=1, b=1",
    ["r=1, g=1, b=1"],
])
def test_rgb_dict_value_err(rgb_init,dict_value):
    with pytest.raises(
        ValueError
    ):
        RGB._rgb_dict(rgb_init,dict_value)

def test_rgb_string_value_err():
    with pytest.raises(
        ValueError
    ) as raiseinfo:
        RGB(
            rgb="fadsfsfsaf"
        )
    print(raiseinfo.value)

def test_rgb_string_value_err2():
    with pytest.raises(
        ValueError
    ) as raiseinfo:
        RGB(
            rgb="r=255, b=255, a=233"
        )
    print(raiseinfo.value)

def test_rgb_string_value_err3():
    with pytest.raises(
        ValueError
    ) as raiseinfo:
        RGB(
            rgb="r=255, b=255,`=233"
        )
    print(raiseinfo.value)

def test_rgb_string_value_err4():
    with pytest.raises(
        ValueError
    ) as raiseinfo:
        RGB(
            rgb="255"
        )
    print(raiseinfo.value)

@pytest.mark.parametrize(
    "string",[
    1,
    1.0,
    b"r=1, g=2, b=21",
    ["r=1, g=2, b=21"],
    {"value": "r=1, g=2, b=21"}
])
def test_rgb_string_value_err5(rgb_init, string):
    with pytest.raises(
        ValueError
    ) as raiseinfo:
        RGB._rgb_string(
            cls=rgb_init,
            value=string,
        )
    print(raiseinfo.value)

def test_str(rgb_init):
    result = str(rgb_init)
    assert isinstance(result, str)

def test_call(rgb_init):
    result = rgb_init.__call__()
    assert isinstance(result, str)

def test_rgb(rgb_init):
    result = rgb_init.rgb
    assert isinstance(result, tuple)

def test_instance_value_error():
    class A:
        ...
    with pytest.raises(
        ValueError
    ):
        RGB._instance(A)
