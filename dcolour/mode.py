from enum import Enum
from .cm import CMMember
from .name import Name
from .rgb import RGB
from .index import Index

class ColourMode(Enum):
    """
    how to decide specific colour 
    """
    # specify colour string
    NAME=Name
    # R=0~255, G=0~255, B=0~255
    RGB=RGB
    # 0~255
    INDEX=Index

    @staticmethod
    def _mode_str(mode):
        if not issubclass(mode.value, CMMember):
            raise TypeError(
                "mode must be subclass of CMMember."
            )
        return mode.value()

    @staticmethod
    def mode(mode):
        for _mode in ColourMode:
            if ColourMode._mode_str(_mode) == mode:
                return _mode.value
        raise ValueError(
            f"mode({mode}) is invalid value. "
            f"valid value({','.join([x.value() for x in ColourMode])})."
        )
