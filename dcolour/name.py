from enum import Enum
from .cm import CMMember
from .where import BaseWhere, ColourWhere
from .index import Index

class NameList(Enum):
    black = {
        "name": "black",
        "number": 0
    }
    red = {
        "name": "red",
        "number": 1
    }
    green = {
        "name": "green",
        "number": 2,
    }
    yellow = {
        "name": "yellow",
        "number": 3,
    }
    blue = {
        "name": "blue",
        "number": 4,
    }
    megenta = {
        "name": "megenta",
        "number": 5,
    }
    cyan = {
        "name": "cyan",
        "number": 6,
    }
    white = {
        "name": "white",
        "number": 7,
    }
    dark_gray = {
        "name": "dark_gray",
        "number": 8,
    }
    bright_red = {
        "name": "bright_red",
        "number": 9,
    }
    bright_green = {
        "name": "bright_green",
        "number": 10,
    }
    bright_yellow = {
        "name": "bright_yellow",
        "number": 11,
    }
    bright_blue = {
        "name": "bright_blue",
        "number": 12,
    }
    bright_megenta = {
        "name": "bright_megenta",
        "number": 13,
    }
    bright_cyan = {
        "name": "bright_cyan",
        "number": 14,
    }
    bright_white = {
        "name": "bright_white",
        "number": 15,
    }


class Name(CMMember, BaseWhere):
    _MODESTR="name"
    def __new__(
        cls,
        *args,
        **kwargs,
    ):
        if len(args) == 0 and len(kwargs) == 0:
            return Name._MODESTR
        return super().__new__(
            cls
        )

    def __init__(
        self,
        colour,
        where=ColourWhere.CHARACTER,
    ):
        self.colour = colour
        self.where = where

    @property
    def colour(self):
        return self._colour
    
    @colour.setter
    def colour(self, value):
        if not isinstance(value, (str, int)):
            raise TypeError(
                "colour must be str or int type."
            )
        if isinstance(value, str):
            for x in NameList:
                if x.value["name"] == value:
                    self._colour = x
                    return
            raise ValueError(
                "invalid colour string."
                f"valid colour string({','.join([x.value['name'] for x in NameList])}) ."
                f"now {value}"
            )
        if isinstance(value, int):
            for x in NameList:
                if x.value["number"] == value:
                    self._colour = x
                    return
            raise ValueError(
                "invalid colour number."
                f"valid colour numebr({','.join([x.value['name'] for x in NameList])})"
            )

    def __str__(self):
        return self._MODESTR

    def __call__(self):
        return Index.index_string(
            index=self.colour.value["number"],
            where=self.where,
        )

