========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-genesiscreator/badge/?style=flat
    :target: https://readthedocs.org/projects/python-genesiscreator
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/ahmedbodi/python-genesiscreator.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ahmedbodi/python-genesiscreator

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ahmedbodi/python-genesiscreator?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ahmedbodi/python-genesiscreator

.. |requires| image:: https://requires.io/github/ahmedbodi/python-genesiscreator/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ahmedbodi/python-genesiscreator/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/ahmedbodi/python-genesiscreator/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ahmedbodi/python-genesiscreator

.. |version| image:: https://img.shields.io/pypi/v/genesiscreator.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/genesiscreator

.. |commits-since| image:: https://img.shields.io/github/commits-since/ahmedbodi/python-genesiscreator/v0.2.0.svg
    :alt: Commits since latest release
    :target: https://github.com/ahmedbodi/python-genesiscreator/compare/v0.2.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/genesiscreator.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/genesiscreator

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/genesiscreator.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/genesiscreator

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/genesiscreator.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/genesiscreator


.. end-badges

A Crypto-Currency Genesis Block Creator

* Free software: BSD 3-Clause License

Installation
============

::

    pip install genesiscreator

Documentation
=============

https://python-genesiscreator.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
