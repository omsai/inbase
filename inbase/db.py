# Released into the Public Domain:
# https://creativecommons.org/publicdomain/zero/1.0/legalcode

"""Cache inteins.com InBase database locally as Pandas DataFrame."""

# Standard library imports.
import io
import os
import pkg_resources

# 3rdparty imports.
from Bio import SeqIO
from Bio.Alphabet.IUPAC import extended_protein
import pandas as pd


def str_to_protein(seq_string):
    """Convert AA strings into BioPython Seq objects."""
    fh = io.StringIO(seq_string)
    seq_record = list(SeqIO.parse(fh, "fasta"))[0]
    seq_record.seq.alphabet = extended_protein
    return seq_record


# Load inbase during package startup.
_FILE_JSON = pkg_resources.resource_filename(__name__, 'data/inbase.json')
if not os.path.exists(_FILE_JSON):  # pragma: no cover
    # Pandas doesn't give an informative error if you ask it to read a
    # non-existant file.
    raise IOError(('Package was not installed correctly.  '
                   'Cannot find database file %s' % _FILE_JSON))
INBASE = pd.read_json(_FILE_JSON)
INBASE['Intein aa Sequence'] = INBASE['Intein aa Sequence'].map(str_to_protein)
