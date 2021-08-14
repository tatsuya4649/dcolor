import pytest
from dcolor.cm import *

def test_colormodemeta_str_err():
    with pytest.raises(
        AttributeError
    ):
        class A(metaclass=ColorModeMeta):
            ...

def test_colormodemeta_call_err():
    with pytest.raises(
        AttributeError
    ):
        class A(metaclass=ColorModeMeta):
            def __str__(self):
                pass

def test_cmmode_str_notimplemented_err():
    member = CMMember()
    with pytest.raises(
        NotImplementedError
    ):
        str(member)

def test_cmmode_call_notimplemented_err():
    member = CMMember()
    with pytest.raises(
        NotImplementedError
    ):
        member.__call__()
