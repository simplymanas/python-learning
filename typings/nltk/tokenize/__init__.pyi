"""
This type stub file was generated by pyright.
"""

import re
from nltk.data import load
from nltk.tokenize.casual import TweetTokenizer, casual_tokenize
from nltk.tokenize.mwe import MWETokenizer
from nltk.tokenize.punkt import PunktSentenceTokenizer
from nltk.tokenize.regexp import BlanklineTokenizer, RegexpTokenizer, WhitespaceTokenizer, WordPunctTokenizer, blankline_tokenize, regexp_tokenize, wordpunct_tokenize
from nltk.tokenize.repp import ReppTokenizer
from nltk.tokenize.sexpr import SExprTokenizer, sexpr_tokenize
from nltk.tokenize.simple import LineTokenizer, SpaceTokenizer, TabTokenizer, line_tokenize
from nltk.tokenize.texttiling import TextTilingTokenizer
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.tokenize.treebank import TreebankWordTokenizer
from nltk.tokenize.util import regexp_span_tokenize, string_span_tokenize
from nltk.tokenize.stanford_segmenter import StanfordSegmenter
from nltk.tokenize.sonority_sequencing import SyllableTokenizer

r"""
NLTK Tokenizer Package

Tokenizers divide strings into lists of substrings.  For example,
tokenizers can be used to find the words and punctuation in a string:

    >>> from nltk.tokenize import word_tokenize
    >>> s = '''Good muffins cost $3.88\nin New York.  Please buy me
    ... two of them.\n\nThanks.'''
    >>> word_tokenize(s)
    ['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York', '.',
    'Please', 'buy', 'me', 'two', 'of', 'them', '.', 'Thanks', '.']

This particular tokenizer requires the Punkt sentence tokenization
models to be installed. NLTK also provides a simpler,
regular-expression based tokenizer, which splits text on whitespace
and punctuation:

    >>> from nltk.tokenize import wordpunct_tokenize
    >>> wordpunct_tokenize(s)
    ['Good', 'muffins', 'cost', '$', '3', '.', '88', 'in', 'New', 'York', '.',
    'Please', 'buy', 'me', 'two', 'of', 'them', '.', 'Thanks', '.']

We can also operate at the level of sentences, using the sentence
tokenizer directly as follows:

    >>> from nltk.tokenize import sent_tokenize, word_tokenize
    >>> sent_tokenize(s)
    ['Good muffins cost $3.88\nin New York.', 'Please buy me\ntwo of them.', 'Thanks.']
    >>> [word_tokenize(t) for t in sent_tokenize(s)]
    [['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York', '.'],
    ['Please', 'buy', 'me', 'two', 'of', 'them', '.'], ['Thanks', '.']]

Caution: when tokenizing a Unicode string, make sure you are not
using an encoded version of the string (it may be necessary to
decode it first, e.g. with ``s.decode("utf8")``.

NLTK tokenizers can produce token-spans, represented as tuples of integers
having the same semantics as string slices, to support efficient comparison
of tokenizers.  (These methods are implemented as generators.)

    >>> from nltk.tokenize import WhitespaceTokenizer
    >>> list(WhitespaceTokenizer().span_tokenize(s))
    [(0, 4), (5, 12), (13, 17), (18, 23), (24, 26), (27, 30), (31, 36), (38, 44),
    (45, 48), (49, 51), (52, 55), (56, 58), (59, 64), (66, 73)]

There are numerous ways to tokenize text.  If you need more control over
tokenization, see the other methods provided in this package.

For further information, please see Chapter 3 of the NLTK book.
"""
def sent_tokenize(text, language=...):
    """
    Return a sentence-tokenized copy of *text*,
    using NLTK's recommended sentence tokenizer
    (currently :class:`.PunktSentenceTokenizer`
    for the specified language).

    :param text: text to split into sentences
    :param language: the model name in the Punkt corpus
    """
    ...

_treebank_word_tokenizer = TreebankWordTokenizer()
improved_open_quote_regex = re.compile(u'([«“‘„]|[`]+)', re.U)
improved_open_single_quote_regex = re.compile(r"(?i)(\')(?!re|ve|ll|m|t|s|d)(\w)\b", re.U)
improved_close_quote_regex = re.compile(u'([»”’])', re.U)
improved_punct_regex = re.compile(r'([^\.])(\.)([\]\)}>"\'' u'»”’ ' r']*)\s*$', re.U)
def word_tokenize(text, language=..., preserve_line: bool = ...):
    """
    Return a tokenized copy of *text*,
    using NLTK's recommended word tokenizer
    (currently an improved :class:`.TreebankWordTokenizer`
    along with :class:`.PunktSentenceTokenizer`
    for the specified language).

    :param text: text to split into words
    :type text: str
    :param language: the model name in the Punkt corpus
    :type language: str
    :param preserve_line: An option to keep the preserve the sentence and not sentence tokenize it.
    :type preserve_line: bool
    """
    ...

