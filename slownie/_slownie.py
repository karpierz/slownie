# Copyright (c) 2016-2018 Adam Karpierz
# Licensed under the zlib/libpng License
# http://opensource.org/licenses/zlib

from __future__ import absolute_import

import math

__all__ = ('slownie', 'slownie_zl', 'slownie_zl100gr')


ZERO_LITERALLY = u"zero"

MINUS_LITERALLY = u"minus "

HUNDREDS_LITERALLY = [
    u"",
    u"sto ",
    u"dwie\u015Bcie ",
    u"trzysta ",
    u"czterysta ",
    u"pi\u0119\u0107set ",
    u"sze\u015B\u0107set ",
    u"siedemset ",
    u"osiemset ",
    u"dziewi\u0119\u0107set "
]

TENS_LITERALLY = [
    u"",
    u"",
    u"dwadzie\u015Bcia ",
    u"trzydzie\u015Bci ",
    u"czterdzie\u015Bci ",
    u"pi\u0119\u0107dziesi\u0105t ",
    u"sze\u015B\u0107dziesi\u0105t ",
    u"siedemdziesi\u0105t ",
    u"osiemdziesi\u0105t ",
    u"dziewi\u0119\u0107dziesi\u0105t "
]

UNITIES_LITERALLY = [
    u"",
    u"jeden ",
    u"dwa ",
    u"trzy ",
    u"cztery ",
    u"pi\u0119\u0107 ",
    u"sze\u015B\u0107 ",
    u"siedem ",
    u"osiem ",
    u"dziewi\u0119\u0107 ",
    u"dziesi\u0119\u0107 ",
    u"jedena\u015Bcie ",
    u"dwana\u015Bcie ",
    u"trzyna\u015Bcie ",
    u"czterna\u015Bcie ",
    u"pi\u0119tna\u015Bcie ",
    u"szesna\u015Bcie ",
    u"siedemna\u015Bcie ",
    u"osiemna\u015Bcie ",
    u"dziewi\u0119tna\u015Bcie "
]

PARTS_LITERALLY = [
    [u"", u"",             u"",              u""],
    [u"", u"tysi\u0105c ", u"tysi\u0105ce ", u"tysi\u0119cy "],
    [u"", u"milion ",      u"miliony ",      u"milion\u00F3w "],
    [u"", u"miliard ",     u"miliardy ",     u"miliard\u00F3w "],
    [u"", u"bilion ",      u"biliony ",      u"bilion\u00F3w "],
    [u"", u"biliard ",     u"biliardy ",     u"biliard\u00F3w "],
    [u"", u"trylion ",     u"tryliony ",     u"trylion\u00F3w "],
    [u"", u"tryliard ",    u"tryliardy ",    u"tryliard\u00F3w "],
    [u"", u"kwadrylion ",  u"kwadryliony ",  u"kwadrylion\u00F3w "],
    [u"", u"kwadryliard ", u"kwadryliardy ", u"kwadryliard\u00F3w "],
]


def slownie(value):

    if value == 0.0:
        return ZERO_LITERALLY

    literally = u"" if value >= 0.0 else (MINUS_LITERALLY + u" ")

    value = abs(value)

    for k in range(len(PARTS_LITERALLY) - 1, -1, -1):

        part = int((value % 1000.0**(k + 1)) / 1000.0**k)
        hundreds, rest = divmod(part, 100)
        tens, unities  = divmod(rest, 10)
        if tens == 1: tens, unities = 0, rest

        if unities == 0:
            nj = 3 if hundreds or tens else 0
        elif unities == 1:
            nj = 3 if hundreds or tens else 1
        elif unities in (2, 3, 4):
            nj = 2
        else:  # unities >= 5:
            nj = 3

        literally += HUNDREDS_LITERALLY[hundreds]
        literally += TENS_LITERALLY[tens]
        literally += UNITIES_LITERALLY[unities]
        literally += PARTS_LITERALLY[k][nj]

    return literally[:-1]


def slownie_zl(amount):

    grosze, zlote = math.modf(amount)
    grosze = int(abs(grosze) * 100.0 + 0.5)

    literally = slownie_zl100gr(zlote)

    if grosze:
        literally += u" "
        literally += slownie(grosze)
        groszy = int(math.modf(grosze / 10.0)[0] * 10.0 + 0.5)
        literally += u" "
        if grosze == 1:
            literally += u"grosz"
        elif groszy in (2, 3, 4):
            literally += u"grosze"
        else:
            literally += u"groszy"

    return literally


def slownie_zl100gr(amount):

    grosze, zlote = math.modf(amount)
    grosze = int(abs(grosze) * 100.0 + 0.5)

    literally = slownie(zlote)
    zlotych = int(abs(math.modf(zlote / 10.0)[0]) * 10.0 + 0.5)
    literally += u" "
    if zlote == 1.0:
        literally += u"z\u0142oty"
    elif zlotych in (2, 3, 4):
        literally += u"z\u0142ote"
    else:
        literally += u"z\u0142otych"

    if grosze:
        literally += u" "
        literally += str(grosze)
        literally += u"/100"

    return literally
