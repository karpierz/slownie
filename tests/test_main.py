# Copyright (c) 2016 Adam Karpierz
# SPDX-License-Identifier: Zlib

import unittest

import slownie
from slownie import slownie, slownie_zl, slownie_zl100gr


class SlownieTestCase(unittest.TestCase):

    def test_slownie(self):
        self.assertEqual(slownie(0), "zero")
        self.assertEqual(slownie(1), "jeden")
        self.assertEqual(slownie(-1), "minus jeden")
        self.assertEqual(slownie(12892), "dwanaście tysięcy osiemset dziewięćdziesiąt dwa")

    def test_slownie_zl(self):
        self.assertEqual(slownie_zl(0), "zero złotych")
        self.assertEqual(slownie_zl100gr(0), "zero złotych 00/100")
        self.assertEqual(slownie_zl(1), "jeden złoty")
        self.assertEqual(slownie_zl100gr(1), "jeden złoty 00/100")
        self.assertEqual(slownie_zl(11), "jedenaście złotych")
        self.assertEqual(slownie_zl100gr(11), "jedenaście złotych 00/100")
        self.assertEqual(slownie_zl(123), "sto dwadzieścia trzy złote")
        self.assertEqual(slownie_zl100gr(123), "sto dwadzieścia trzy złote 00/100")
        self.assertEqual(slownie_zl(123.34), "sto dwadzieścia trzy złote trzydzieści cztery grosze")
        self.assertEqual(slownie_zl100gr(123.34), "sto dwadzieścia trzy złote 34/100")
        self.assertEqual(slownie_zl(123.34, "i"), "sto dwadzieścia trzy złote i trzydzieści cztery grosze")
        self.assertEqual(slownie_zl(123.34, " i "), "sto dwadzieścia trzy złote i trzydzieści cztery grosze")
