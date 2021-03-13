"""
This type stub file was generated by pyright.
"""

from functools import total_ordering
from nltk.internals import Counter
from nltk.compat import python_2_unicode_compatible
from typing import Any, Optional

"""
A version of first order predicate logic, built on
top of the typed lambda calculus.
"""
APP = 'APP'
_counter = Counter()
class Tokens(object):
    LAMBDA = ...
    LAMBDA_LIST = ...
    EXISTS = ...
    EXISTS_LIST = ...
    ALL = ...
    ALL_LIST = ...
    DOT = ...
    OPEN = ...
    CLOSE = ...
    COMMA = ...
    NOT = ...
    NOT_LIST = ...
    AND = ...
    AND_LIST = ...
    OR = ...
    OR_LIST = ...
    IMP = ...
    IMP_LIST = ...
    IFF = ...
    IFF_LIST = ...
    EQ = ...
    EQ_LIST = ...
    NEQ = ...
    NEQ_LIST = ...
    BINOPS = ...
    QUANTS = ...
    PUNCT = ...
    TOKENS = ...
    SYMBOLS = ...


def boolean_ops():
    """
    Boolean operators
    """
    ...

def equality_preds():
    """
    Equality predicates
    """
    ...

def binding_ops():
    """
    Binding operators
    """
    ...

@python_2_unicode_compatible
class LogicParser(object):
    """A lambda calculus expression parser."""
    def __init__(self, type_check: bool = ...):
        """
        :param type_check: bool should type checking be performed?
        to their types.
        """
        self.type_check = ...
        self.quote_chars = ...
        self.operator_precedence = ...
        self.right_associated_operations = ...
    
    def parse(self, data, signature: Optional[Any] = ...):
        """
        Parse the expression.

        :param data: str for the input to be parsed
        :param signature: ``dict<str, str>`` that maps variable names to type
        strings
        :returns: a parsed Expression
        """
        ...
    
    def process(self, data):
        """Split the data into tokens"""
        ...
    
    def process_quoted_token(self, data_idx, data):
        ...
    
    def get_all_symbols(self):
        """This method exists to be overridden"""
        ...
    
    def inRange(self, location):
        """Return TRUE if the given location is within the buffer"""
        ...
    
    def token(self, location: Optional[Any] = ...):
        """Get the next waiting token.  If a location is given, then
        return the token at currentIndex+location without advancing
        currentIndex; setting it gives lookahead/lookback capability."""
        ...
    
    def isvariable(self, tok):
        ...
    
    def process_next_expression(self, context):
        """Parse the next complete expression from the stream and return it."""
        ...
    
    def handle(self, tok, context):
        """This method is intended to be overridden for logics that
        use different operators or expressions"""
        ...
    
    def attempt_adjuncts(self, expression, context):
        ...
    
    def handle_negation(self, tok, context):
        ...
    
    def make_NegatedExpression(self, expression):
        ...
    
    def handle_variable(self, tok, context):
        ...
    
    def get_next_token_variable(self, description):
        ...
    
    def handle_lambda(self, tok, context):
        ...
    
    def handle_quant(self, tok, context):
        ...
    
    def get_QuantifiedExpression_factory(self, tok):
        """This method serves as a hook for other logic parsers that
        have different quantifiers"""
        ...
    
    def make_QuanifiedExpression(self, factory, variable, term):
        ...
    
    def handle_open(self, tok, context):
        ...
    
    def attempt_EqualityExpression(self, expression, context):
        """Attempt to make an equality expression.  If the next token is an
        equality operator, then an EqualityExpression will be returned.
        Otherwise, the parameter will be returned."""
        ...
    
    def make_EqualityExpression(self, first, second):
        """This method serves as a hook for other logic parsers that
        have different equality expression classes"""
        ...
    
    def attempt_BooleanExpression(self, expression, context):
        """Attempt to make a boolean expression.  If the next token is a boolean
        operator, then a BooleanExpression will be returned.  Otherwise, the
        parameter will be returned."""
        ...
    
    def get_BooleanExpression_factory(self, tok):
        """This method serves as a hook for other logic parsers that
        have different boolean operators"""
        ...
    
    def make_BooleanExpression(self, factory, first, second):
        ...
    
    def attempt_ApplicationExpression(self, expression, context):
        """Attempt to make an application expression.  The next tokens are
        a list of arguments in parens, then the argument expression is a
        function being applied to the arguments.  Otherwise, return the
        argument expression."""
        ...
    
    def make_ApplicationExpression(self, function, argument):
        ...
    
    def make_VariableExpression(self, name):
        ...
    
    def make_LambdaExpression(self, variable, term):
        ...
    
    def has_priority(self, operation, context):
        ...
    
    def assertNextToken(self, expected):
        ...
    
    def assertToken(self, tok, expected):
        ...
    
    def __repr__(self):
        ...
    


def read_logic(s, logic_parser: Optional[Any] = ..., encoding: Optional[Any] = ...):
    """
    Convert a file of First Order Formulas into a list of {Expression}s.

    :param s: the contents of the file
    :type s: str
    :param logic_parser: The parser to be used to parse the logical expression
    :type logic_parser: LogicParser
    :param encoding: the encoding of the input string, if it is binary
    :type encoding: str
    :return: a list of parsed formulas.
    :rtype: list(Expression)
    """
    ...

@total_ordering
@python_2_unicode_compatible
class Variable(object):
    def __init__(self, name):
        """
        :param name: the name of the variable
        """
        self.name = ...
    
    def __eq__(self, other):
        ...
    
    def __ne__(self, other):
        ...
    
    def __lt__(self, other):
        ...
    
    def substitute_bindings(self, bindings):
        ...
    
    def __hash__(self):
        ...
    
    def __str__(self):
        ...
    
    def __repr__(self):
        ...
    


def unique_variable(pattern: Optional[Any] = ..., ignore: Optional[Any] = ...):
    """
    Return a new, unique variable.

    :param pattern: ``Variable`` that is being replaced.  The new variable must
        be the same type.
    :param term: a set of ``Variable`` objects that should not be returned from
        this function.
    :rtype: Variable
    """
    ...

def skolem_function(univ_scope: Optional[Any] = ...):
    """
    Return a skolem function over the variables in univ_scope
    param univ_scope
    """
    ...

@python_2_unicode_compatible
class Type(object):
    def __repr__(self):
        ...
    
    def __hash__(self):
        ...
    
    @classmethod
    def fromstring(cls, s):
        ...
    


@python_2_unicode_compatible
class ComplexType(Type):
    def __init__(self, first, second):
        self.first = ...
        self.second = ...
    
    def __eq__(self, other):
        ...
    
    def __ne__(self, other):
        ...
    
    __hash__ = ...
    def matches(self, other):
        ...
    
    def resolve(self, other):
        ...
    
    def __str__(self):
        ...
    
    def str(self):
        ...
    


class BasicType(Type):
    def __eq__(self, other):
        ...
    
    def __ne__(self, other):
        ...
    
    __hash__ = ...
    def matches(self, other):
        ...
    
    def resolve(self, other):
        ...
    


@python_2_unicode_compatible
class EntityType(BasicType):
    def __str__(self):
        ...
    
    def str(self):
        ...
    


@python_2_unicode_compatible
class TruthValueType(BasicType):
    def __str__(self):
        ...
    
    def str(self):
        ...
    


@python_2_unicode_compatible
class EventType(BasicType):
    def __str__(self):
        ...
    
    def str(self):
        ...
    


@python_2_unicode_compatible
class AnyType(BasicType, ComplexType):
    def __init__(self):
        ...
    
    @property
    def first(self):
        ...
    
    @property
    def second(self):
        ...
    
    def __eq__(self, other):
        ...
    
    def __ne__(self, other):
        ...
    
    __hash__ = ...
    def matches(self, other):
        ...
    
    def resolve(self, other):
        ...
    
    def __str__(self):
        ...
    
    def str(self):
        ...
    


TRUTH_TYPE = TruthValueType()
ENTITY_TYPE = EntityType()
EVENT_TYPE = EventType()
ANY_TYPE = AnyType()
def read_type(type_string):
    ...

class TypeException(Exception):
    def __init__(self, msg):
        ...
    


class InconsistentTypeHierarchyException(TypeException):
    def __init__(self, variable, expression: Optional[Any] = ...):
        ...
    


class TypeResolutionException(TypeException):
    def __init__(self, expression, other_type):
        ...
    


class IllegalTypeException(TypeException):
    def __init__(self, expression, other_type, allowed_type):
        ...
    


def typecheck(expressions, signature: Optional[Any] = ...):
    """
    Ensure correct typing across a collection of ``Expression`` objects.
    :param expressions: a collection of expressions
    :param signature: dict that maps variable names to types (or string
    representations of types)
    """
    ...

class SubstituteBindingsI(object):
    """
    An interface for classes that can perform substitutions for
    variables.
    """
    def substitute_bindings(self, bindings):
        """
        :return: The object that is obtained by replacing
            each variable bound by ``bindings`` with its values.
            Aliases are already resolved. (maybe?)
        :rtype: (any)
        """
        ...
    
    def variables(self):
        """
        :return: A list of all variables in this object.
        """
        ...
    


@python_2_unicode_compatible
class Expression(SubstituteBindingsI):
    """This is the base abstract object for all logical expressions"""
    _logic_parser = ...
    _type_checking_logic_parser = ...
    @classmethod
    def fromstring(cls, s, type_check: bool = ..., signature: Optional[Any] = ...):
        ...
    
    def __call__(self, other, *additional):
        ...
    
    def applyto(self, other):
        ...
    
    def __neg__(self):
        ...
    
    def negate(self):
        """If this is a negated expression, remove the negation.
        Otherwise add a negation."""
        ...
    
    def __and__(self, other):
        ...
    
    def __or__(self, other):
        ...
    
    def __gt__(self, other):
        ...
    
    def __lt__(self, other):
        ...
    
    def __eq__(self, other):
        ...
    
    def __ne__(self, other):
        ...
    
    def equiv(self, other, prover: Optional[Any] = ...):
        """
        Check for logical equivalence.
        Pass the expression (self <-> other) to the theorem prover.
        If the prover says it is valid, then the self and other are equal.

        :param other: an ``Expression`` to check equality against
        :param prover: a ``nltk.inference.api.Prover``
        """
        ...
    
    def __hash__(self):
        ...
    
    def substitute_bindings(self, bindings):
        ...
    
    def typecheck(self, signature: Optional[Any] = ...):
        """
        Infer and check types.  Raise exceptions if necessary.

        :param signature: dict that maps variable names to types (or string
            representations of types)
        :return: the signature, plus any additional type mappings
        """
        ...
    
    def findtype(self, variable):
        """
        Find the type of the given variable as it is used in this expression.
        For example, finding the type of "P" in "P(x) & Q(x,y)" yields "<e,t>"

        :param variable: Variable
        """
        ...
    
    def _set_type(self, other_type=..., signature: Optional[Any] = ...):
        """
        Set the type of this expression to be the given type.  Raise type
        exceptions where applicable.

        :param other_type: Type
        :param signature: dict(str -> list(AbstractVariableExpression))
        """
        ...
    
    def replace(self, variable, expression, replace_bound: bool = ..., alpha_convert: bool = ...):
        """
        Replace every instance of 'variable' with 'expression'
        :param variable: ``Variable`` The variable to replace
        :param expression: ``Expression`` The expression with which to replace it
        :param replace_bound: bool Should bound variables be replaced?
        :param alpha_convert: bool Alpha convert automatically to avoid name clashes?
        """
        ...
    
    def normalize(self, newvars: Optional[Any] = ...):
        """Rename auto-generated unique variables"""
        ...
    
    def visit(self, function, combinator):
        """
        Recursively visit subexpressions.  Apply 'function' to each
        subexpression and pass the result of each function application
        to the 'combinator' for aggregation:

            return combinator(map(function, self.subexpressions))

        Bound variables are neither applied upon by the function nor given to
        the combinator.
        :param function: ``Function<Expression,T>`` to call on each subexpression
        :param combinator: ``Function<list<T>,R>`` to combine the results of the
        function calls
        :return: result of combination ``R``
        """
        ...
    
    def visit_structured(self, function, combinator):
        """
        Recursively visit subexpressions.  Apply 'function' to each
        subexpression and pass the result of each function application
        to the 'combinator' for aggregation.  The combinator must have
        the same signature as the constructor.  The function is not
        applied to bound variables, but they are passed to the
        combinator.
        :param function: ``Function`` to call on each subexpression
        :param combinator: ``Function`` with the same signature as the
        constructor, to combine the results of the function calls
        :return: result of combination
        """
        ...
    
    def __repr__(self):
        ...
    
    def __str__(self):
        ...
    
    def variables(self):
        """
        Return a set of all the variables for binding substitution.
        The variables returned include all free (non-bound) individual
        variables and any variable starting with '?' or '@'.
        :return: set of ``Variable`` objects
        """
        ...
    
    def free(self):
        """
        Return a set of all the free (non-bound) variables.  This includes
        both individual and predicate variables, but not constants.
        :return: set of ``Variable`` objects
        """
        ...
    
    def constants(self):
        """
        Return a set of individual constants (non-predicates).
        :return: set of ``Variable`` objects
        """
        ...
    
    def predicates(self):
        """
        Return a set of predicates (constants, not variables).
        :return: set of ``Variable`` objects
        """
        ...
    
    def simplify(self):
        """
        :return: beta-converted version of this expression
        """
        ...
    
    def make_VariableExpression(self, variable):
        ...
    


@python_2_unicode_compatible
class ApplicationExpression(Expression):
    r"""
    This class is used to represent two related types of logical expressions.

    The first is a Predicate Expression, such as "P(x,y)".  A predicate
    expression is comprised of a ``FunctionVariableExpression`` or
    ``ConstantExpression`` as the predicate and a list of Expressions as the
    arguments.

    The second is a an application of one expression to another, such as
    "(\x.dog(x))(fido)".

    The reason Predicate Expressions are treated as Application Expressions is
    that the Variable Expression predicate of the expression may be replaced
    with another Expression, such as a LambdaExpression, which would mean that
    the Predicate should be thought of as being applied to the arguments.

    The logical expression reader will always curry arguments in a application expression.
    So, "\x y.see(x,y)(john,mary)" will be represented internally as
    "((\x y.(see(x))(y))(john))(mary)".  This simplifies the internals since
    there will always be exactly one argument in an application.

    The str() method will usually print the curried forms of application
    expressions.  The one exception is when the the application expression is
    really a predicate expression (ie, underlying function is an
    ``AbstractVariableExpression``).  This means that the example from above
    will be returned as "(\x y.see(x,y)(john))(mary)".
    """
    def __init__(self, function, argument):
        """
        :param function: ``Expression``, for the function expression
        :param argument: ``Expression``, for the argument
        """
        self.function = ...
        self.argument = ...
    
    def simplify(self):
        ...
    
    @property
    def type(self):
        ...
    
    def _set_type(self, other_type=..., signature: Optional[Any] = ...):
        """:see Expression._set_type()"""
        ...
    
    def findtype(self, variable):
        """:see Expression.findtype()"""
        ...
    
    def constants(self):
        """:see: Expression.constants()"""
        ...
    
    def predicates(self):
        """:see: Expression.predicates()"""
        ...
    
    def visit(self, function, combinator):
        """:see: Expression.visit()"""
        ...
    
    def __eq__(self, other):
        ...
    
    def __ne__(self, other):
        ...
    
    __hash__ = ...
    def __str__(self):
        ...
    
    def uncurry(self):
        """
        Uncurry this application expression

        return: A tuple (base-function, arg-list)
        """
        ...
    
    @property
    def pred(self):
        """
        Return uncurried base-function.
        If this is an atom, then the result will be a variable expression.
        Otherwise, it will be a lambda expression.
        """
        ...
    
    @property
    def args(self):
        """
        Return uncurried arg-list
        """
        ...
    
    def is_atom(self):
        """
        Is this expression an atom (as opposed to a lambda expression applied
        to a term)?
        """
        ...
    


@total_ordering
@python_2_unicode_compatible
class AbstractVariableExpression(Expression):
    """This class represents a variable to be used as a predicate or entity"""
    def __init__(self, variable):
        """
        :param variable: ``Variable``, for the variable
        """
        self.variable = ...
    
    def simplify(self):
        ...
    
    def replace(self, variable, expression, replace_bound: bool = ..., alpha_convert: bool = ...):
        """:see: Expression.replace()"""
        ...
    
    def _set_type(self, other_type=..., signature: Optional[Any] = ...):
        """:see Expression._set_type()"""
        ...
    
    def findtype(self, variable):
        """:see Expression.findtype()"""
        ...
    
    def predicates(self):
        """:see: Expression.predicates()"""
        ...
    
    def __eq__(self, other):
        """Allow equality between instances of ``AbstractVariableExpression``
        subtypes."""
        ...
    
    def __ne__(self, other):
        ...
    
    def __lt__(self, other):
        ...
    
    __hash__ = ...
    def __str__(self):
        ...
    


class IndividualVariableExpression(AbstractVariableExpression):
    """This class represents variables that take the form of a single lowercase
    character (other than 'e') followed by zero or more digits."""
    def _set_type(self, other_type=..., signature: Optional[Any] = ...):
        """:see Expression._set_type()"""
        ...
    
    def _get_type(self):
        ...
    
    type = ...
    def free(self):
        """:see: Expression.free()"""
        ...
    
    def constants(self):
        """:see: Expression.constants()"""
        ...
    


class FunctionVariableExpression(AbstractVariableExpression):
    """This class represents variables that take the form of a single uppercase
    character followed by zero or more digits."""
    type = ...
    def free(self):
        """:see: Expression.free()"""
        ...
    
    def constants(self):
        """:see: Expression.constants()"""
        ...
    


class EventVariableExpression(IndividualVariableExpression):
    """This class represents variables that take the form of a single lowercase
    'e' character followed by zero or more digits."""
    type = ...


class ConstantExpression(AbstractVariableExpression):
    """This class represents variables that do not take the form of a single
    character followed by zero or more digits."""
    type = ...
    def _set_type(self, other_type=..., signature: Optional[Any] = ...):
        """:see Expression._set_type()"""
        ...
    
    def free(self):
        """:see: Expression.free()"""
        ...
    
    def constants(self):
        """:see: Expression.constants()"""
        ...
    


def VariableExpression(variable):
    """
    This is a factory method that instantiates and returns a subtype of
    ``AbstractVariableExpression`` appropriate for the given variable.
    """
    ...

class VariableBinderExpression(Expression):
    """This an abstract class for any Expression that binds a variable in an
    Expression.  This includes LambdaExpressions and Quantified Expressions"""
    def __init__(self, variable, term):
        """
        :param variable: ``Variable``, for the variable
        :param term: ``Expression``, for the term
        """
        self.variable = ...
        self.term = ...
    
    def replace(self, variable, expression, replace_bound: bool = ..., alpha_convert: bool = ...):
        """:see: Expression.replace()"""
        ...
    
    def alpha_convert(self, newvar):
        """Rename all occurrences of the variable introduced by this variable
        binder in the expression to ``newvar``.
        :param newvar: ``Variable``, for the new variable
        """
        ...
    
    def free(self):
        """:see: Expression.free()"""
        ...
    
    def findtype(self, variable):
        """:see Expression.findtype()"""
        ...
    
    def visit(self, function, combinator):
        """:see: Expression.visit()"""
        ...
    
    def visit_structured(self, function, combinator):
        """:see: Expression.visit_structured()"""
        ...
    
    def __eq__(self, other):
        r"""Defines equality modulo alphabetic variance.  If we are comparing
        \x.M  and \y.N, then check equality of M and N[x/y]."""
        ...
    
    def __ne__(self, other):
        ...
    
    __hash__ = ...


@python_2_unicode_compatible
class LambdaExpression(VariableBinderExpression):
    @property
    def type(self):
        ...
    
    def _set_type(self, other_type=..., signature: Optional[Any] = ...):
        """:see Expression._set_type()"""
        ...
    
    def __str__(self):
        ...
    


@python_2_unicode_compatible
class QuantifiedExpression(VariableBinderExpression):
    @property
    def type(self):
        ...
    
    def _set_type(self, other_type=..., signature: Optional[Any] = ...):
        """:see Expression._set_type()"""
        ...
    
    def __str__(self):
        ...
    


class ExistsExpression(QuantifiedExpression):
    def getQuantifier(self):
        ...
    


class AllExpression(QuantifiedExpression):
    def getQuantifier(self):
        ...
    


@python_2_unicode_compatible
class NegatedExpression(Expression):
    def __init__(self, term):
        self.term = ...
    
    @property
    def type(self):
        ...
    
    def _set_type(self, other_type=..., signature: Optional[Any] = ...):
        """:see Expression._set_type()"""
        ...
    
    def findtype(self, variable):
        ...
    
    def visit(self, function, combinator):
        """:see: Expression.visit()"""
        ...
    
    def negate(self):
        """:see: Expression.negate()"""
        ...
    
    def __eq__(self, other):
        ...
    
    def __ne__(self, other):
        ...
    
    __hash__ = ...
    def __str__(self):
        ...
    


@python_2_unicode_compatible
class BinaryExpression(Expression):
    def __init__(self, first, second):
        self.first = ...
        self.second = ...
    
    @property
    def type(self):
        ...
    
    def findtype(self, variable):
        """:see Expression.findtype()"""
        ...
    
    def visit(self, function, combinator):
        """:see: Expression.visit()"""
        ...
    
    def __eq__(self, other):
        ...
    
    def __ne__(self, other):
        ...
    
    __hash__ = ...
    def __str__(self):
        ...
    
    def _str_subex(self, subex):
        ...
    


class BooleanExpression(BinaryExpression):
    def _set_type(self, other_type=..., signature: Optional[Any] = ...):
        """:see Expression._set_type()"""
        ...
    


class AndExpression(BooleanExpression):
    """This class represents conjunctions"""
    def getOp(self):
        ...
    
    def _str_subex(self, subex):
        ...
    


class OrExpression(BooleanExpression):
    """This class represents disjunctions"""
    def getOp(self):
        ...
    
    def _str_subex(self, subex):
        ...
    


class ImpExpression(BooleanExpression):
    """This class represents implications"""
    def getOp(self):
        ...
    


class IffExpression(BooleanExpression):
    """This class represents biconditionals"""
    def getOp(self):
        ...
    


class EqualityExpression(BinaryExpression):
    """This class represents equality expressions like "(x = y)"."""
    def _set_type(self, other_type=..., signature: Optional[Any] = ...):
        """:see Expression._set_type()"""
        ...
    
    def getOp(self):
        ...
    


class LogicalExpressionException(Exception):
    def __init__(self, index, message):
        self.index = ...
    


class UnexpectedTokenException(LogicalExpressionException):
    def __init__(self, index, unexpected: Optional[Any] = ..., expected: Optional[Any] = ..., message: Optional[Any] = ...):
        ...
    


class ExpectedMoreTokensException(LogicalExpressionException):
    def __init__(self, index, message: Optional[Any] = ...):
        ...
    


def is_indvar(expr):
    """
    An individual variable must be a single lowercase character other than 'e',
    followed by zero or more digits.

    :param expr: str
    :return: bool True if expr is of the correct form
    """
    ...

def is_funcvar(expr):
    """
    A function variable must be a single uppercase character followed by
    zero or more digits.

    :param expr: str
    :return: bool True if expr is of the correct form
    """
    ...

def is_eventvar(expr):
    """
    An event variable must be a single lowercase 'e' character followed by
    zero or more digits.

    :param expr: str
    :return: bool True if expr is of the correct form
    """
    ...

def demo():
    ...

def demo_errors():
    ...

def demoException(s):
    ...

def printtype(ex):
    ...

if __name__ == '__main__':
    ...
