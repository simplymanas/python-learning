"""
This type stub file was generated by pyright.
"""

from functools import total_ordering
from nltk.compat import python_2_unicode_compatible
from nltk.parse.api import ParserI
from typing import Any, Optional

"""
Data classes and parser implementations for "chart parsers", which
use dynamic programming to efficiently parse a text.  A chart
parser derives parse trees for a text by iteratively adding "edges"
to a "chart."  Each edge represents a hypothesis about the tree
structure for a subsequence of the text.  The chart is a
"blackboard" for composing and combining these hypotheses.

When a chart parser begins parsing a text, it creates a new (empty)
chart, spanning the text.  It then incrementally adds new edges to the
chart.  A set of "chart rules" specifies the conditions under which
new edges should be added to the chart.  Once the chart reaches a
stage where none of the chart rules adds any new edges, parsing is
complete.

Charts are encoded with the ``Chart`` class, and edges are encoded with
the ``TreeEdge`` and ``LeafEdge`` classes.  The chart parser module
defines three chart parsers:

  - ``ChartParser`` is a simple and flexible chart parser.  Given a
    set of chart rules, it will apply those rules to the chart until
    no more edges are added.

  - ``SteppingChartParser`` is a subclass of ``ChartParser`` that can
    be used to step through the parsing process.
"""
@total_ordering
class EdgeI(object):
    """
    A hypothesis about the structure of part of a sentence.
    Each edge records the fact that a structure is (partially)
    consistent with the sentence.  An edge contains:

    - A span, indicating what part of the sentence is
      consistent with the hypothesized structure.
    - A left-hand side, specifying what kind of structure is
      hypothesized.
    - A right-hand side, specifying the contents of the
      hypothesized structure.
    - A dot position, indicating how much of the hypothesized
      structure is consistent with the sentence.

    Every edge is either complete or incomplete:

    - An edge is complete if its structure is fully consistent
      with the sentence.
    - An edge is incomplete if its structure is partially
      consistent with the sentence.  For every incomplete edge, the
      span specifies a possible prefix for the edge's structure.

    There are two kinds of edge:

    - A ``TreeEdge`` records which trees have been found to
      be (partially) consistent with the text.
    - A ``LeafEdge`` records the tokens occurring in the text.

    The ``EdgeI`` interface provides a common interface to both types
    of edge, allowing chart parsers to treat them in a uniform manner.
    """
    def __init__(self):
        ...
    
    def span(self):
        """
        Return a tuple ``(s, e)``, where ``tokens[s:e]`` is the
        portion of the sentence that is consistent with this
        edge's structure.

        :rtype: tuple(int, int)
        """
        ...
    
    def start(self):
        """
        Return the start index of this edge's span.

        :rtype: int
        """
        ...
    
    def end(self):
        """
        Return the end index of this edge's span.

        :rtype: int
        """
        ...
    
    def length(self):
        """
        Return the length of this edge's span.

        :rtype: int
        """
        ...
    
    def lhs(self):
        """
        Return this edge's left-hand side, which specifies what kind
        of structure is hypothesized by this edge.

        :see: ``TreeEdge`` and ``LeafEdge`` for a description of
            the left-hand side values for each edge type.
        """
        ...
    
    def rhs(self):
        """
        Return this edge's right-hand side, which specifies
        the content of the structure hypothesized by this edge.

        :see: ``TreeEdge`` and ``LeafEdge`` for a description of
            the right-hand side values for each edge type.
        """
        ...
    
    def dot(self):
        """
        Return this edge's dot position, which indicates how much of
        the hypothesized structure is consistent with the
        sentence.  In particular, ``self.rhs[:dot]`` is consistent
        with ``tokens[self.start():self.end()]``.

        :rtype: int
        """
        ...
    
    def nextsym(self):
        """
        Return the element of this edge's right-hand side that
        immediately follows its dot.

        :rtype: Nonterminal or terminal or None
        """
        ...
    
    def is_complete(self):
        """
        Return True if this edge's structure is fully consistent
        with the text.

        :rtype: bool
        """
        ...
    
    def is_incomplete(self):
        """
        Return True if this edge's structure is partially consistent
        with the text.

        :rtype: bool
        """
        ...
    
    def __eq__(self, other):
        ...
    
    def __ne__(self, other):
        ...
    
    def __lt__(self, other):
        ...
    
    def __hash__(self):
        ...
    


@python_2_unicode_compatible
class TreeEdge(EdgeI):
    """
    An edge that records the fact that a tree is (partially)
    consistent with the sentence.  A tree edge consists of:

    - A span, indicating what part of the sentence is
      consistent with the hypothesized tree.
    - A left-hand side, specifying the hypothesized tree's node
      value.
    - A right-hand side, specifying the hypothesized tree's
      children.  Each element of the right-hand side is either a
      terminal, specifying a token with that terminal as its leaf
      value; or a nonterminal, specifying a subtree with that
      nonterminal's symbol as its node value.
    - A dot position, indicating which children are consistent
      with part of the sentence.  In particular, if ``dot`` is the
      dot position, ``rhs`` is the right-hand size, ``(start,end)``
      is the span, and ``sentence`` is the list of tokens in the
      sentence, then ``tokens[start:end]`` can be spanned by the
      children specified by ``rhs[:dot]``.

    For more information about edges, see the ``EdgeI`` interface.
    """
    def __init__(self, span, lhs, rhs, dot=...):
        """
        Construct a new ``TreeEdge``.

        :type span: tuple(int, int)
        :param span: A tuple ``(s, e)``, where ``tokens[s:e]`` is the
            portion of the sentence that is consistent with the new
            edge's structure.
        :type lhs: Nonterminal
        :param lhs: The new edge's left-hand side, specifying the
            hypothesized tree's node value.
        :type rhs: list(Nonterminal and str)
        :param rhs: The new edge's right-hand side, specifying the
            hypothesized tree's children.
        :type dot: int
        :param dot: The position of the new edge's dot.  This position
            specifies what prefix of the production's right hand side
            is consistent with the text.  In particular, if
            ``sentence`` is the list of tokens in the sentence, then
            ``okens[span[0]:span[1]]`` can be spanned by the
            children specified by ``rhs[:dot]``.
        """
        ...
    
    @staticmethod
    def from_production(production, index):
        """
        Return a new ``TreeEdge`` formed from the given production.
        The new edge's left-hand side and right-hand side will
        be taken from ``production``; its span will be
        ``(index,index)``; and its dot position will be ``0``.

        :rtype: TreeEdge
        """
        ...
    
    def move_dot_forward(self, new_end):
        """
        Return a new ``TreeEdge`` formed from this edge.
        The new edge's dot position is increased by ``1``,
        and its end index will be replaced by ``new_end``.

        :param new_end: The new end index.
        :type new_end: int
        :rtype: TreeEdge
        """
        ...
    
    def lhs(self):
        ...
    
    def span(self):
        ...
    
    def start(self):
        ...
    
    def end(self):
        ...
    
    def length(self):
        ...
    
    def rhs(self):
        ...
    
    def dot(self):
        ...
    
    def is_complete(self):
        ...
    
    def is_incomplete(self):
        ...
    
    def nextsym(self):
        ...
    
    def __str__(self):
        ...
    
    def __repr__(self):
        ...
    


@python_2_unicode_compatible
class LeafEdge(EdgeI):
    """
    An edge that records the fact that a leaf value is consistent with
    a word in the sentence.  A leaf edge consists of:

    - An index, indicating the position of the word.
    - A leaf, specifying the word's content.

    A leaf edge's left-hand side is its leaf value, and its right hand
    side is ``()``.  Its span is ``[index, index+1]``, and its dot
    position is ``0``.
    """
    def __init__(self, leaf, index):
        """
        Construct a new ``LeafEdge``.

        :param leaf: The new edge's leaf value, specifying the word
            that is recorded by this edge.
        :param index: The new edge's index, specifying the position of
            the word that is recorded by this edge.
        """
        ...
    
    def lhs(self):
        ...
    
    def span(self):
        ...
    
    def start(self):
        ...
    
    def end(self):
        ...
    
    def length(self):
        ...
    
    def rhs(self):
        ...
    
    def dot(self):
        ...
    
    def is_complete(self):
        ...
    
    def is_incomplete(self):
        ...
    
    def nextsym(self):
        ...
    
    def __str__(self):
        ...
    
    def __repr__(self):
        ...
    


class Chart(object):
    """
    A blackboard for hypotheses about the syntactic constituents of a
    sentence.  A chart contains a set of edges, and each edge encodes
    a single hypothesis about the structure of some portion of the
    sentence.

    The ``select`` method can be used to select a specific collection
    of edges.  For example ``chart.select(is_complete=True, start=0)``
    yields all complete edges whose start indices are 0.  To ensure
    the efficiency of these selection operations, ``Chart`` dynamically
    creates and maintains an index for each set of attributes that
    have been selected on.

    In order to reconstruct the trees that are represented by an edge,
    the chart associates each edge with a set of child pointer lists.
    A child pointer list is a list of the edges that license an
    edge's right-hand side.

    :ivar _tokens: The sentence that the chart covers.
    :ivar _num_leaves: The number of tokens.
    :ivar _edges: A list of the edges in the chart
    :ivar _edge_to_cpls: A dictionary mapping each edge to a set
        of child pointer lists that are associated with that edge.
    :ivar _indexes: A dictionary mapping tuples of edge attributes
        to indices, where each index maps the corresponding edge
        attribute values to lists of edges.
    """
    def __init__(self, tokens):
        """
        Construct a new chart. The chart is initialized with the
        leaf edges corresponding to the terminal leaves.

        :type tokens: list
        :param tokens: The sentence that this chart will be used to parse.
        """
        ...
    
    def initialize(self):
        """
        Clear the chart.
        """
        ...
    
    def num_leaves(self):
        """
        Return the number of words in this chart's sentence.

        :rtype: int
        """
        ...
    
    def leaf(self, index):
        """
        Return the leaf value of the word at the given index.

        :rtype: str
        """
        ...
    
    def leaves(self):
        """
        Return a list of the leaf values of each word in the
        chart's sentence.

        :rtype: list(str)
        """
        ...
    
    def edges(self):
        """
        Return a list of all edges in this chart.  New edges
        that are added to the chart after the call to edges()
        will *not* be contained in this list.

        :rtype: list(EdgeI)
        :see: ``iteredges``, ``select``
        """
        ...
    
    def iteredges(self):
        """
        Return an iterator over the edges in this chart.  It is
        not guaranteed that new edges which are added to the
        chart before the iterator is exhausted will also be generated.

        :rtype: iter(EdgeI)
        :see: ``edges``, ``select``
        """
        ...
    
    __iter__ = ...
    def num_edges(self):
        """
        Return the number of edges contained in this chart.

        :rtype: int
        """
        ...
    
    def select(self, **restrictions):
        """
        Return an iterator over the edges in this chart.  Any
        new edges that are added to the chart before the iterator
        is exahusted will also be generated.  ``restrictions``
        can be used to restrict the set of edges that will be
        generated.

        :param span: Only generate edges ``e`` where ``e.span()==span``
        :param start: Only generate edges ``e`` where ``e.start()==start``
        :param end: Only generate edges ``e`` where ``e.end()==end``
        :param length: Only generate edges ``e`` where ``e.length()==length``
        :param lhs: Only generate edges ``e`` where ``e.lhs()==lhs``
        :param rhs: Only generate edges ``e`` where ``e.rhs()==rhs``
        :param nextsym: Only generate edges ``e`` where
            ``e.nextsym()==nextsym``
        :param dot: Only generate edges ``e`` where ``e.dot()==dot``
        :param is_complete: Only generate edges ``e`` where
            ``e.is_complete()==is_complete``
        :param is_incomplete: Only generate edges ``e`` where
            ``e.is_incomplete()==is_incomplete``
        :rtype: iter(EdgeI)
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
    
    def insert_with_backpointer(self, new_edge, previous_edge, child_edge):
        """
        Add a new edge to the chart, using a pointer to the previous edge.
        """
        ...
    
    def insert(self, edge, *child_pointer_lists):
        """
        Add a new edge to the chart, and return True if this operation
        modified the chart.  In particular, return true iff the chart
        did not already contain ``edge``, or if it did not already associate
        ``child_pointer_lists`` with ``edge``.

        :type edge: EdgeI
        :param edge: The new edge
        :type child_pointer_lists: sequence of tuple(EdgeI)
        :param child_pointer_lists: A sequence of lists of the edges that
            were used to form this edge.  This list is used to reconstruct
            the trees (or partial trees) that are associated with ``edge``.
        :rtype: bool
        """
        ...
    
    def _append_edge(self, edge):
        ...
    
    def parses(self, root, tree_class=...):
        """
        Return an iterator of the complete tree structures that span
        the entire chart, and whose root node is ``root``.
        """
        ...
    
    def trees(self, edge, tree_class=..., complete: bool = ...):
        """
        Return an iterator of the tree structures that are associated
        with ``edge``.

        If ``edge`` is incomplete, then the unexpanded children will be
        encoded as childless subtrees, whose node value is the
        corresponding terminal or nonterminal.

        :rtype: list(Tree)
        :note: If two trees share a common subtree, then the same
            Tree may be used to encode that subtree in
            both trees.  If you need to eliminate this subtree
            sharing, then create a deep copy of each tree.
        """
        ...
    
    def _trees(self, edge, complete, memo, tree_class):
        """
        A helper function for ``trees``.

        :param memo: A dictionary used to record the trees that we've
            generated for each edge, so that when we see an edge more
            than once, we can reuse the same trees.
        """
        ...
    
    def child_pointer_lists(self, edge):
        """
        Return the set of child pointer lists for the given edge.
        Each child pointer list is a list of edges that have
        been used to form this edge.

        :rtype: list(list(EdgeI))
        """
        ...
    
    def pretty_format_edge(self, edge, width: Optional[Any] = ...):
        """
        Return a pretty-printed string representation of a given edge
        in this chart.

        :rtype: str
        :param width: The number of characters allotted to each
            index in the sentence.
        """
        ...
    
    def pretty_format_leaves(self, width: Optional[Any] = ...):
        """
        Return a pretty-printed string representation of this
        chart's leaves.  This string can be used as a header
        for calls to ``pretty_format_edge``.
        """
        ...
    
    def pretty_format(self, width: Optional[Any] = ...):
        """
        Return a pretty-printed string representation of this chart.

        :param width: The number of characters allotted to each
            index in the sentence.
        :rtype: str
        """
        ...
    
    def dot_digraph(self):
        ...
    


class ChartRuleI(object):
    """
    A rule that specifies what new edges are licensed by any given set
    of existing edges.  Each chart rule expects a fixed number of
    edges, as indicated by the class variable ``NUM_EDGES``.  In
    particular:

    - A chart rule with ``NUM_EDGES=0`` specifies what new edges are
      licensed, regardless of existing edges.
    - A chart rule with ``NUM_EDGES=1`` specifies what new edges are
      licensed by a single existing edge.
    - A chart rule with ``NUM_EDGES=2`` specifies what new edges are
      licensed by a pair of existing edges.

    :type NUM_EDGES: int
    :cvar NUM_EDGES: The number of existing edges that this rule uses
        to license new edges.  Typically, this number ranges from zero
        to two.
    """
    def apply(self, chart, grammar, *edges):
        """
        Return a generator that will add edges licensed by this rule
        and the given edges to the chart, one at a time.  Each
        time the generator is resumed, it will either add a new
        edge and yield that edge; or return.

        :type edges: list(EdgeI)
        :param edges: A set of existing edges.  The number of edges
            that should be passed to ``apply()`` is specified by the
            ``NUM_EDGES`` class variable.
        :rtype: iter(EdgeI)
        """
        ...
    
    def apply_everywhere(self, chart, grammar):
        """
        Return a generator that will add all edges licensed by
        this rule, given the edges that are currently in the
        chart, one at a time.  Each time the generator is resumed,
        it will either add a new edge and yield that edge; or return.

        :rtype: iter(EdgeI)
        """
        ...
    


@python_2_unicode_compatible
class AbstractChartRule(ChartRuleI):
    """
    An abstract base class for chart rules.  ``AbstractChartRule``
    provides:

    - A default implementation for ``apply``.
    - A default implementation for ``apply_everywhere``,
      (Currently, this implementation assumes that ``NUM_EDGES``<=3.)
    - A default implementation for ``__str__``, which returns a
      name based on the rule's class name.
    """
    def apply(self, chart, grammar, *edges):
        ...
    
    def apply_everywhere(self, chart, grammar):
        ...
    
    def __str__(self):
        ...
    


class FundamentalRule(AbstractChartRule):
    """
    A rule that joins two adjacent edges to form a single combined
    edge.  In particular, this rule specifies that any pair of edges

    - ``[A -> alpha \* B beta][i:j]``
    - ``[B -> gamma \*][j:k]``

    licenses the edge:

    - ``[A -> alpha B * beta][i:j]``
    """
    NUM_EDGES = ...
    def apply(self, chart, grammar, left_edge, right_edge):
        ...
    


class SingleEdgeFundamentalRule(FundamentalRule):
    """
    A rule that joins a given edge with adjacent edges in the chart,
    to form combined edges.  In particular, this rule specifies that
    either of the edges:

    - ``[A -> alpha \* B beta][i:j]``
    - ``[B -> gamma \*][j:k]``

    licenses the edge:

    - ``[A -> alpha B * beta][i:j]``

    if the other edge is already in the chart.

    :note: This is basically ``FundamentalRule``, with one edge left
        unspecified.
    """
    NUM_EDGES = ...
    def apply(self, chart, grammar, edge):
        ...
    
    def _apply_complete(self, chart, grammar, right_edge):
        ...
    
    def _apply_incomplete(self, chart, grammar, left_edge):
        ...
    


class LeafInitRule(AbstractChartRule):
    NUM_EDGES = ...
    def apply(self, chart, grammar):
        ...
    


class TopDownInitRule(AbstractChartRule):
    """
    A rule licensing edges corresponding to the grammar productions for
    the grammar's start symbol.  In particular, this rule specifies that
    ``[S -> \* alpha][0:i]`` is licensed for each grammar production
    ``S -> alpha``, where ``S`` is the grammar's start symbol.
    """
    NUM_EDGES = ...
    def apply(self, chart, grammar):
        ...
    


class TopDownPredictRule(AbstractChartRule):
    """
    A rule licensing edges corresponding to the grammar productions
    for the nonterminal following an incomplete edge's dot.  In
    particular, this rule specifies that
    ``[A -> alpha \* B beta][i:j]`` licenses the edge
    ``[B -> \* gamma][j:j]`` for each grammar production ``B -> gamma``.

    :note: This rule corresponds to the Predictor Rule in Earley parsing.
    """
    NUM_EDGES = ...
    def apply(self, chart, grammar, edge):
        ...
    


class CachedTopDownPredictRule(TopDownPredictRule):
    """
    A cached version of ``TopDownPredictRule``.  After the first time
    this rule is applied to an edge with a given ``end`` and ``next``,
    it will not generate any more edges for edges with that ``end`` and
    ``next``.

    If ``chart`` or ``grammar`` are changed, then the cache is flushed.
    """
    def __init__(self):
        ...
    
    def apply(self, chart, grammar, edge):
        ...
    


class BottomUpPredictRule(AbstractChartRule):
    """
    A rule licensing any edge corresponding to a production whose
    right-hand side begins with a complete edge's left-hand side.  In
    particular, this rule specifies that ``[A -> alpha \*]`` licenses
    the edge ``[B -> \* A beta]`` for each grammar production ``B -> A beta``.
    """
    NUM_EDGES = ...
    def apply(self, chart, grammar, edge):
        ...
    


class BottomUpPredictCombineRule(BottomUpPredictRule):
    """
    A rule licensing any edge corresponding to a production whose
    right-hand side begins with a complete edge's left-hand side.  In
    particular, this rule specifies that ``[A -> alpha \*]``
    licenses the edge ``[B -> A \* beta]`` for each grammar
    production ``B -> A beta``.

    :note: This is like ``BottomUpPredictRule``, but it also applies
        the ``FundamentalRule`` to the resulting edge.
    """
    NUM_EDGES = ...
    def apply(self, chart, grammar, edge):
        ...
    


class EmptyPredictRule(AbstractChartRule):
    """
    A rule that inserts all empty productions as passive edges,
    in every position in the chart.
    """
    NUM_EDGES = ...
    def apply(self, chart, grammar):
        ...
    


class FilteredSingleEdgeFundamentalRule(SingleEdgeFundamentalRule):
    def _apply_complete(self, chart, grammar, right_edge):
        ...
    
    def _apply_incomplete(self, chart, grammar, left_edge):
        ...
    


class FilteredBottomUpPredictCombineRule(BottomUpPredictCombineRule):
    def apply(self, chart, grammar, edge):
        ...
    


def _bottomup_filter(grammar, nexttoken, rhs, dot=...):
    ...

TD_STRATEGY = [LeafInitRule(), TopDownInitRule(), CachedTopDownPredictRule(), SingleEdgeFundamentalRule()]
BU_STRATEGY = [LeafInitRule(), EmptyPredictRule(), BottomUpPredictRule(), SingleEdgeFundamentalRule()]
BU_LC_STRATEGY = [LeafInitRule(), EmptyPredictRule(), BottomUpPredictCombineRule(), SingleEdgeFundamentalRule()]
LC_STRATEGY = [LeafInitRule(), FilteredBottomUpPredictCombineRule(), FilteredSingleEdgeFundamentalRule()]
class ChartParser(ParserI):
    """
    A generic chart parser.  A "strategy", or list of
    ``ChartRuleI`` instances, is used to decide what edges to add to
    the chart.  In particular, ``ChartParser`` uses the following
    algorithm to parse texts:

    | Until no new edges are added:
    |   For each *rule* in *strategy*:
    |     Apply *rule* to any applicable edges in the chart.
    | Return any complete parses in the chart
    """
    def __init__(self, grammar, strategy=..., trace=..., trace_chart_width=..., use_agenda: bool = ..., chart_class=...):
        """
        Create a new chart parser, that uses ``grammar`` to parse
        texts.

        :type grammar: CFG
        :param grammar: The grammar used to parse texts.
        :type strategy: list(ChartRuleI)
        :param strategy: A list of rules that should be used to decide
            what edges to add to the chart (top-down strategy by default).
        :type trace: int
        :param trace: The level of tracing that should be used when
            parsing a text.  ``0`` will generate no tracing output;
            and higher numbers will produce more verbose tracing
            output.
        :type trace_chart_width: int
        :param trace_chart_width: The default total width reserved for
            the chart in trace output.  The remainder of each line will
            be used to display edges.
        :type use_agenda: bool
        :param use_agenda: Use an optimized agenda-based algorithm,
            if possible.
        :param chart_class: The class that should be used to create
            the parse charts.
        """
        ...
    
    def grammar(self):
        ...
    
    def _trace_new_edges(self, chart, rule, new_edges, trace, edge_width):
        ...
    
    def chart_parse(self, tokens, trace: Optional[Any] = ...):
        """
        Return the final parse ``Chart`` from which all possible
        parse trees can be extracted.

        :param tokens: The sentence to be parsed
        :type tokens: list(str)
        :rtype: Chart
        """
        ...
    
    def parse(self, tokens, tree_class=...):
        ...
    


class TopDownChartParser(ChartParser):
    """
    A ``ChartParser`` using a top-down parsing strategy.
    See ``ChartParser`` for more information.
    """
    def __init__(self, grammar, **parser_args):
        ...
    


class BottomUpChartParser(ChartParser):
    """
    A ``ChartParser`` using a bottom-up parsing strategy.
    See ``ChartParser`` for more information.
    """
    def __init__(self, grammar, **parser_args):
        ...
    


class BottomUpLeftCornerChartParser(ChartParser):
    """
    A ``ChartParser`` using a bottom-up left-corner parsing strategy.
    This strategy is often more efficient than standard bottom-up.
    See ``ChartParser`` for more information.
    """
    def __init__(self, grammar, **parser_args):
        ...
    


class LeftCornerChartParser(ChartParser):
    def __init__(self, grammar, **parser_args):
        ...
    


class SteppingChartParser(ChartParser):
    """
    A ``ChartParser`` that allows you to step through the parsing
    process, adding a single edge at a time.  It also allows you to
    change the parser's strategy or grammar midway through parsing a
    text.

    The ``initialize`` method is used to start parsing a text.  ``step``
    adds a single edge to the chart.  ``set_strategy`` changes the
    strategy used by the chart parser.  ``parses`` returns the set of
    parses that has been found by the chart parser.

    :ivar _restart: Records whether the parser's strategy, grammar,
        or chart has been changed.  If so, then ``step`` must restart
        the parsing algorithm.
    """
    def __init__(self, grammar, strategy=..., trace=...):
        ...
    
    def initialize(self, tokens):
        "Begin parsing the given tokens."
        ...
    
    def step(self):
        """
        Return a generator that adds edges to the chart, one at a
        time.  Each time the generator is resumed, it adds a single
        edge and yields that edge.  If no more edges can be added,
        then it yields None.

        If the parser's strategy, grammar, or chart is changed, then
        the generator will continue adding edges using the new
        strategy, grammar, or chart.

        Note that this generator never terminates, since the grammar
        or strategy might be changed to values that would add new
        edges.  Instead, it yields None when no more edges can be
        added with the current strategy and grammar.
        """
        ...
    
    def _parse(self):
        """
        A generator that implements the actual parsing algorithm.
        ``step`` iterates through this generator, and restarts it
        whenever the parser's strategy, grammar, or chart is modified.
        """
        ...
    
    def strategy(self):
        "Return the strategy used by this parser."
        ...
    
    def grammar(self):
        "Return the grammar used by this parser."
        ...
    
    def chart(self):
        "Return the chart that is used by this parser."
        ...
    
    def current_chartrule(self):
        "Return the chart rule used to generate the most recent edge."
        ...
    
    def parses(self, tree_class=...):
        "Return the parse trees currently contained in the chart."
        ...
    
    def set_strategy(self, strategy):
        """
        Change the strategy that the parser uses to decide which edges
        to add to the chart.

        :type strategy: list(ChartRuleI)
        :param strategy: A list of rules that should be used to decide
            what edges to add to the chart.
        """
        ...
    
    def set_grammar(self, grammar):
        "Change the grammar used by the parser."
        ...
    
    def set_chart(self, chart):
        "Load a given chart into the chart parser."
        ...
    
    def parse(self, tokens, tree_class=...):
        ...
    


def demo_grammar():
    ...

def demo(choice: Optional[Any] = ..., print_times: bool = ..., print_grammar: bool = ..., print_trees: bool = ..., trace=..., sent=..., numparses=...):
    """
    A demonstration of the chart parsers.
    """
    ...

if __name__ == '__main__':
    ...
