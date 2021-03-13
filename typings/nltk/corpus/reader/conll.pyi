"""
This type stub file was generated by pyright.
"""

from nltk import compat
from nltk.corpus.reader.util import *
from nltk.corpus.reader.api import *
from typing import Any, Optional

"""
Read CoNLL-style chunk fileids.
"""
class ConllCorpusReader(CorpusReader):
    """
    A corpus reader for CoNLL-style files.  These files consist of a
    series of sentences, separated by blank lines.  Each sentence is
    encoded using a table (or "grid") of values, where each line
    corresponds to a single word, and each column corresponds to an
    annotation type.  The set of columns used by CoNLL-style files can
    vary from corpus to corpus; the ``ConllCorpusReader`` constructor
    therefore takes an argument, ``columntypes``, which is used to
    specify the columns that are used by a given corpus. By default
    columns are split by consecutive whitespaces, with the
    ``separator`` argument you can set a string to split by (e.g.
    ``\'\t\'``).


    @todo: Add support for reading from corpora where different
        parallel files contain different columns.
    @todo: Possibly add caching of the grid corpus view?  This would
        allow the same grid view to be used by different data access
        methods (eg words() and parsed_sents() could both share the
        same grid corpus view object).
    @todo: Better support for -DOCSTART-.  Currently, we just ignore
        it, but it could be used to define methods that retrieve a
        document at a time (eg parsed_documents()).
    """
    WORDS = ...
    POS = ...
    TREE = ...
    CHUNK = ...
    NE = ...
    SRL = ...
    IGNORE = ...
    COLUMN_TYPES = ...
    def __init__(self, root, fileids, columntypes, chunk_types: Optional[Any] = ..., root_label=..., pos_in_tree: bool = ..., srl_includes_roleset: bool = ..., encoding=..., tree_class=..., tagset: Optional[Any] = ..., separator: Optional[Any] = ...):
        self.sep = ...
    
    def raw(self, fileids: Optional[Any] = ...):
        ...
    
    def words(self, fileids: Optional[Any] = ...):
        ...
    
    def sents(self, fileids: Optional[Any] = ...):
        ...
    
    def tagged_words(self, fileids: Optional[Any] = ..., tagset: Optional[Any] = ...):
        ...
    
    def tagged_sents(self, fileids: Optional[Any] = ..., tagset: Optional[Any] = ...):
        ...
    
    def chunked_words(self, fileids: Optional[Any] = ..., chunk_types: Optional[Any] = ..., tagset: Optional[Any] = ...):
        ...
    
    def chunked_sents(self, fileids: Optional[Any] = ..., chunk_types: Optional[Any] = ..., tagset: Optional[Any] = ...):
        ...
    
    def parsed_sents(self, fileids: Optional[Any] = ..., pos_in_tree: Optional[Any] = ..., tagset: Optional[Any] = ...):
        ...
    
    def srl_spans(self, fileids: Optional[Any] = ...):
        ...
    
    def srl_instances(self, fileids: Optional[Any] = ..., pos_in_tree: Optional[Any] = ..., flatten: bool = ...):
        ...
    
    def iob_words(self, fileids: Optional[Any] = ..., tagset: Optional[Any] = ...):
        """
        :return: a list of word/tag/IOB tuples
        :rtype: list(tuple)
        :param fileids: the list of fileids that make up this corpus
        :type fileids: None or str or list
        """
        ...
    
    def iob_sents(self, fileids: Optional[Any] = ..., tagset: Optional[Any] = ...):
        """
        :return: a list of lists of word/tag/IOB tuples
        :rtype: list(list)
        :param fileids: the list of fileids that make up this corpus
        :type fileids: None or str or list
        """
        ...
    
    def _grids(self, fileids: Optional[Any] = ...):
        ...
    
    def _read_grid_block(self, stream):
        ...
    
    def _get_words(self, grid):
        ...
    
    def _get_tagged_words(self, grid, tagset: Optional[Any] = ...):
        ...
    
    def _get_iob_words(self, grid, tagset: Optional[Any] = ...):
        ...
    
    def _get_chunked_words(self, grid, chunk_types, tagset: Optional[Any] = ...):
        ...
    
    def _get_parsed_sent(self, grid, pos_in_tree, tagset: Optional[Any] = ...):
        ...
    
    def _get_srl_spans(self, grid):
        """
        list of list of (start, end), tag) tuples
        """
        ...
    
    def _get_srl_instances(self, grid, pos_in_tree):
        ...
    
    def _require(self, *columntypes):
        ...
    
    @staticmethod
    def _get_column(grid, column_index):
        ...
    


@compat.python_2_unicode_compatible
class ConllSRLInstance(object):
    """
    An SRL instance from a CoNLL corpus, which identifies and
    providing labels for the arguments of a single verb.
    """
    def __init__(self, tree, verb_head, verb_stem, roleset, tagged_spans):
        self.verb = ...
        self.verb_head = ...
        self.verb_stem = ...
        self.roleset = ...
        self.arguments = ...
        self.tagged_spans = ...
        self.tree = ...
        self.words = ...
    
    def __repr__(self):
        ...
    
    def pprint(self):
        ...
    


@compat.python_2_unicode_compatible
class ConllSRLInstanceList(list):
    """
    Set of instances for a single sentence
    """
    def __init__(self, tree, instances=...):
        self.tree = ...
    
    def __str__(self):
        ...
    
    def pprint(self, include_tree: bool = ...):
        ...
    
    def _tree2conll(self, tree, wordnum, words, pos, synt):
        ...
    


class ConllChunkCorpusReader(ConllCorpusReader):
    """
    A ConllCorpusReader whose data file contains three columns: words,
    pos, and chunk.
    """
    def __init__(self, root, fileids, chunk_types, encoding=..., tagset: Optional[Any] = ..., separator: Optional[Any] = ...):
        ...
    

