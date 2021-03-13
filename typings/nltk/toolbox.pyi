"""
This type stub file was generated by pyright.
"""

import re
from typing import Any, Optional

"""
Module for reading, writing and manipulating
Toolbox databases and settings files.
"""
class StandardFormat(object):
    """
    Class for reading and processing standard format marker files and strings.
    """
    def __init__(self, filename: Optional[Any] = ..., encoding: Optional[Any] = ...):
        ...
    
    def open(self, sfm_file):
        """
        Open a standard format marker file for sequential reading.

        :param sfm_file: name of the standard format marker input file
        :type sfm_file: str
        """
        ...
    
    def open_string(self, s):
        """
        Open a standard format marker string for sequential reading.

        :param s: string to parse as a standard format marker input file
        :type s: str
        """
        ...
    
    def raw_fields(self):
        """
        Return an iterator that returns the next field in a (marker, value)
        tuple. Linebreaks and trailing white space are preserved except
        for the final newline in each field.

        :rtype: iter(tuple(str, str))
        """
        self.line_num = ...
    
    def fields(self, strip: bool = ..., unwrap: bool = ..., encoding: Optional[Any] = ..., errors=..., unicode_fields: Optional[Any] = ...):
        """
        Return an iterator that returns the next field in a ``(marker, value)``
        tuple, where ``marker`` and ``value`` are unicode strings if an ``encoding``
        was specified in the ``fields()`` method. Otherwise they are non-unicode strings.

        :param strip: strip trailing whitespace from the last line of each field
        :type strip: bool
        :param unwrap: Convert newlines in a field to spaces.
        :type unwrap: bool
        :param encoding: Name of an encoding to use. If it is specified then
            the ``fields()`` method returns unicode strings rather than non
            unicode strings.
        :type encoding: str or None
        :param errors: Error handling scheme for codec. Same as the ``decode()``
            builtin string method.
        :type errors: str
        :param unicode_fields: Set of marker names whose values are UTF-8 encoded.
            Ignored if encoding is None. If the whole file is UTF-8 encoded set
            ``encoding='utf8'`` and leave ``unicode_fields`` with its default
            value of None.
        :type unicode_fields: sequence
        :rtype: iter(tuple(str, str))
        """
        ...
    
    def close(self):
        """Close a previously opened standard format marker file or string."""
        ...
    


class ToolboxData(StandardFormat):
    def parse(self, grammar: Optional[Any] = ..., **kwargs):
        ...
    
    def _record_parse(self, key: Optional[Any] = ..., **kwargs):
        """
        Returns an element tree structure corresponding to a toolbox data file with
        all markers at the same level.

        Thus the following Toolbox database::
            \_sh v3.0  400  Rotokas Dictionary
            \_DateStampHasFourDigitYear

            \lx kaa
            \ps V.A
            \ge gag
            \gp nek i pas

            \lx kaa
            \ps V.B
            \ge strangle
            \gp pasim nek

        after parsing will end up with the same structure (ignoring the extra
        whitespace) as the following XML fragment after being parsed by
        ElementTree::
            <toolbox_data>
                <header>
                    <_sh>v3.0  400  Rotokas Dictionary</_sh>
                    <_DateStampHasFourDigitYear/>
                </header>

                <record>
                    <lx>kaa</lx>
                    <ps>V.A</ps>
                    <ge>gag</ge>
                    <gp>nek i pas</gp>
                </record>

                <record>
                    <lx>kaa</lx>
                    <ps>V.B</ps>
                    <ge>strangle</ge>
                    <gp>pasim nek</gp>
                </record>
            </toolbox_data>

        :param key: Name of key marker at the start of each record. If set to
            None (the default value) the first marker that doesn't begin with
            an underscore is assumed to be the key.
        :type key: str
        :param kwargs: Keyword arguments passed to ``StandardFormat.fields()``
        :type kwargs: dict
        :rtype: ElementTree._ElementInterface
        :return: contents of toolbox data divided into header and records
        """
        ...
    
    def _tree2etree(self, parent):
        ...
    
    def _chunk_parse(self, grammar: Optional[Any] = ..., root_label=..., trace=..., **kwargs):
        """
        Returns an element tree structure corresponding to a toolbox data file
        parsed according to the chunk grammar.

        :type grammar: str
        :param grammar: Contains the chunking rules used to parse the
            database.  See ``chunk.RegExp`` for documentation.
        :type root_label: str
        :param root_label: The node value that should be used for the
            top node of the chunk structure.
        :type trace: int
        :param trace: The level of tracing that should be used when
            parsing a text.  ``0`` will generate no tracing output;
            ``1`` will generate normal tracing output; and ``2`` or
            higher will generate verbose tracing output.
        :type kwargs: dict
        :param kwargs: Keyword arguments passed to ``toolbox.StandardFormat.fields()``
        :rtype: ElementTree._ElementInterface
        """
        ...
    


_is_value = re.compile(r"\S")
def to_sfm_string(tree, encoding: Optional[Any] = ..., errors=..., unicode_fields: Optional[Any] = ...):
    """
    Return a string with a standard format representation of the toolbox
    data in tree (tree can be a toolbox database or a single record).

    :param tree: flat representation of toolbox data (whole database or single record)
    :type tree: ElementTree._ElementInterface
    :param encoding: Name of an encoding to use.
    :type encoding: str
    :param errors: Error handling scheme for codec. Same as the ``encode()``
        builtin string method.
    :type errors: str
    :param unicode_fields:
    :type unicode_fields: dict(str) or set(str)
    :rtype: str
    """
    ...

class ToolboxSettings(StandardFormat):
    """This class is the base class for settings files."""
    def __init__(self):
        ...
    
    def parse(self, encoding: Optional[Any] = ..., errors=..., **kwargs):
        """
        Return the contents of toolbox settings file with a nested structure.

        :param encoding: encoding used by settings file
        :type encoding: str
        :param errors: Error handling scheme for codec. Same as ``decode()`` builtin method.
        :type errors: str
        :param kwargs: Keyword arguments passed to ``StandardFormat.fields()``
        :type kwargs: dict
        :rtype: ElementTree._ElementInterface
        """
        ...
    


def to_settings_string(tree, encoding: Optional[Any] = ..., errors=..., unicode_fields: Optional[Any] = ...):
    ...

def _to_settings_string(node, l, **kwargs):
    ...

def remove_blanks(elem):
    """
    Remove all elements and subelements with no text and no child elements.

    :param elem: toolbox data in an elementtree structure
    :type elem: ElementTree._ElementInterface
    """
    ...

def add_default_fields(elem, default_fields):
    """
    Add blank elements and subelements specified in default_fields.

    :param elem: toolbox data in an elementtree structure
    :type elem: ElementTree._ElementInterface
    :param default_fields: fields to add to each type of element and subelement
    :type default_fields: dict(tuple)
    """
    ...

def sort_fields(elem, field_orders):
    """
    Sort the elements and subelements in order specified in field_orders.

    :param elem: toolbox data in an elementtree structure
    :type elem: ElementTree._ElementInterface
    :param field_orders: order of fields for each type of element and subelement
    :type field_orders: dict(tuple)
    """
    ...

def _sort_fields(elem, orders_dicts):
    """sort the children of elem"""
    ...

def add_blank_lines(tree, blanks_before, blanks_between):
    """
    Add blank lines before all elements and subelements specified in blank_before.

    :param elem: toolbox data in an elementtree structure
    :type elem: ElementTree._ElementInterface
    :param blank_before: elements and subelements to add blank lines before
    :type blank_before: dict(tuple)
    """
    ...

def demo():
    ...

if __name__ == '__main__':
    ...
