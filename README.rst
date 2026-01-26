slownie
=======

Polish spelled-out numbers and amounts.

Overview
========

Provides routines to spell out numbers and amounts in Polish.

| **slownie(value)**
| **slownie_zl(amount)**
| **slownie_zl100gr(amount)**

`PyPI record`_.

`Documentation`_.

Usage
-----

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

+ Python 3.10 or higher

  * https://www.python.org/

+ pip

  * https://pypi.org/project/pip/

To install run:

  .. parsed-literal::

    python -m pip install --upgrade |package|

Development
===========

Prerequisites:

+ Development is strictly based on *nox*. To install it run::

    python -m pip install --upgrade nox

Visit `Development page`_.

Installation from sources:

clone the sources:

  .. parsed-literal::

    git clone |respository| |package|

and run:

  .. parsed-literal::

    python -m pip install ./|package|

or on development mode:

  .. parsed-literal::

    python -m pip install --editable ./|package|

License
=======

  | |copyright|
  | Licensed under the zlib/libpng License
  | https://opensource.org/license/zlib
  | Please refer to the accompanying LICENSE file.

Authors
=======

* Adam Karpierz <adam@karpierz.net>

Sponsoring
==========

| If you would like to sponsor the development of this project, your contribution
  is greatly appreciated.
| As I am now retired, any support helps me dedicate more time to maintaining and
  improving this work.

`Donate`_

.. |package| replace:: slownie
.. |package_bold| replace:: **slownie**
.. |copyright| replace:: Copyright (c) 2016-2026 Adam Karpierz
.. |respository| replace:: https://github.com/karpierz/slownie
.. _Development page: https://github.com/karpierz/slownie
.. _PyPI record: https://pypi.org/project/slownie/
.. _Documentation: https://karpierz.github.io/slownie/
.. _Donate: https://www.paypal.com/donate/?hosted_button_id=FX8L7CJUGLW7S
