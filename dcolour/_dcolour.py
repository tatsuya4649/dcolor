from .mode import ColourMode
from .where import ColourWhere

def color(
    colour,
    mode=ColourMode.NAME.value,
):
    _colour = Color(
        colour=colour,
        mode=mode,
        where=ColourWhere.CHARACTER,
    )
    pass

def background(
):
    pass

def attribute(
):
    pass
