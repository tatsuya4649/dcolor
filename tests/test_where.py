import pytest
from unittest import mock
from dcolor.where import *

@pytest.fixture(scope="function", autouse=False)
def where_init():
    where = BaseWhere()
    yield where

def test_init():
    where = BaseWhere()

@pytest.mark.parametrize(
    "value", [
    "value",
    1,
    1.0,
    [ColorWhere.CHARACTER],
    {"where": ColorWhere.CHARACTER},
])
def test_where_type_err(where_init, value):
    with pytest.raises(
        TypeError
    ):
        where_init.where = value

@pytest.mark.parametrize(
    "value", 
    [x for x in ColorWhere]
)
def test_where(where_init, value):
    where_init.where = value

def test_end_none(where_init):
    with mock.patch(
        "dcolor.where.BaseWhere.where",
        new_callable=mock.PropertyMock(),
    ) as mock_where:
        mock_where.return_value = None
        result = where_init.end()
        assert result is None
