from .cm import CMMember
from .where import BaseWhere

class Index(CMMember, BaseWhere):
    _MODESTR="index"
    def __new__(
        cls,
        *args,
        **kwargs
    ):
        if len(args) == 0 or len(kwargs) == 0:
            return Index._MODESTR
        
        return super().__new__(
            cls,**kwargs
        )

    def __init__(
        self,
        index,
        where,
    ):
        self.index = index
        self.where = where

    def __str__(self):
        return "index"

    @staticmethod
    def index_string(index, where):
        return f"\033[;{where.value};5;{self.index}m"

    def __call__(self):
        return self.index_string(
            index=self.index
            where=self.where
        )

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        if not isinstance(value, int):
            raise TypeError(
                "index must be int type."
            )
        if value > 255 or value < 0:
            raise ValueError(
                "index must be 0~255(int)."
            )
        self._index = value
