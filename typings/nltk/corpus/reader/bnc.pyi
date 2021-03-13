"""
This type stub file was generated by pyright.
"""

from nltk.corpus.reader.xmldocs import XMLCorpusReader, XMLCorpusView
from typing import Any, Optional

"""Corpus reader for the XML version of the British National Corpus."""
class BNCCorpusReader(XMLCorpusReader):
    """Corpus reader for the XML version of the British National Corpus.

    For access to the complete XML data structure, use the ``xml()``
    method.  For access to simple word lists and tagged word lists, use
    ``words()``, ``sents()``, ``tagged_words()``, and ``tagged_sents()``.

    You can obtain the full version of the BNC corpus at
    http://www.ota.ox.ac.uk/desc/2554

    If you extracted the archive to a directory called `BNC`, then you can
    instantiate the reader as::

        BNCCorpusReader(root='BNC/Texts/', fileids=r'[A-K]/\w*/\w*\.xml')

    """
    def __init__(self, root, fileids, lazy: bool = ...):
        ...
    
    def words(self, fileids: Optional[Any] = ..., strip_space: bool = ..., stem: bool = ...):
        """
        :return: the given file(s) as a list of words
            and punctuation symbols.
        :rtype: list(str)

        :param strip_space: If true, then strip trailing spaces from
            word tokens.  Otherwise, leave the spaces on the tokens.
        :param stem: If true, then use word stems instead of word strings.
        """
        ...
    
    def tagged_words(self, fileids: Optional[Any] = ..., c5: bool = ..., strip_space: bool = ..., stem: bool = ...):
        """
        :return: the given file(s) as a list of tagged
            words and punctuation symbols, encoded as tuples
            ``(word,tag)``.
        :rtype: list(tuple(str,str))

        :param c5: If true, then the tags used will be the more detailed
            c5 tags.  Otherwise, the simplified tags will be used.
        :param strip_space: If true, then strip trailing spaces from
            word tokens.  Otherwise, leave the spaces on the tokens.
        :param stem: If true, then use word stems instead of word strings.
        """
        ...
    
    def sents(self, fileids: Optional[Any] = ..., strip_space: bool = ..., stem: bool = ...):
        """
        :return: the given file(s) as a list of
            sentences or utterances, each encoded as a list of word
            strings.
        :rtype: list(list(str))

        :param strip_space: If true, then strip trailing spaces from
            word tokens.  Otherwise, leave the spaces on the tokens.
        :param stem: If true, then use word stems instead of word strings.
        """
        ...
    
    def tagged_sents(self, fileids: Optional[Any] = ..., c5: bool = ..., strip_space: bool = ..., stem: bool = ...):
        """
        :return: the given file(s) as a list of
            sentences, each encoded as a list of ``(word,tag)`` tuples.
        :rtype: list(list(tuple(str,str)))

        :param c5: If true, then the tags used will be the more detailed
            c5 tags.  Otherwise, the simplified tags will be used.
        :param strip_space: If true, then strip trailing spaces from
            word tokens.  Otherwise, leave the spaces on the tokens.
        :param stem: If true, then use word stems instead of word strings.
        """
        ...
    
    def _views(self, fileids: Optional[Any] = ..., sent: bool = ..., tag: bool = ..., strip_space: bool = ..., stem: bool = ...):
        """A helper function that instantiates BNCWordViews or the list of words/sentences."""
        ...
    
    def _words(self, fileid, bracket_sent, tag, strip_space, stem):
        """
        Helper used to implement the view methods -- returns a list of
        words or a list of sentences, optionally tagged.

        :param fileid: The name of the underlying file.
        :param bracket_sent: If true, include sentence bracketing.
        :param tag: The name of the tagset to use, or None for no tags.
        :param strip_space: If true, strip spaces from word tokens.
        :param stem: If true, then substitute stems for words.
        """
        ...
    


def _all_xmlwords_in(elt, result: Optional[Any] = ...):
    ...

class BNCSentence(list):
    """
    A list of words, augmented by an attribute ``num`` used to record
    the sentence identifier (the ``n`` attribute from the XML).
    """
    def __init__(self, num, items):
        self.num = ...
    


class BNCWordView(XMLCorpusView):
    """
    A stream backed corpus view specialized for use with the BNC corpus.
    """
    tags_to_ignore = ...
    def __init__(self, fileid, sent, tag, strip_space, stem):
        """
        :param fileid: The name of the underlying file.
        :param sent: If true, include sentence bracketing.
        :param tag: The name of the tagset to use, or None for no tags.
        :param strip_space: If true, strip spaces from word tokens.
        :param stem: If true, then substitute stems for words.
        """
        self.title = ...
        self.author = ...
        self.editor = ...
        self.resps = ...
    
    def handle_header(self, elt, context):
        ...
    
    def handle_elt(self, elt, context):
        ...
    
    def handle_word(self, elt):
        ...
    
    def handle_sent(self, elt):
        ...
    


