"""
This type stub file was generated by pyright.
"""

from nltk.compat import python_2_unicode_compatible
from typing import Any, Optional

@python_2_unicode_compatible
class WordNetLemmatizer(object):
    """
    WordNet Lemmatizer

    Lemmatize using WordNet's built-in morphy function.
    Returns the input word unchanged if it cannot be found in WordNet.

        >>> from nltk.stem import WordNetLemmatizer
        >>> wnl = WordNetLemmatizer()
        >>> print(wnl.lemmatize('dogs'))
        dog
        >>> print(wnl.lemmatize('churches'))
        church
        >>> print(wnl.lemmatize('aardwolves'))
        aardwolf
        >>> print(wnl.lemmatize('abaci'))
        abacus
        >>> print(wnl.lemmatize('hardrock'))
        hardrock
    """
    def __init__(self):
        ...
    
    def lemmatize(self, word, pos=...):
        ...
    
    def __repr__(self):
        ...
    


def teardown_module(module: Optional[Any] = ...):
    ...
