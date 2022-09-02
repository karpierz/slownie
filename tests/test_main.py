# Copyright (c) 2016-2022 Adam Karpierz
# Licensed under the zlib/libpng License
# https://opensource.org/licenses/Zlib

import unittest

from slownie import slownie, slownie_zl, slownie_zl100gr


class SlownieTestCase(unittest.TestCase):

    def test_slownie(self):
        self.assertEqual(slownie(12892), "dwanaście tysięcy osiemset dziewięćdziesiąt dwa")

    def test_slownie_zl(self):
        self.assertEqual(slownie_zl(123), "sto dwadzieścia trzy złote")
        self.assertEqual(slownie_zl100gr(123), "sto dwadzieścia trzy złote 00/100")
        self.assertEqual(slownie_zl(123.34), "sto dwadzieścia trzy złote trzydzieści cztery grosze")
        self.assertEqual(slownie_zl100gr(123.34), "sto dwadzieścia trzy złote 34/100")
