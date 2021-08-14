import pytest
from dcolour.deco import _decorate_base

def test_not_imple_call():
    with pytest.raises(
        NotImplementedError
    ):
        class A(metaclass=_decorate_base):
            def start():
                ...
            def end():
                ...

def test_not_imple_start():
    with pytest.raises(
        NotImplementedError
    ):
        class A(metaclass=_decorate_base):
            def __call__(self):
                ...
            def end():
                ...

def test_not_imple_end():
    with pytest.raises(
        NotImplementedError
    ):
        class A(metaclass=_decorate_base):
            def __call__(self):
                ...
            def start():
                ...
