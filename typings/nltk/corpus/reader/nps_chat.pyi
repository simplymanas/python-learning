"""
This type stub file was generated by pyright.
"""

from nltk.corpus.reader.util import *
from nltk.corpus.reader.api import *
from nltk.corpus.reader.xmldocs import *
from typing import Any, Optional

class NPSChatCorpusReader(XMLCorpusReader):
    def __init__(self, root, fileids, wrap_etree: bool = ..., tagset: Optional[Any] = ...):
        ...
    
    def xml_posts(self, fileids: Optional[Any] = ...):
        ...
    
    def posts(self, fileids: Optional[Any] = ...):
        ...
    
    def tagged_posts(self, fileids: Optional[Any] = ..., tagset: Optional[Any] = ...):
        ...
    
    def words(self, fileids: Optional[Any] = ...):
        ...
    
    def tagged_words(self, fileids: Optional[Any] = ..., tagset: Optional[Any] = ...):
        ...
    
    def _wrap_elt(self, elt, handler):
        ...
    
    def _elt_to_words(self, elt, handler):
        ...
    
    def _elt_to_tagged_words(self, elt, handler, tagset: Optional[Any] = ...):
        ...
    
    @staticmethod
    def _simplify_username(word):
        ...
    


