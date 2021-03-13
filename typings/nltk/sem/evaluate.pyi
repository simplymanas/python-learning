"""
This type stub file was generated by pyright.
"""

import re
from nltk.compat import python_2_unicode_compatible
from typing import Any, Optional

"""
This module provides data structures for representing first-order
models.
"""
class Error(Exception):
    ...


class Undefined(Error):
    ...


def trace(f, *args, **kw):
    ...

def is_rel(s):
    """
    Check whether a set represents a relation (of any arity).

    :param s: a set containing tuples of str elements
    :type s: set
    :rtype: bool
        """
    ...

def set2rel(s):
    """
    Convert a set containing individuals (strings or numbers) into a set of
    unary tuples. Any tuples of strings already in the set are passed through
    unchanged.

    For example:
      - set(['a', 'b']) => set([('a',), ('b',)])
      - set([3, 27]) => set([('3',), ('27',)])

    :type s: set
    :rtype: set of tuple of str
    """
    ...

def arity(rel):
    """
    Check the arity of a relation.
    :type rel: set of tuples
    :rtype: int of tuple of str
    """
    ...

@python_2_unicode_compatible
class Valuation(dict):
    """
    A dictionary which represents a model-theoretic Valuation of non-logical constants.
    Keys are strings representing the constants to be interpreted, and values correspond
    to individuals (represented as strings) and n-ary relations (represented as sets of tuples
    of strings).

    An instance of ``Valuation`` will raise a KeyError exception (i.e.,
    just behave like a standard  dictionary) if indexed with an expression that
    is not in its list of symbols.
    """
    def __init__(self, xs):
        """
        :param xs: a list of (symbol, value) pairs.
        """
        ...
    
    def __getitem__(self, key):
        ...
    
    def __str__(self):
        ...
    
    @property
    def domain(self):
        """Set-theoretic domain of the value-space of a Valuation."""
        ...
    
    @property
    def symbols(self):
        """The non-logical constants which the Valuation recognizes."""
        ...
    
    @classmethod
    def fromstring(cls, s):
        ...
    


_VAL_SPLIT_RE = re.compile(r'\s*=+>\s*')
_ELEMENT_SPLIT_RE = re.compile(r'\s*,\s*')
_TUPLES_RE = re.compile(r"""\s*
                                (\([^)]+\))  # tuple-expression
                                \s*""", re.VERBOSE)
def _read_valuation_line(s):
    """
    Read a line in a valuation file.

    Lines are expected to be of the form::

      noosa => n
      girl => {g1, g2}
      chase => {(b1, g1), (b2, g1), (g1, d1), (g2, d2)}

    :param s: input line
    :type s: str
    :return: a pair (symbol, value)
    :rtype: tuple
    """
    ...

def read_valuation(s, encoding: Optional[Any] = ...):
    """
    Convert a valuation string into a valuation.

    :param s: a valuation string
    :type s: str
    :param encoding: the encoding of the input string, if it is binary
    :type encoding: str
    :return: a ``nltk.sem`` valuation
    :rtype: Valuation
    """
    ...

@python_2_unicode_compatible
class Assignment(dict):
    """
    A dictionary which represents an assignment of values to variables.

    An assigment can only assign values from its domain.

    If an unknown expression *a* is passed to a model *M*\ 's
    interpretation function *i*, *i* will first check whether *M*\ 's
    valuation assigns an interpretation to *a* as a constant, and if
    this fails, *i* will delegate the interpretation of *a* to
    *g*. *g* only assigns values to individual variables (i.e.,
    members of the class ``IndividualVariableExpression`` in the ``logic``
    module. If a variable is not assigned a value by *g*, it will raise
    an ``Undefined`` exception.

    A variable *Assignment* is a mapping from individual variables to
    entities in the domain. Individual variables are usually indicated
    with the letters ``'x'``, ``'y'``, ``'w'`` and ``'z'``, optionally
    followed by an integer (e.g., ``'x0'``, ``'y332'``).  Assignments are
    created using the ``Assignment`` constructor, which also takes the
    domain as a parameter.

        >>> from nltk.sem.evaluate import Assignment
        >>> dom = set(['u1', 'u2', 'u3', 'u4'])
        >>> g3 = Assignment(dom, [('x', 'u1'), ('y', 'u2')])
        >>> g3 == {'x': 'u1', 'y': 'u2'}
        True

    There is also a ``print`` format for assignments which uses a notation
    closer to that in logic textbooks:

        >>> print(g3)
        g[u1/x][u2/y]

    It is also possible to update an assignment using the ``add`` method:

        >>> dom = set(['u1', 'u2', 'u3', 'u4'])
        >>> g4 = Assignment(dom)
        >>> g4.add('x', 'u1')
        {'x': 'u1'}

    With no arguments, ``purge()`` is equivalent to ``clear()`` on a dictionary:

        >>> g4.purge()
        >>> g4
        {}

    :param domain: the domain of discourse
    :type domain: set
    :param assign: a list of (varname, value) associations
    :type assign: list
    """
    def __init__(self, domain, assign: Optional[Any] = ...):
        self.domain = ...
        self.variant = ...
    
    def __getitem__(self, key):
        ...
    
    def copy(self):
        ...
    
    def purge(self, var: Optional[Any] = ...):
        """
        Remove one or all keys (i.e. logic variables) from an
        assignment, and update ``self.variant``.

        :param var: a Variable acting as a key for the assignment.
        """
        ...
    
    def __str__(self):
        """
        Pretty printing for assignments. {'x', 'u'} appears as 'g[u/x]'
        """
        ...
    
    def _addvariant(self):
        """
        Create a more pretty-printable version of the assignment.
        """
        self.variant = ...
    
    def add(self, var, val):
        """
        Add a new variable-value pair to the assignment, and update
        ``self.variant``.

        """
        ...
    


@python_2_unicode_compatible
class Model(object):
    """
    A first order model is a domain *D* of discourse and a valuation *V*.

    A domain *D* is a set, and a valuation *V* is a map that associates
    expressions with values in the model.
    The domain of *V* should be a subset of *D*.

    Construct a new ``Model``.

    :type domain: set
    :param domain: A set of entities representing the domain of discourse of the model.
    :type valuation: Valuation
    :param valuation: the valuation of the model.
    :param prop: If this is set, then we are building a propositional\
    model and don't require the domain of *V* to be subset of *D*.
    """
    def __init__(self, domain, valuation):
        self.domain = ...
        self.valuation = ...
    
    def __repr__(self):
        ...
    
    def __str__(self):
        ...
    
    def evaluate(self, expr, g, trace: Optional[Any] = ...):
        """
        Read input expressions, and provide a handler for ``satisfy``
        that blocks further propagation of the ``Undefined`` error.
        :param expr: An ``Expression`` of ``logic``.
        :type g: Assignment
        :param g: an assignment to individual variables.
        :rtype: bool or 'Undefined'
        """
        ...
    
    def satisfy(self, parsed, g, trace: Optional[Any] = ...):
        """
        Recursive interpretation function for a formula of first-order logic.

        Raises an ``Undefined`` error when ``parsed`` is an atomic string
        but is not a symbol or an individual variable.

        :return: Returns a truth value or ``Undefined`` if ``parsed`` is\
        complex, and calls the interpretation function ``i`` if ``parsed``\
        is atomic.

        :param parsed: An expression of ``logic``.
        :type g: Assignment
        :param g: an assignment to individual variables.
        """
        ...
    
    def i(self, parsed, g, trace: bool = ...):
        """
        An interpretation function.

        Assuming that ``parsed`` is atomic:

        - if ``parsed`` is a non-logical constant, calls the valuation *V*
        - else if ``parsed`` is an individual variable, calls assignment *g*
        - else returns ``Undefined``.

        :param parsed: an ``Expression`` of ``logic``.
        :type g: Assignment
        :param g: an assignment to individual variables.
        :return: a semantic value
        """
        ...
    
    def satisfiers(self, parsed, varex, g, trace: Optional[Any] = ..., nesting=...):
        """
        Generate the entities from the model's domain that satisfy an open formula.

        :param parsed: an open formula
        :type parsed: Expression
        :param varex: the relevant free individual variable in ``parsed``.
        :type varex: VariableExpression or str
        :param g: a variable assignment
        :type g:  Assignment
        :return: a set of the entities that satisfy ``parsed``.
        """
        ...
    


mult = 30
def propdemo(trace: Optional[Any] = ...):
    """Example of a propositional model."""
    ...

def folmodel(quiet: bool = ..., trace: Optional[Any] = ...):
    """Example of a first-order model."""
    ...

def foldemo(trace: Optional[Any] = ...):
    """
    Interpretation of closed expressions in a first-order model.
    """
    ...

def satdemo(trace: Optional[Any] = ...):
    """Satisfiers of an open formula in a first order model."""
    ...

def demo(num=..., trace: Optional[Any] = ...):
    """
    Run exists demos.

     - num = 1: propositional logic demo
     - num = 2: first order model demo (only if trace is set)
     - num = 3: first order sentences demo
     - num = 4: satisfaction of open formulas demo
     - any other value: run all the demos

    :param trace: trace = 1, or trace = 2 for more verbose tracing
    """
    ...

if __name__ == "__main__":
    ...