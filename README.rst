slownie
=======

Polish spelled-out numbers and amounts.

Overview
========

**slownie** (value):
**slownie_zl** (amount):
**slownie_zl100gr** (amount):

  | Provides routines to spell out numbers and amounts in Polish.

.. code:: python

  >>> from slownie import *
  >>> slownie(12892)
  dwanaście tysięcy osiemset dziewięćdziesiąt dwa
  >>> slownie_zl(123.34)
  sto dwadzieścia trzy złote trzydzieści cztery groszy
  >>> slownie_zl100gr(123.34)
  sto dwadzieścia trzy złote 34/100

Installation
============

::

    $ python -m pip install --upgrade slownie

Prerequisites:

+ Python 2.6 or higher

  * http://www.python.org/
  * 2.7 and 3.4 are primary test environments.

+ pip or setuptools

  * http://pypi.python.org/pypi/pip
  * http://pypi.python.org/pypi/setuptools

License
=======

  | Copyright (c) 2016-2017 Adam Karpierz
  |
  | Licensed under the zlib/libpng License
  | http://opensource.org/licenses/zlib
  | Please refer to the accompanying LICENSE file.

Authors
=======

* Adam Karpierz <python@python.pl>
