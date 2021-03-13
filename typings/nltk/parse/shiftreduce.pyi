"""
This type stub file was generated by pyright.
"""

from nltk.parse.api import ParserI
from typing import Any, Optional

class ShiftReduceParser(ParserI):
    """
    A simple bottom-up CFG parser that uses two operations, "shift"
    and "reduce", to find a single parse for a text.

    ``ShiftReduceParser`` maintains a stack, which records the
    structure of a portion of the text.  This stack is a list of
    strings and Trees that collectively cover a portion of
    the text.  For example, while parsing the sentence "the dog saw
    the man" with a typical grammar, ``ShiftReduceParser`` will produce
    the following stack, which covers "the dog saw"::

       [(NP: (Det: 'the') (N: 'dog')), (V: 'saw')]

    ``ShiftReduceParser`` attempts to extend the stack to cover the
    entire text, and to combine the stack elements into a single tree,
    producing a complete parse for the sentence.

    Initially, the stack is empty.  It is extended to cover the text,
    from left to right, by repeatedly applying two operations:

      - "shift" moves a token from the beginning of the text to the
        end of the stack.
      - "reduce" uses a CFG production to combine the rightmost stack
        elements into a single Tree.

    Often, more than one operation can be performed on a given stack.
    In this case, ``ShiftReduceParser`` uses the following heuristics
    to decide which operation to perform:

      - Only shift if no reductions are available.
      - If multiple reductions are available, then apply the reduction
        whose CFG production is listed earliest in the grammar.

    Note that these heuristics are not guaranteed to choose an
    operation that leads to a parse of the text.  Also, if multiple
    parses exists, ``ShiftReduceParser`` will return at most one of
    them.

    :see: ``nltk.grammar``
    """
    def __init__(self, grammar, trace=...):
        """
        Create a new ``ShiftReduceParser``, that uses ``grammar`` to
        parse texts.

        :type grammar: Grammar
        :param grammar: The grammar used to parse texts.
        :type trace: int
        :param trace: The level of tracing that should be used when
            parsing a text.  ``0`` will generate no tracing output;
            and higher numbers will produce more verbose tracing
            output.
        """
        ...
    
    def grammar(self):
        ...
    
    def parse(self, tokens):
        ...
    
    def _shift(self, stack, remaining_text):
        """
        Move a token from the beginning of ``remaining_text`` to the
        end of ``stack``.

        :type stack: list(str and Tree)
        :param stack: A list of strings and Trees, encoding
            the structure of the text that has been parsed so far.
        :type remaining_text: list(str)
        :param remaining_text: The portion of the text that is not yet
            covered by ``stack``.
        :rtype: None
        """
        ...
    
    def _match_rhs(self, rhs, rightmost_stack):
        """
        :rtype: bool
        :return: true if the right hand side of a CFG production
            matches the rightmost elements of the stack.  ``rhs``
            matches ``rightmost_stack`` if they are the same length,
            and each element of ``rhs`` matches the corresponding
            element of ``rightmost_stack``.  A nonterminal element of
            ``rhs`` matches any Tree whose node value is equal
            to the nonterminal's symbol.  A terminal element of ``rhs``
            matches any string whose type is equal to the terminal.
        :type rhs: list(terminal and Nonterminal)
        :param rhs: The right hand side of a CFG production.
        :type rightmost_stack: list(string and Tree)
        :param rightmost_stack: The rightmost elements of the parser's
            stack.
        """
        ...
    
    def _reduce(self, stack, remaining_text, production: Optional[Any] = ...):
        """
        Find a CFG production whose right hand side matches the
        rightmost stack elements; and combine those stack elements
        into a single Tree, with the node specified by the
        production's left-hand side.  If more than one CFG production
        matches the stack, then use the production that is listed
        earliest in the grammar.  The new Tree replaces the
        elements in the stack.

        :rtype: Production or None
        :return: If a reduction is performed, then return the CFG
            production that the reduction is based on; otherwise,
            return false.
        :type stack: list(string and Tree)
        :param stack: A list of strings and Trees, encoding
            the structure of the text that has been parsed so far.
        :type remaining_text: list(str)
        :param remaining_text: The portion of the text that is not yet
            covered by ``stack``.
        """
        ...
    
    def trace(self, trace=...):
        """
        Set the level of tracing output that should be generated when
        parsing a text.

        :type trace: int
        :param trace: The trace level.  A trace level of ``0`` will
            generate no tracing output; and higher trace levels will
            produce more verbose tracing output.
        :rtype: None
        """
        ...
    
    def _trace_stack(self, stack, remaining_text, marker=...):
        """
        Print trace output displaying the given stack and text.

        :rtype: None
        :param marker: A character that is printed to the left of the
            stack.  This is used with trace level 2 to print 'S'
            before shifted stacks and 'R' before reduced stacks.
        """
        ...
    
    def _trace_shift(self, stack, remaining_text):
        """
        Print trace output displaying that a token has been shifted.

        :rtype: None
        """
        ...
    
    def _trace_reduce(self, stack, production, remaining_text):
        """
        Print trace output displaying that ``production`` was used to
        reduce ``stack``.

        :rtype: None
        """
        ...
    
    def _check_grammar(self):
        """
        Check to make sure that all of the CFG productions are
        potentially useful.  If any productions can never be used,
        then print a warning.

        :rtype: None
        """
        ...
    


class SteppingShiftReduceParser(ShiftReduceParser):
    """
    A ``ShiftReduceParser`` that allows you to setp through the parsing
    process, performing a single operation at a time.  It also allows
    you to change the parser's grammar midway through parsing a text.

    The ``initialize`` method is used to start parsing a text.
    ``shift`` performs a single shift operation, and ``reduce`` performs
    a single reduce operation.  ``step`` will perform a single reduce
    operation if possible; otherwise, it will perform a single shift
    operation.  ``parses`` returns the set of parses that have been
    found by the parser.

    :ivar _history: A list of ``(stack, remaining_text)`` pairs,
        containing all of the previous states of the parser.  This
        history is used to implement the ``undo`` operation.
    :see: ``nltk.grammar``
    """
    def __init__(self, grammar, trace=...):
        ...
    
    def parse(self, tokens):
        ...
    
    def stack(self):
        """
        :return: The parser's stack.
        :rtype: list(str and Tree)
        """
        ...
    
    def remaining_text(self):
        """
        :return: The portion of the text that is not yet covered by the
            stack.
        :rtype: list(str)
        """
        ...
    
    def initialize(self, tokens):
        """
        Start parsing a given text.  This sets the parser's stack to
        ``[]`` and sets its remaining text to ``tokens``.
        """
        ...
    
    def step(self):
        """
        Perform a single parsing operation.  If a reduction is
        possible, then perform that reduction, and return the
        production that it is based on.  Otherwise, if a shift is
        possible, then perform it, and return True.  Otherwise,
        return False.

        :return: False if no operation was performed; True if a shift was
            performed; and the CFG production used to reduce if a
            reduction was performed.
        :rtype: Production or bool
        """
        ...
    
    def shift(self):
        """
        Move a token from the beginning of the remaining text to the
        end of the stack.  If there are no more tokens in the
        remaining text, then do nothing.

        :return: True if the shift operation was successful.
        :rtype: bool
        """
        ...
    
    def reduce(self, production: Optional[Any] = ...):
        """
        Use ``production`` to combine the rightmost stack elements into
        a single Tree.  If ``production`` does not match the
        rightmost stack elements, then do nothing.

        :return: The production used to reduce the stack, if a
            reduction was performed.  If no reduction was performed,
            return None.

        :rtype: Production or None
        """
        ...
    
    def undo(self):
        """
        Return the parser to its state before the most recent
        shift or reduce operation.  Calling ``undo`` repeatedly return
        the parser to successively earlier states.  If no shift or
        reduce operations have been performed, ``undo`` will make no
        changes.

        :return: true if an operation was successfully undone.
        :rtype: bool
        """
        ...
    
    def reducible_productions(self):
        """
        :return: A list of the productions for which reductions are
            available for the current parser state.
        :rtype: list(Production)
        """
        ...
    
    def parses(self):
        """
        :return: An iterator of the parses that have been found by this
            parser so far.
        :rtype: iter(Tree)
        """
        ...
    
    def set_grammar(self, grammar):
        """
        Change the grammar used to parse texts.

        :param grammar: The new grammar.
        :type grammar: CFG
        """
        ...
    


def demo():
    """
    A demonstration of the shift-reduce parser.
    """
    ...

if __name__ == '__main__':
    ...