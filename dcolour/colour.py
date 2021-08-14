from .mode import ColourMode
from .where import BaseWhere
from .deco import _decorate_base


class Colour(BaseWhere, metaclass=_decorate_base):
    def __init__(
        self,
        colour,
        mode,
        where,
    ):
        self.mode = mode
        self._colour = colour
        self.where = where
    
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if not isinstance(value, (str, ColourMode)):
            raise TypeError(
                "mode must be str type."
            )
        if isinstance(value, str):
            # check valid mode value
            self._mode = ColourMode.mode(value)
        else:
            self._mode = value

    def __call__(self):
        return self.mode(
            colour=self._colour,
            where=self.where,
        )()

    def start(self):
        return self.__call__()
