"""
This type stub file was generated by pyright.
"""

from abc import ABCMeta, abstractmethod
from six import add_metaclass

@add_metaclass(ABCMeta)
class StemmerI(object):
    """
    A processing interface for removing morphological affixes from
    words.  This process is known as stemming.

    """
    @abstractmethod
    def stem(self, token):
        """
        Strip affixes from the token and return the stem.

        :param token: The token that should be stemmed.
        :type token: str
        """
        ...
    


