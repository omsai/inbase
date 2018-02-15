# InBase

[![Build Status](https://travis-ci.org/omsai/inbase.svg?branch=master)](https://travis-ci.org/omsai/inbase)
[![Coverage](https://codecov.io/gh/omsai/inbase/graphs/badge.svg)](https://codecov.io/gh/omsai/inbase)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

InBase provides a convenient pandas DataFrame of the 585 inteins in
the unmaintained [inteins.com](http://inteins.com) InBase database.
The protein sequences are available as biopython SeqRecord objects,
but otherwise nothing else is changed from the inteins.com metadata.

InBase was collected using [scrapy](https://scrapy.org) and can
updated as detailed in the "update database" section below.

# Installation

    pip install --user git+https://github.com/omsai/inbase

# Usage

``` python
from inbase import INBASE

# See first few lines of all inteins.
INBASE.head()
# See first intein.
INBASE.ix[0]
# Access biopython seq record information of first intein.
INBASE.ix[0, 'Intein aa Sequence']
# Count archea inteins.
INBASE['Domain of Life'].unique()
(INBASE['Domain of Life'] == 'Archaea').sum()
# Count all inteins.
len(INBASE)
```

# Development Environment

Virtual environments and tests are orchestrated using `tox`.  Install
`tox` using `pip`:

    pip install --user tox

Make sure that `~/.local/bin` or similar is in your path per
[PEP 370](https://www.python.org/dev/peps/pep-0370/).

Install without tests:

    tox --notest -e py27

# Update DataBase

Unfortunately `scrapy` does not provide an update function to check
against the existing JSON data.  One has to redownload the database,
but which only takes a few seconds.  First, you will need to clone
this repository and create a "development environment" as described in
the section above.  Then initialize the data environment with the
`scrapy` extras package:

    tox --notest -e data

Check the current number of inbase records:

    cat data/inbase.json | wc -l | xargs expr -2 +

Redownload the data:

    rm data/inbase.json
    .tox/data/bin/scrapy runspider -o data/inbase.json inbase/update.py

Check the new number of records:

    cat data/inbase.json | wc -l | xargs expr -2 +

If there indeed are more records, update your Manifest checksums,
re-run the data tests and update your git repository and submit a pull
request:

    version=$(date +%Y%m%d.1)
    sed -i -E "s#(version=').*('.+)#\1${version}\2#" setup.py
    .tox/data/bin/gemato create --hashes "MD5 SHA1 SHA256" data/
    tox -e data
    git commit setup.py data/* -m "MAINT: Update inbase database on $(date -I)"
	git push

# Tests

Run all non-data tests using:

    tox

Debug failing tests:

    tox --pdb

If you add dependencies and get import errors, you need to recreate
the tox environment:

    tox --recreate

When you edit the files, you're likely going to create lots of linter
errors caught by the tox unit tests if your text editor doesn't have
interactive error reporting.  If you use Emacs, you can configure it
for python development by installing
[elpy](https://github.com/jorgenschaefer/elpy).
