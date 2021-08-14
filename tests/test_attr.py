import pytest
from dcolor.attr import *

def attr_init():
    attr = Attr(
        kind="bold"
    )
    yield attr

def test_init():
    Attr(
        kind="bold"
    )

def test_init2():
    Attr(
        kind=AttrList.bold
    )

@pytest.mark.parametrize(
    "kind", [
    b"kind",
    10,
    10.0,
    ["bold"],
    {"kind": "bold"},
    True
])
def test_kind_type_err(kind):
    with pytest.raises(
        TypeError
    ) as raiseinfo:
        attr = Attr(
            kind=kind,
        )

def test_kind_value_err():
    with pytest.raises(
        ValueError
    ) as raiseinfo:
        attr = Attr(
            kind="kind",
        )

def test_call():
    attr = Attr(
        kind="bold",
    )
    result = attr.__call__()
    assert isinstance(result, str)
    assert result == "\033[1m"

def test_end():
    attr = Attr(
        kind="bold",
    )
    result = attr.end()
    assert isinstance(result, str)
    assert result == "\033[0m"
