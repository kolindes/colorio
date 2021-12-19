# Copyright ANS BSD 3-Clause license, see LICENSE file.

from typing import Tuple

from ._color_string import ColorStr
from .io import ri


def colorize(v) -> ColorStr:
    """
        :param v: string

        :return: a ColorStr

        usage examples:

        -- text.yellow,

        -- text.lightyellow,

        -- text.light_yellow

        """
    return ColorStr(v)


def inp(hint: str, color: str = 'light_cyan', min_length: int = 0, max_length: int = 0, custom_err: str = '') -> any:
    return ri(getattr(ColorStr(hint), color), min_length, max_length, custom_err)


def paint(*v, color: str = 'white') -> Tuple[any]:
    return tuple(getattr(colorize(i), color) for i in v)


def paint_bool(b: bool) -> str:
    clr = colorize(b)
    return clr.lightgreen if b else clr.red


def str_bool_based(positive: str, negative: str, b: bool) -> str:
    """

    :param positive: positive choice (light_green)

    :param negative: negative choice (light_red)

    :param b: bool True/False

    :return: a string positive/negative choice

    """
    return colorize(positive).light_green if b else colorize(negative).light_red
