# Released into the Public Domain:
# https://creativecommons.org/publicdomain/zero/1.0/legalcode

"""Detect putative inteins."""

import sys
from setuptools import find_packages, setup


# Boilerplate for pytest-runner suggested by pypi page.
NEEDS_PYTEST = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
# Also add pytest itself because it is a runtime dependency of pytest-runner.
PYTEST_RUNNER = ['pytest-runner', 'pytest'] if NEEDS_PYTEST else []

setup(
    name="inteinfinder",
    version="0.1.dev1",
    description=__doc__,
    author="Pariksheet Nanda",
    author_email="pariksheet.nanda@uconn.edu",
    packages=find_packages(),
    setup_requires=PYTEST_RUNNER,
    install_requires=[
        'biopython',
        'scrapy',
    ],
    tests_require=[
        'pytest',               # Test suite.
        'pytest-cov',           # `coverage` wrapper.
        'pytest-pylint',        # `pylint` wrapper.
    ],
    # Data was downloaded from:
    # http://www.biocenter.helsinki.fi/bi/iwai/InBase/tools.neb.com/inbase/inbase_fasta.txt
    data_files=[
        'data/inbase_fasta.txt',
        'data/inbase.json',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    url='https://github.com/omsai/inteinfinder',
)
