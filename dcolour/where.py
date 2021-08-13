from enum import Enum

class ColourWhere(Enum):
    CHARACTER = "38"
    BACKGROUND = "48"

class BaseWhere:
    @property
    def where(self):
        return self._where
    @where.setter
    def where(self, value):
        if not type(value) is ColourWhere:
            raise TypeError(
                "where must be ColourWhere type."
            )
        self._where = value
