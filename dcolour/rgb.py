import re
from .cm import CMMember
from .where import BaseWhere

class RGB(CMMember, BaseWhere):
    _MODESTR="rgb"
    def __new__(
        cls,
        **kwargs
    ):
        if len(args) == 0 or len(kwargs) == 0:
            return RGB._MODESTR
        
        return super().__new__(
            cls,**kwargs
        )
    def __init__(
        self,
        rgb,
        where,
    ):
        self.rgb = rgb

    @property
    def rgb(self):
        return (
            self._r,
            self._g,
            self._b
        )

    @rgb.setter
    def rgb(self, value):
        if not isinstance(value, (str, dict, list, tuple)):
            raise TypeError(
                "rbg must be str or dict,list type."
            )
        if isinstance(value, str):
            self._rgb_string(value)
        if isinstance(value, dict):
            self._rgb_dict(value)
        if isinstance(value, (list, tuple)):
            self._rgb_list(value)

    @staticmethod
    def _rgb_string(value):
        devide = re.finditer(
            r"(([rR]|[gG]|[bB])\s*=\s*)?(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(,?)(\s*)",
            value,
        )
        rgb = dict()
        left = list()
        for a in result:
            string = re.search(
                r"[rR]|[gG]|[bB]",
                a.group(),
            )
            number = re.search(
                r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])",
                a.group(),
            )
            number = int(number.group())
            if string is not None:
                _lower = string.group().lower()
                rgb.setdefault(_lower, number)
            else:
                left.append(number)

        if len(rgb) + len(left) != 3:
            raise ValueError(
                "rgb string is invalid value. "
                f"\"R=255,G=255,B=255\".now {value}"
            )
        for i in left:
            for colour in "rgb":
                if colour in rgb.keys():
                    continue
                rgb.setdefault(colour, i)
                break

        RGB._rgb_dict(rgb)

    @staticmethod
    def _rgb_dict(value):
        keys = list(set(value.keys()))
        lower_keys = dict()
        for key in keys:
            if not isinstance(key, str):
                raise TypeError(
                    "RGB dict key must be str type."
                )
            if not isinstance(value[key], int):
                raise TypeError(
                    "RGB dict value must be int type. "
                    f"now {type(value[key])}"
                )
            number = RGB._valid_value(value[keys])
            lower_keys[key.lower()] = number

        if len(lower_keys) != 3:
            raise ValueError(
                "rgb dict keys must be 'R', 'G', 'B'. "
                f"now {list(value.keys())}."
            )
        self._r = lower_keys["r"]
        self._g = lower_keys["g"]
        self._b = lower_keys["b"]

    @staticmethod
    def _rgb_list(value):
        if len(value) != 3:
            raise ValueError(
                "rgb list must be [R, G, B]. "
                f"now {value}"
            )
        self._r = self._valid_value(value[0])
        self._g = self._valid_value(value[1])
        self._b = self._valid_value(value[2])
    
    @staticmethod
    def _valid_value(number):
        if number > 255 or number < 0:
            raise ValueError(
                "rgb must be 0~255."
            )
        return number
        

    def __str__(self):
        return "rgb"

    def __call__(self):
        return f"\033[{self.where};2;{self._r}:{self._g}:{self._b}"

