from colorama.ansi import AnsiFore, Fore

from .exceptions import InvalidColorName


class _Colorizer(AnsiFore):
    def __getattr__(self, item: str):
        if item.startswith('light') and '_' in item:
            item = item.replace('_', '')
        return getattr(Fore, item.upper() + ('_EX' if item.startswith('light') else ''))

    def __call__(self, s: str, color: str):
        if not hasattr(self, color):
            raise InvalidColorName(color)
        return getattr(self, color) + s + getattr(self, 'WHITE')
