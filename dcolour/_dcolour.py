from .where import ColourWhere
from .mode import ColourMode
from .colour import Colour
from .attr import Attr, AttrList


def _colour(
    colour,
    mode=ColourMode.NAME.value(),
):
    _colour = Colour(
        colour=colour,
        mode=mode,
        where=ColourWhere.CHARACTER,
    )
    return _colour

def _check_string(value):
    if not isinstance(value, str):
        raise TypeError(
            "must be string"
        )
    return value

def colours(
    string,
    colour,
    mode=ColourMode.NAME.value(),
):
    _cins = _colour(
        colour=colour,
        mode=mode,
    )
    return (
        _cins.start() + \
        _check_string(string) + \
        _cins.end()
    )


def _background(
    colour,
    mode=ColourMode.NAME.value(),
):
    _colour = Colour(
        colour=colour,
        mode=mode,
        where=ColourWhere.BACKGROUND,
    )
    return _colour


def backgrounds(
    string,
    colour,
    mode=ColourMode.NAME.value(),
):
    _cins = _background(
        colour=colour,
        mode=mode,
    )
    return (
        _cins.start() + \
        _check_string(string) + \
        _cins.end()
    )


def attributes(
    string,
    attr,
):
    _attr = Attr(
        kind=attr,
    )
    return (
        _attr.start() + \
        _check_string(string) + \
        _attr.end()
    )
