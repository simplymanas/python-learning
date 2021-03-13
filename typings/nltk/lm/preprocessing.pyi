"""
This type stub file was generated by pyright.
"""

from functools import partial
from itertools import chain
from nltk.util import pad_sequence

flatten = chain.from_iterable
pad_both_ends = partial(pad_sequence, pad_left=True, left_pad_symbol="<s>", pad_right=True, right_pad_symbol="</s>")
def padded_everygrams(order, sentence):
    """Helper with some useful defaults.

    Applies pad_both_ends to sentence and follows it up with everygrams.
    """
    ...

def padded_everygram_pipeline(order, text):
    """Default preprocessing for a sequence of sentences.

    Creates two iterators:
    - sentences padded and turned into sequences of `nltk.util.everygrams`
    - sentences padded as above and chained together for a flat stream of words

    :param order: Largest ngram length produced by `everygrams`.
    :param text: Text to iterate over. Expected to be an iterable of sentences:
    Iterable[Iterable[str]]
    :return: iterator over text as ngrams, iterator over text as vocabulary data
    """
    ...

