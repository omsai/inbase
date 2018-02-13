# Intein finder

[![Build Status](https://travis-ci.org/omsai/inteinfinder.svg?branch=master)](https://travis-ci.org/omsai/inteinfinder)
[![Coverage](https://codecov.io/gh/omsai/inteinfinder/graphs/badge.svg)](https://codecov.io/gh/omsai/inteinfinder)

Intein finder uses the intein database, InBase, to detect putative
inteins in your favorite genome.

# Testing

Virtual environments and tests are orchestrated using `tox`.  Install
`tox` using `pip`:

    pip install --user tox

Make sure that `~/.local/bin` or similar is in your path per
[PEP 370](https://www.python.org/dev/peps/pep-0370/).

Install without tests:

    tox --develop --notest

Test:

    tox --develop

Debug failing tests:

    tox --develop -- --pdb

If you add dependencies and get import errors, you need to recreate
the tox environment:

    tox --recreate --develop

When you edit the files, you're likely going to create lots of linter
errors caught by the tox unit tests if your text editor doesn't have
interactive error reporting.  If you use Emacs, you can configure it
for python development by installing
[elpy](https://github.com/jorgenschaefer/elpy).
