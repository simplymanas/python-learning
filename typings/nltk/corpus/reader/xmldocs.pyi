"""
This type stub file was generated by pyright.
"""

from nltk.corpus.reader.api import CorpusReader
from nltk.corpus.reader.util import *
from typing import Any, Optional

"""
Corpus reader for corpora whose documents are xml files.

(note -- not named 'xml' to avoid conflicting w/ standard xml package)
"""
class XMLCorpusReader(CorpusReader):
    """
    Corpus reader for corpora whose documents are xml files.

    Note that the ``XMLCorpusReader`` constructor does not take an
    ``encoding`` argument, because the unicode encoding is specified by
    the XML files themselves.  See the XML specs for more info.
    """
    def __init__(self, root, fileids, wrap_etree: bool = ...):
        ...
    
    def xml(self, fileid: Optional[Any] = ...):
        ...
    
    def words(self, fileid: Optional[Any] = ...):
        """
        Returns all of the words and punctuation symbols in the specified file
        that were in text nodes -- ie, tags are ignored. Like the xml() method,
        fileid can only specify one file.

        :return: the given file's text nodes as a list of words and punctuation symbols
        :rtype: list(str)
        """
        ...
    
    def raw(self, fileids: Optional[Any] = ...):
        ...
    


class XMLCorpusView(StreamBackedCorpusView):
    """
    A corpus view that selects out specified elements from an XML
    file, and provides a flat list-like interface for accessing them.
    (Note: ``XMLCorpusView`` is not used by ``XMLCorpusReader`` itself,
    but may be used by subclasses of ``XMLCorpusReader``.)

    Every XML corpus view has a "tag specification", indicating what
    XML elements should be included in the view; and each (non-nested)
    element that matches this specification corresponds to one item in
    the view.  Tag specifications are regular expressions over tag
    paths, where a tag path is a list of element tag names, separated
    by '/', indicating the ancestry of the element.  Some examples:

      - ``'foo'``: A top-level element whose tag is ``foo``.
      - ``'foo/bar'``: An element whose tag is ``bar`` and whose parent
        is a top-level element whose tag is ``foo``.
      - ``'.*/foo'``: An element whose tag is ``foo``, appearing anywhere
        in the xml tree.
      - ``'.*/(foo|bar)'``: An wlement whose tag is ``foo`` or ``bar``,
        appearing anywhere in the xml tree.

    The view items are generated from the selected XML elements via
    the method ``handle_elt()``.  By default, this method returns the
    element as-is (i.e., as an ElementTree object); but it can be
    overridden, either via subclassing or via the ``elt_handler``
    constructor parameter.
    """
    _DEBUG = ...
    _BLOCK_SIZE = ...
    def __init__(self, fileid, tagspec, elt_handler: Optional[Any] = ...):
        """
        Create a new corpus view based on a specified XML file.

        Note that the ``XMLCorpusView`` constructor does not take an
        ``encoding`` argument, because the unicode encoding is
        specified by the XML files themselves.

        :type tagspec: str
        :param tagspec: A tag specification, indicating what XML
            elements should be included in the view.  Each non-nested
            element that matches this specification corresponds to one
            item in the view.

        :param elt_handler: A function used to transform each element
            to a value for the view.  If no handler is specified, then
            ``self.handle_elt()`` is called, which returns the element
            as an ElementTree object.  The signature of elt_handler is::

                elt_handler(elt, tagspec) -> value
        """
        ...
    
    def _detect_encoding(self, fileid):
        ...
    
    def handle_elt(self, elt, context):
        """
        Convert an element into an appropriate value for inclusion in
        the view.  Unless overridden by a subclass or by the
        ``elt_handler`` constructor argument, this method simply
        returns ``elt``.

        :return: The view value corresponding to ``elt``.

        :type elt: ElementTree
        :param elt: The element that should be converted.

        :type context: str
        :param context: A string composed of element tags separated by
            forward slashes, indicating the XML context of the given
            element.  For example, the string ``'foo/bar/baz'``
            indicates that the element is a ``baz`` element whose
            parent is a ``bar`` element and whose grandparent is a
            top-level ``foo`` element.
        """
        ...
    
    _VALID_XML_RE = ...
    _XML_TAG_NAME = ...
    _XML_PIECE = ...
    def _read_xml_fragment(self, stream):
        """
        Read a string from the given stream that does not contain any
        un-closed tags.  In particular, this function first reads a
        block from the stream of size ``self._BLOCK_SIZE``.  It then
        checks if that block contains an un-closed tag.  If it does,
        then this function either backtracks to the last '<', or reads
        another block.
        """
        ...
    
    def read_block(self, stream, tagspec: Optional[Any] = ..., elt_handler: Optional[Any] = ...):
        """
        Read from ``stream`` until we find at least one element that
        matches ``tagspec``, and return the result of applying
        ``elt_handler`` to each element found.
        """
        ...
    


