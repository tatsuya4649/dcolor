from .mode import ColourMode

class Coulor:
    def __init__(
        self,
        color,
        mode,
        where,
    ):
        self.mode = mode(color)
        self._color = color
    
    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, value):
        if not isinstance(value, str):
            raise TypeError(
                "mode must be str type."
            )
        # check valid mode value
        ColourMode.mode(value)
        self._mode = value

    @property
    def where(self):
        return self._where

    @where.setter
    def where(self, value):
        if not type(value) is ColourWhere:
            raise TypeError(
                "where must be ColourWhere."
            )
        self._where = value
    def __call__(self):
        return self.mode(self._color)()
