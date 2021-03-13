"""
This type stub file was generated by pyright.
"""

from functools import total_ordering
from nltk.compat import python_2_unicode_compatible

@total_ordering
@python_2_unicode_compatible
class DependencySpan(object):
    """
    A contiguous span over some part of the input string representing
    dependency (head -> modifier) relationships amongst words.  An atomic
    span corresponds to only one word so it isn't a 'span' in the conventional
    sense, as its _start_index = _end_index = _head_index for concatenation
    purposes.  All other spans are assumed to have arcs between all nodes
    within the start and end indexes of the span, and one head index corresponding
    to the head word for the entire span.  This is the same as the root node if
    the dependency structure were depicted as a graph.
    """
    def __init__(self, start_index, end_index, head_index, arcs, tags):
        ...
    
    def head_index(self):
        """
        :return: An value indexing the head of the entire ``DependencySpan``.
        :rtype: int
        """
        ...
    
    def __repr__(self):
        """
        :return: A concise string representatino of the ``DependencySpan``.
        :rtype: str.
        """
        ...
    
    def __str__(self):
        """
        :return: A verbose string representation of the ``DependencySpan``.
        :rtype: str
        """
        ...
    
    def __eq__(self, other):
        ...
    
    def __ne__(self, other):
        ...
    
    def __lt__(self, other):
        ...
    
    def __hash__(self):
        """
        :return: The hash value of this ``DependencySpan``.
        """
        ...
    


@python_2_unicode_compatible
class ChartCell(object):
    """
    A cell from the parse chart formed when performing the CYK algorithm.
    Each cell keeps track of its x and y coordinates (though this will probably
    be discarded), and a list of spans serving as the cell's entries.
    """
    def __init__(self, x, y):
        """
        :param x: This cell's x coordinate.
        :type x: int.
        :param y: This cell's y coordinate.
        :type y: int.
        """
        ...
    
    def add(self, span):
        """
        Appends the given span to the list of spans
        representing the chart cell's entries.

        :param span: The span to add.
        :type span: DependencySpan
        """
        ...
    
    def __str__(self):
        """
        :return: A verbose string representation of this ``ChartCell``.
        :rtype: str.
        """
        ...
    
    def __repr__(self):
        """
        :return: A concise string representation of this ``ChartCell``.
        :rtype: str.
        """
        ...
    


class ProjectiveDependencyParser(object):
    """
    A projective, rule-based, dependency parser.  A ProjectiveDependencyParser
    is created with a DependencyGrammar, a set of productions specifying
    word-to-word dependency relations.  The parse() method will then
    return the set of all parses, in tree representation, for a given input
    sequence of tokens.  Each parse must meet the requirements of the both
    the grammar and the projectivity constraint which specifies that the
    branches of the dependency tree are not allowed to cross.  Alternatively,
    this can be understood as stating that each parent node and its children
    in the parse tree form a continuous substring of the input sequence.
    """
    def __init__(self, dependency_grammar):
        """
        Create a new ProjectiveDependencyParser, from a word-to-word
        dependency grammar ``DependencyGrammar``.

        :param dependency_grammar: A word-to-word relation dependencygrammar.
        :type dependency_grammar: DependencyGrammar
        """
        ...
    
    def parse(self, tokens):
        """
        Performs a projective dependency parse on the list of tokens using
        a chart-based, span-concatenation algorithm similar to Eisner (1996).

        :param tokens: The list of input tokens.
        :type tokens: list(str)
        :return: An iterator over parse trees.
        :rtype: iter(Tree)
        """
        ...
    
    def concatenate(self, span1, span2):
        """
        Concatenates the two spans in whichever way possible.  This
        includes rightward concatenation (from the leftmost word of the
        leftmost span to the rightmost word of the rightmost span) and
        leftward concatenation (vice-versa) between adjacent spans.  Unlike
        Eisner's presentation of span concatenation, these spans do not
        share or pivot on a particular word/word-index.

        :return: A list of new spans formed through concatenation.
        :rtype: list(DependencySpan)
        """
        ...
    


class ProbabilisticProjectiveDependencyParser(object):
    """A probabilistic, projective dependency parser.

    This parser returns the most probable projective parse derived from the
    probabilistic dependency grammar derived from the train() method.  The
    probabilistic model is an implementation of Eisner's (1996) Model C, which
    conditions on head-word, head-tag, child-word, and child-tag.  The decoding
    uses a bottom-up chart-based span concatenation algorithm that's identical
    to the one utilized by the rule-based projective parser.

    Usage example
    -------------
    >>> from nltk.parse.dependencygraph import conll_data2

    >>> graphs = [
    ... DependencyGraph(entry) for entry in conll_data2.split('\\n\\n') if entry
    ... ]

    >>> ppdp = ProbabilisticProjectiveDependencyParser()
    >>> ppdp.train(graphs)

    >>> sent = ['Cathy', 'zag', 'hen', 'wild', 'zwaaien', '.']
    >>> list(ppdp.parse(sent))
    [Tree('zag', ['Cathy', 'hen', Tree('zwaaien', ['wild', '.'])])]

    """
    def __init__(self):
        """
        Create a new probabilistic dependency parser.  No additional
        operations are necessary.
        """
        ...
    
    def parse(self, tokens):
        """
        Parses the list of tokens subject to the projectivity constraint
        and the productions in the parser's grammar.  This uses a method
        similar to the span-concatenation algorithm defined in Eisner (1996).
        It returns the most probable parse derived from the parser's
        probabilistic dependency grammar.
        """
        ...
    
    def concatenate(self, span1, span2):
        """
        Concatenates the two spans in whichever way possible.  This
        includes rightward concatenation (from the leftmost word of the
        leftmost span to the rightmost word of the rightmost span) and
        leftward concatenation (vice-versa) between adjacent spans.  Unlike
        Eisner's presentation of span concatenation, these spans do not
        share or pivot on a particular word/word-index.

        :return: A list of new spans formed through concatenation.
        :rtype: list(DependencySpan)
        """
        ...
    
    def train(self, graphs):
        """
        Trains a ProbabilisticDependencyGrammar based on the list of input
        DependencyGraphs.  This model is an implementation of Eisner's (1996)
        Model C, which derives its statistics from head-word, head-tag,
        child-word, and child-tag relationships.

        :param graphs: A list of dependency graphs to train from.
        :type: list(DependencyGraph)
        """
        ...
    
    def compute_prob(self, dg):
        """
        Computes the probability of a dependency graph based
        on the parser's probability model (defined by the parser's
        statistical dependency grammar).

        :param dg: A dependency graph to score.
        :type dg: DependencyGraph
        :return: The probability of the dependency graph.
        :rtype: int
        """
        ...
    


def demo():
    ...

def projective_rule_parse_demo():
    """
    A demonstration showing the creation and use of a
    ``DependencyGrammar`` to perform a projective dependency
    parse.
    """
    ...

def arity_parse_demo():
    """
    A demonstration showing the creation of a ``DependencyGrammar``
    in which a specific number of modifiers is listed for a given
    head.  This can further constrain the number of possible parses
    created by a ``ProjectiveDependencyParser``.
    """
    ...

def projective_prob_parse_demo():
    """
    A demo showing the training and use of a projective
    dependency parser.
    """
    ...

if __name__ == '__main__':
    ...