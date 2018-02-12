# Released into the Public Domain:
# https://creativecommons.org/publicdomain/zero/1.0/legalcode

"""Detect putative inteins."""

# Standard library imports.
import pkg_resources

# 3rdparty imports.
from Bio import SeqIO
from Bio.Alphabet.IUPAC import extended_protein
import scrapy


# Load known inteins during package startup.
_FILE_FASTA = pkg_resources.resource_filename('inteinfinder',
                                              'data/inbase_fasta.txt')
INTEINS_KNOWN = list(SeqIO.parse(_FILE_FASTA, "fasta"))
for record in INTEINS_KNOWN:
    record.seq.alphabet = extended_protein


class InteinSpider(scrapy.Spider):
    """Fetch complete InBase registry."""
    name = "inteins"
    start_urls = [('http://www.biocenter.helsinki.fi/'
                   'bi/iwai/InBase/tools.neb.com/inbase/list.html')]

    def parse(self, response):
        """Follow links to intein detail pages."""
        pages = (response
                 .xpath('//table[@cellspacing="5"]/tr/td/a/@href')
                 .extract())
        for next_page in pages:
            if next_page is not None:
                yield response.follow(next_page,
                                      callback=self.parse_intein_details)

    def parse_intein_details(self, response):  # pylint: disable=no-self-use
        """Parse Intein details page."""
        keys = [
            'Intein Name',
            'Prototype Allele',
            'Extein Name',
            'Intein Class',
            'Organism Name',
            'Organism Description',
            'Domain of Life',
            'Endonuclease Activity',
            'Endo Motif',
            'Location in Extein',
            'Insert Site Comments',
            'Intein Size (aa)',
            'Intein N-terminal',
            'Intein C-terminal',
            'Accession No.',
            'Intein aa Sequence',
            'Block A',
            'Block B',
            'Block C',
            'Block D',
            'Block E',
            'Block F',
            'Block G',
            'Initially Contributed by',
            "Contributor's Address",
            "Contributor's Phone No.",
            "Contributor's FAX No.",
            "Contributor's Email address",
            'Independently Found By',
            'Comments',
            'Date Submitted',
            'References',
        ]
        # If we directly use extract() on the XPath .../font/text(), scrapy
        # flattens the 'Intrein aa sequence'.
        values = [''.join(selector.xpath('text()').extract()).rstrip()
                  for selector in
                  response.xpath('//table[@cellspacing="6"]/tr/td/font')]
        yield dict(zip(keys, values))
