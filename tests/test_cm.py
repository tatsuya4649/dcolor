import pytest
from dcolour.cm import *

def test_colourmodemeta_str_err():
    with pytest.raises(
        AttributeError
    ):
        class A(metaclass=ColourModeMeta):
            ...

def test_colourmodemeta_call_err():
    with pytest.raises(
        AttributeError
    ):
        class A(metaclass=ColourModeMeta):
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
