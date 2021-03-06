"""
This type stub file was generated by pyright.
"""

from nltk.corpus.reader.util import *
from nltk.corpus.reader.api import *
from typing import Any, Optional

"""
Read tuples from a corpus consisting of categorized strings.
For example, from the question classification corpus:

NUM:dist How far is it from Denver to Aspen ?
LOC:city What county is Modesto , California in ?
HUM:desc Who was Galileo ?
DESC:def What is an atom ?
NUM:date When did Hawaii become a state ?
"""
class StringCategoryCorpusReader(CorpusReader):
    def __init__(self, root, fileids, delimiter=..., encoding=...):
        """
        :param root: The root directory for this corpus.
        :param fileids: A list or regexp specifying the fileids in this corpus.
        :param delimiter: Field delimiter
        """
        ...
    
    def tuples(self, fileids: Optional[Any] = ...):
        ...
    
    def raw(self, fileids: Optional[Any] = ...):
        """
        :return: the text contents of the given fileids, as a single string.
        """
        ...
    
    def _read_tuple_block(self, stream):
        ...
    


