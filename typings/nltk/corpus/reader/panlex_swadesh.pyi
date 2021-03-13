"""
This type stub file was generated by pyright.
"""

from collections import namedtuple
from nltk.corpus.reader.wordlist import WordListCorpusReader
from nltk.corpus.reader.util import *
from nltk.corpus.reader.api import *
from typing import Any, Optional

PanlexLanguage = namedtuple('PanlexLanguage', ['panlex_uid', 'iso639', 'iso639_type', 'script', 'name', 'langvar_uid'])
class PanlexSwadeshCorpusReader(WordListCorpusReader):
    """
    This is a class to read the PanLex Swadesh list from

    David Kamholz, Jonathan Pool, and Susan M. Colowick (2014).
    PanLex: Building a Resource for Panlingual Lexical Translation.
    In LREC. http://www.lrec-conf.org/proceedings/lrec2014/pdf/1029_Paper.pdf

    License: CC0 1.0 Universal
    https://creativecommons.org/publicdomain/zero/1.0/legalcode
    """
    def __init__(self, *args, **kwargs):
        self.swadesh_size = ...
    
    def license(self):
        ...
    
    def readme(self):
        ...
    
    def language_codes(self):
        ...
    
    def get_languages(self):
        ...
    
    def get_macrolanguages(self):
        ...
    
    def words_by_lang(self, lang_code):
        """
        :return: a list of list(str)
        """
        ...
    
    def words_by_iso639(self, iso63_code):
        """
        :return: a list of list(str)
        """
        ...
    
    def entries(self, fileids: Optional[Any] = ...):
        """
        :return: a tuple of words for the specified fileids.
        """
        ...
    

