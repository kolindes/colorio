from ._colorizer import _Colorizer

COLORS = ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'light_black',
          'light_red', 'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan', 'light_white']


class ColorStr(str):
    __slots__ = ('_colorizer',
                 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'light_black',
                 'light_red', 'light_green', 'light_yellow', 'light_blue', 'light_magenta', 'light_cyan', 'light_white')

    def __init__(self, s):
        """
        usage text = String(any)
            Examples: text.red, text.yellow, text.lightyellow
        """
        super().__init__()
        self._colorizer = _Colorizer()
        self + str(s)

    def __getattr__(self, color: str):
        return self._colorizer(self, color)
