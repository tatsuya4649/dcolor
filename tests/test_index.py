import pytest
from dcolor.index import *
from dcolor.where import *


@pytest.fixture(scope="function", autouse=False)
def index_init():
    index = Index(
        index=255,
        where=ColorWhere.BACKGROUND,
    )
    yield index
    

def test_init():
    Index(
        index=255,
        where=ColorWhere.BACKGROUND,
    )

@pytest.mark.parametrize(
    "index", [
    100.0,
    "100",
    b"100",
    [100],
    {"index": 100},
])
def test_init_type_err(index):
    with pytest.raises(
        TypeError
    ):
        Index(
            index=index,
        )

def test_init_value_err():
    with pytest.raises(
        ValueError
    ):
        Index(
            index=-290,
        )

def test_str(index_init):
    result = str(index_init)
    assert isinstance(result, str)


def test_call(index_init):
    result = index_init.__call__()
    assert isinstance(result, str)
