"""
This type stub file was generated by pyright.
"""

from nltk.tokenize import *
from nltk.corpus.reader.util import *
from nltk.corpus.reader.api import *
from typing import Any, Optional

class DependencyCorpusReader(SyntaxCorpusReader):
    def __init__(self, root, fileids, encoding=..., word_tokenizer=..., sent_tokenizer=..., para_block_reader=...):
        ...
    
    def raw(self, fileids: Optional[Any] = ...):
        """
        :return: the given file(s) as a single string.
        :rtype: str
        """
        ...
    
    def words(self, fileids: Optional[Any] = ...):
        ...
    
    def tagged_words(self, fileids: Optional[Any] = ...):
        ...
    
    def sents(self, fileids: Optional[Any] = ...):
        ...
    
    def tagged_sents(self, fileids: Optional[Any] = ...):
        ...
    
    def parsed_sents(self, fileids: Optional[Any] = ...):
        ...
    


class DependencyCorpusView(StreamBackedCorpusView):
    _DOCSTART = ...
    def __init__(self, corpus_file, tagged, group_by_sent, dependencies, chunk_types: Optional[Any] = ..., encoding=...):
        ...
    
    def read_block(self, stream):
        ...
    


