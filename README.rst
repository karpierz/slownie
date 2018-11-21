slownie
=======

Polish spelled-out numbers and amounts.

Overview
========

| **slownie(value):** 
| **slownie_zl(amount):** 
| **slownie_zl100gr(amount):** 

  | Provides routines to spell out numbers and amounts in Polish.

.. code:: python

  >>> from slownie import *
  >>> slownie(12892)
  dwanaście tysięcy osiemset dziewięćdziesiąt dwa
  >>> slownie_zl(123.34)
  sto dwadzieścia trzy złote trzydzieści cztery grosze
  >>> slownie_zl100gr(123.34)
  sto dwadzieścia trzy złote 34/100

Installation
============

Prerequisites:

+ Python 2.7 or higher or 3.4 or higher

  * http://www.python.org/
  * 2.7 and 3.6 are primary test environments.

+ pip and setuptools

  * http://pypi.python.org/pypi/pip
  * http://pypi.python.org/pypi/setuptools

To install run::

    python -m pip install --upgrade slownie

Development
===========

Visit `development page <https://github.com/karpierz/slownie>`__

Installation from sources:

Clone the `sources <https://github.com/karpierz/slownie>`__ and run::

    python -m pip install ./slownie

or on development mode::

    python -m pip install --editable ./slownie

Prerequisites:

+ Development is strictly based on *tox*. To install it run::

    python -m pip install tox

License
=======

  | Copyright (c) 2016-2018 Adam Karpierz
  |
  | Licensed under the zlib/libpng License
  | http://opensource.org/licenses/zlib
  | Please refer to the accompanying LICENSE file.

Authors
=======

* Adam Karpierz <adam@karpierz.net>
