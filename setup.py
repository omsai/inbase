# Released into the Public Domain:
# https://creativecommons.org/publicdomain/zero/1.0/legalcode

"""Cache inteins.com InBase database locally as Pandas DataFrame."""

import sys
from setuptools import find_packages, setup


# Boilerplate for pytest-runner suggested by pypi page.
NEEDS_PYTEST = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
# Also add pytest itself because it is a runtime dependency of pytest-runner.
PYTEST_RUNNER = ['pytest-runner', 'pytest'] if NEEDS_PYTEST else []

setup(
    name="inbase",
    version="20180212.1",
    description=__doc__,
    author="Pariksheet Nanda",
    author_email="pariksheet.nanda@uconn.edu",
    packages=find_packages(),
    setup_requires=PYTEST_RUNNER,
    install_requires=[
        'biopython',
        'pandas',
    ],
    extras_require={
        'scrapy': ['scrapy'],
    },
    tests_require=[
        'pytest',               # Test suite.
        'pytest-cov',           # `coverage` wrapper.
        'pytest-pylint',        # `pylint` wrapper.
    ],
    package_data={
        'inbase': ['data/*.json'],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Topic :: Database',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    url='https://github.com/omsai/inbase',
)
