# Released into the Public Domain:
# https://creativecommons.org/publicdomain/zero/1.0/legalcode

"""Unit tests for inbase."""

# Package imports.
from inbase import INBASE
from inbase.db import extended_protein


def test_inbase_db_is_read_as_proteins():
    assert all(INBASE['Intein aa Sequence'].apply(lambda x: x.seq.alphabet)
               == extended_protein)
