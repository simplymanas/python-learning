"""
This type stub file was generated by pyright.
"""

from collections import defaultdict

"""
Interface for converting POS tags from various treebanks
to the universal tagset of Petrov, Das, & McDonald.

The tagset consists of the following 12 coarse tags:

VERB - verbs (all tenses and modes)
NOUN - nouns (common and proper)
PRON - pronouns
ADJ - adjectives
ADV - adverbs
ADP - adpositions (prepositions and postpositions)
CONJ - conjunctions
DET - determiners
NUM - cardinal numbers
PRT - particles or other function words
X - other: foreign words, typos, abbreviations
. - punctuation

@see: http://arxiv.org/abs/1104.2086 and http://code.google.com/p/universal-pos-tags/

"""
_UNIVERSAL_DATA = "taggers/universal_tagset"
_UNIVERSAL_TAGS = ('VERB', 'NOUN', 'PRON', 'ADJ', 'ADV', 'ADP', 'CONJ', 'DET', 'NUM', 'PRT', 'X', '.')
_MAPPINGS = defaultdict(lambda : defaultdict(lambda : defaultdict(lambda : 'UNK')))
def _load_universal_map(fileid):
    ...

def tagset_mapping(source, target):
    """
    Retrieve the mapping dictionary between tagsets.

    >>> tagset_mapping('ru-rnc', 'universal') == {'!': '.', 'A': 'ADJ', 'C': 'CONJ', 'AD': 'ADV',\
            'NN': 'NOUN', 'VG': 'VERB', 'COMP': 'CONJ', 'NC': 'NUM', 'VP': 'VERB', 'P': 'ADP',\
            'IJ': 'X', 'V': 'VERB', 'Z': 'X', 'VI': 'VERB', 'YES_NO_SENT': 'X', 'PTCL': 'PRT'}
    True
    """
    ...

def map_tag(source, target, source_tag):
    """
    Maps the tag from the source tagset to the target tagset.

    >>> map_tag('en-ptb', 'universal', 'VBZ')
    'VERB'
    >>> map_tag('en-ptb', 'universal', 'VBP')
    'VERB'
    >>> map_tag('en-ptb', 'universal', '``')
    '.'
    """
    ...

