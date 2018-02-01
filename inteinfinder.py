# Released into the Public Domain:
# https://creativecommons.org/publicdomain/zero/1.0/legalcode

"""Detect putative inteins."""

# Standard library imports.
import pkg_resources

# 3rdparty imports.
from Bio import SeqIO
from Bio.Alphabet.IUPAC import extended_protein


# Load known inteins during package startup.
_FILE_FASTA = pkg_resources.resource_filename('inteinfinder',
                                              'data/inbase_fasta.txt')
INTEINS_KNOWN = list(SeqIO.parse(_FILE_FASTA, "fasta"))
for record in INTEINS_KNOWN:
    record.seq.alphabet = extended_protein
