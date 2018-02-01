# Released into the Public Domain:
# https://creativecommons.org/publicdomain/zero/1.0/legalcode

"""Unit tests for inteinfinder."""

# Package imports.
from inteinfinder import extended_protein, INTEINS_KNOWN


def test_inbase_db_is_read_as_proteins():
    assert all([record.seq.alphabet == extended_protein
                for record in INTEINS_KNOWN])
