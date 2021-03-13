"""
This type stub file was generated by pyright.
"""

from nltk.compat import python_2_unicode_compatible
from nltk.parse.chart import BottomUpPredictCombineRule, BottomUpPredictRule, CachedTopDownPredictRule, Chart, ChartParser, EmptyPredictRule, FundamentalRule, LeafInitRule, SingleEdgeFundamentalRule, TopDownInitRule, TreeEdge
from typing import Any, Optional
from nltk.data import load

"""
Extension of chart parsing implementation to handle grammars with
feature structures as nodes.
"""
@python_2_unicode_compatible
class FeatureTreeEdge(TreeEdge):
    """
    A specialized tree edge that allows shared variable bindings
    between nonterminals on the left-hand side and right-hand side.

    Each ``FeatureTreeEdge`` contains a set of ``bindings``, i.e., a
    dictionary mapping from variables to values.  If the edge is not
    complete, then these bindings are simply stored.  However, if the
    edge is complete, then the constructor applies these bindings to
    every nonterminal in the edge whose symbol implements the
    interface ``SubstituteBindingsI``.
    """
    def __init__(self, span, lhs, rhs, dot=..., bindings: Optional[Any] = ...):
        """
        Construct a new edge.  If the edge is incomplete (i.e., if
        ``dot<len(rhs)``), then store the bindings as-is.  If the edge
        is complete (i.e., if ``dot==len(rhs)``), then apply the
        bindings to all nonterminals in ``lhs`` and ``rhs``, and then
        clear the bindings.  See ``TreeEdge`` for a description of
        the other arguments.
        """
        ...
    
    @staticmethod
    def from_production(production, index):
        """
        :return: A new ``TreeEdge`` formed from the given production.
            The new edge's left-hand side and right-hand side will
            be taken from ``production``; its span will be
            ``(index,index)``; and its dot position will be ``0``.
        :rtype: TreeEdge
        """
        ...
    
    def move_dot_forward(self, new_end, bindings: Optional[Any] = ...):
        """
        :return: A new ``FeatureTreeEdge`` formed from this edge.
            The new edge's dot position is increased by ``1``,
            and its end index will be replaced by ``new_end``.
        :rtype: FeatureTreeEdge
        :param new_end: The new end index.
        :type new_end: int
        :param bindings: Bindings for the new edge.
        :type bindings: dict
        """
        ...
    
    def _bind(self, nt, bindings):
        ...
    
    def next_with_bindings(self):
        ...
    
    def bindings(self):
        """
        Return a copy of this edge's bindings dictionary.
        """
        ...
    
    def variables(self):
        """
        :return: The set of variables used by this edge.
        :rtype: set(Variable)
        """
        ...
    
    def __str__(self):
        ...
    


class FeatureChart(Chart):
    """
    A Chart for feature grammars.
    :see: ``Chart`` for more information.
    """
    def select(self, **restrictions):
        """
        Returns an iterator over the edges in this chart.
        See ``Chart.select`` for more information about the
        ``restrictions`` on the edges.
        """
        ...
    
    def _add_index(self, restr_keys):
        """
        A helper function for ``select``, which creates a new index for
        a given set of attributes (aka restriction keys).
        """
        ...
    
    def _register_with_indexes(self, edge):
        """
        A helper function for ``insert``, which registers the new
        edge with all existing indexes.
        """
        ...
    
    def _get_type_if_possible(self, item):
        """
        Helper function which returns the ``TYPE`` feature of the ``item``,
        if it exists, otherwise it returns the ``item`` itself
        """
        ...
    
    def parses(self, start, tree_class=...):
        ...
    


class FeatureFundamentalRule(FundamentalRule):
    """
    A specialized version of the fundamental rule that operates on
    nonterminals whose symbols are ``FeatStructNonterminal``s.  Rather
    tha simply comparing the nonterminals for equality, they are
    unified.  Variable bindings from these unifications are collected
    and stored in the chart using a ``FeatureTreeEdge``.  When a
    complete edge is generated, these bindings are applied to all
    nonterminals in the edge.

    The fundamental rule states that:

    - ``[A -> alpha \* B1 beta][i:j]``
    - ``[B2 -> gamma \*][j:k]``

    licenses the edge:

    - ``[A -> alpha B3 \* beta][i:j]``

    assuming that B1 and B2 can be unified to generate B3.
    """
    def apply(self, chart, grammar, left_edge, right_edge):
        ...
    


class FeatureSingleEdgeFundamentalRule(SingleEdgeFundamentalRule):
    """
    A specialized version of the completer / single edge fundamental rule
    that operates on nonterminals whose symbols are ``FeatStructNonterminal``s.
    Rather than simply comparing the nonterminals for equality, they are
    unified.
    """
    _fundamental_rule = ...
    def _apply_complete(self, chart, grammar, right_edge):
        ...
    
    def _apply_incomplete(self, chart, grammar, left_edge):
        ...
    


class FeatureTopDownInitRule(TopDownInitRule):
    def apply(self, chart, grammar):
        ...
    


class FeatureTopDownPredictRule(CachedTopDownPredictRule):
    """
    A specialized version of the (cached) top down predict rule that operates
    on nonterminals whose symbols are ``FeatStructNonterminal``s.  Rather
    than simply comparing the nonterminals for equality, they are
    unified.

    The top down expand rule states that:

    - ``[A -> alpha \* B1 beta][i:j]``

    licenses the edge:

    - ``[B2 -> \* gamma][j:j]``

    for each grammar production ``B2 -> gamma``, assuming that B1
    and B2 can be unified.
    """
    def apply(self, chart, grammar, edge):
        ...
    


class FeatureBottomUpPredictRule(BottomUpPredictRule):
    def apply(self, chart, grammar, edge):
        ...
    


class FeatureBottomUpPredictCombineRule(BottomUpPredictCombineRule):
    def apply(self, chart, grammar, edge):
        ...
    


class FeatureEmptyPredictRule(EmptyPredictRule):
    def apply(self, chart, grammar):
        ...
    


TD_FEATURE_STRATEGY = [LeafInitRule(), FeatureTopDownInitRule(), FeatureTopDownPredictRule(), FeatureSingleEdgeFundamentalRule()]
BU_FEATURE_STRATEGY = [LeafInitRule(), FeatureEmptyPredictRule(), FeatureBottomUpPredictRule(), FeatureSingleEdgeFundamentalRule()]
BU_LC_FEATURE_STRATEGY = [LeafInitRule(), FeatureEmptyPredictRule(), FeatureBottomUpPredictCombineRule(), FeatureSingleEdgeFundamentalRule()]
class FeatureChartParser(ChartParser):
    def __init__(self, grammar, strategy=..., trace_chart_width=..., chart_class=..., **parser_args):
        ...
    


class FeatureTopDownChartParser(FeatureChartParser):
    def __init__(self, grammar, **parser_args):
        ...
    


class FeatureBottomUpChartParser(FeatureChartParser):
    def __init__(self, grammar, **parser_args):
        ...
    


class FeatureBottomUpLeftCornerChartParser(FeatureChartParser):
    def __init__(self, grammar, **parser_args):
        ...
    


class InstantiateVarsChart(FeatureChart):
    """
    A specialized chart that 'instantiates' variables whose names
    start with '@', by replacing them with unique new variables.
    In particular, whenever a complete edge is added to the chart, any
    variables in the edge's ``lhs`` whose names start with '@' will be
    replaced by unique new ``Variable``s.
    """
    def __init__(self, tokens):
        ...
    
    def initialize(self):
        ...
    
    def insert(self, edge, child_pointer_list):
        ...
    
    def instantiate_edge(self, edge):
        """
        If the edge is a ``FeatureTreeEdge``, and it is complete,
        then instantiate all variables whose names start with '@',
        by replacing them with unique new variables.

        Note that instantiation is done in-place, since the
        parsing algorithms might already hold a reference to
        the edge for future use.
        """
        ...
    
    def inst_vars(self, edge):
        ...
    


def demo_grammar():
    ...

def demo(print_times: bool = ..., print_grammar: bool = ..., print_trees: bool = ..., print_sentence: bool = ..., trace=..., parser=..., sent=...):
    ...

def run_profile():
    ...

if __name__ == '__main__':
    grammar = load('grammars/book_grammars/feat0.fcfg')
    cp = FeatureChartParser(grammar, trace=2)
    sent = 'Kim likes children'
    tokens = sent.split()
    trees = cp.parse(tokens)
