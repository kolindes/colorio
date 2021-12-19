# Copyright ANS BSD 3-Clause license, see LICENSE file.

from typing import Optional


def ri(hint: str, min_length: int = 0, max_length: int = 0, custom_error: str = '') -> Optional[any]:

    if not hint.endswith('>'):
        hint += '>'

    assert min_length <= max_length, f'{min_length}<={max_length}'

    _inp = input(hint)

    if min_length != max_length != 0:
        inp_len = len(_inp)
        assert inp_len in range(min_length, max_length), \
            f'[{inp_len}] out of ({min_length}, {max_length}) range\n{custom_error}'

    return _inp


def typed_inp(_t: type, hint: str, custom_error: str = '', looped: bool = False) -> Optional[any]:
    """
        _t: type int/float/bool...

        return example int(input(hint)) -> int(user_input)
    """
    if not hint.endswith('>'):
        hint += '>'

    def _ti():
        _inp = ri(hint, custom_error=custom_error)
        try:
            if _t is bool:
                assert _inp == 'True' or _inp == 'False', 'bool - True/False accepted only'
            return _t(eval(_inp.title()))
        except (ValueError, NameError, SyntaxError):
            print(f'Value "{_inp}" cannot be converted into "{_t.__name__}" type.')
            if custom_error:
                print(custom_error)

    if looped:
        while True:
            r = _ti()
            if r:
                return r
    else:
        return _ti()


def input_int(s: str = '>', custom_error: str = '') -> int:
    return typed_inp(int, s, custom_error)


def input_float(s: str = '>', custom_error: str = '') -> float:
    return typed_inp(float, s, custom_error)


def input_bool(s: str = '>', custom_error: str = '') -> bool:
    return typed_inp(bool, s, custom_error)


def confirm(hint: str = '', positive_sign: str = 'y', negative_sign: str = 'n') -> bool:
    """
        [y/n]> y >> True

        :param hint: any text

        :param positive_sign: default -- y

        :param negative_sign: default -- n

        :return: True/False (bool)

    """
    _inp = ri(f'{hint}[{positive_sign}/{negative_sign}]> ')
    return _inp == positive_sign
