# Copyright (c) 2016-2022 Adam Karpierz
# Licensed under the zlib/libpng License
# https://opensource.org/licenses/Zlib

import math

__all__ = ('slownie', 'slownie_zl', 'slownie_zl100gr')


ZERO_LITERALLY = "zero"

MINUS_LITERALLY = "minus "

HUNDREDS_LITERALLY = [
    "",
    "sto ",
    "dwie\u015Bcie ",
    "trzysta ",
    "czterysta ",
    "pi\u0119\u0107set ",
    "sze\u015B\u0107set ",
    "siedemset ",
    "osiemset ",
    "dziewi\u0119\u0107set "
]

TENS_LITERALLY = [
    "",
    "",
    "dwadzie\u015Bcia ",
    "trzydzie\u015Bci ",
    "czterdzie\u015Bci ",
    "pi\u0119\u0107dziesi\u0105t ",
    "sze\u015B\u0107dziesi\u0105t ",
    "siedemdziesi\u0105t ",
    "osiemdziesi\u0105t ",
    "dziewi\u0119\u0107dziesi\u0105t "
]

UNITIES_LITERALLY = [
    "",
    "jeden ",
    "dwa ",
    "trzy ",
    "cztery ",
    "pi\u0119\u0107 ",
    "sze\u015B\u0107 ",
    "siedem ",
    "osiem ",
    "dziewi\u0119\u0107 ",
    "dziesi\u0119\u0107 ",
    "jedena\u015Bcie ",
    "dwana\u015Bcie ",
    "trzyna\u015Bcie ",
    "czterna\u015Bcie ",
    "pi\u0119tna\u015Bcie ",
    "szesna\u015Bcie ",
    "siedemna\u015Bcie ",
    "osiemna\u015Bcie ",
    "dziewi\u0119tna\u015Bcie "
]

PARTS_LITERALLY = [
    ["", "",             "",              ""],
    ["", "tysi\u0105c ", "tysi\u0105ce ", "tysi\u0119cy "],
    ["", "milion ",      "miliony ",      "milion\u00F3w "],
    ["", "miliard ",     "miliardy ",     "miliard\u00F3w "],
    ["", "bilion ",      "biliony ",      "bilion\u00F3w "],
    ["", "biliard ",     "biliardy ",     "biliard\u00F3w "],
    ["", "trylion ",     "tryliony ",     "trylion\u00F3w "],
    ["", "tryliard ",    "tryliardy ",    "tryliard\u00F3w "],
    ["", "kwadrylion ",  "kwadryliony ",  "kwadrylion\u00F3w "],
    ["", "kwadryliard ", "kwadryliardy ", "kwadryliard\u00F3w "],
]

GROSZE_LITERALLY = [
    " groszy",
    " grosz",
    " grosze",
    " groszy"
]

ZLOTE_LITERALLY = [
    " z\u0142otych",
    " z\u0142oty",
    " z\u0142ote",
    " z\u0142otych"
]


def slownie(value):
    """ """
    if value == 0.0:
        return ZERO_LITERALLY

    literally = "" if value >= 0.0 else (MINUS_LITERALLY + " ")

    value = abs(value)

    for k in range(len(PARTS_LITERALLY) - 1, -1, -1):
        part = int((value % 1000.0**(k + 1)) / 1000.0**k)
        hundreds, tens, unities, declension = _split(part)
        literally += HUNDREDS_LITERALLY[hundreds]
        literally += TENS_LITERALLY[tens]
        literally += UNITIES_LITERALLY[unities]
        literally += PARTS_LITERALLY[k][declension]

    return literally[:-1]


def slownie_zl(amount):
    """ """
    grosze, zlote = math.modf(amount)
    grosze = int(abs(grosze) * 100.0 + 0.5)

    literally = _slownie(zlote, ZLOTE_LITERALLY)
    if grosze:
        literally += " "
        literally += _slownie(grosze, GROSZE_LITERALLY)

    return literally


def slownie_zl100gr(amount):
    """ """
    grosze, zlote = math.modf(amount)
    grosze = int(abs(grosze) * 100.0 + 0.5)

    literally = _slownie(zlote, ZLOTE_LITERALLY)
    literally += " %02d/100" % grosze

    return literally


def _slownie(amount, LITERALLY):
    literally = slownie(amount)
    amount = int(abs(amount) + 0.5)
    _, _, _, declension = _split(amount)
    literally += LITERALLY[declension]
    return literally


def _split(value):
    hundreds, rest = divmod(value, 100)
    tens, unities  = divmod(rest, 10)
    if tens == 1: tens, unities = 0, rest
    if unities == 0:
        declension = 3 if hundreds or tens else 0
    elif unities == 1:
        declension = 3 if hundreds or tens else 1
    elif unities in (2, 3, 4):
        declension = 2
    else:  # unities >= 5:
        declension = 3
    return (hundreds, tens, unities, declension)
