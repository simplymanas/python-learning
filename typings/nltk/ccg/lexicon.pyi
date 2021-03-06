"""
This type stub file was generated by pyright.
"""

import re
from nltk.compat import python_2_unicode_compatible
from nltk.internals import deprecated
from typing import Any, Optional

"""
CCG Lexicons
"""
PRIM_RE = re.compile(r'''([A-Za-z]+)(\[[A-Za-z,]+\])?''')
NEXTPRIM_RE = re.compile(r'''([A-Za-z]+(?:\[[A-Za-z,]+\])?)(.*)''')
APP_RE = re.compile(r'''([\\/])([.,]?)([.,]?)(.*)''')
LEX_RE = re.compile(r'''([\S_]+)\s*(::|[-=]+>)\s*(.+)''', re.UNICODE)
RHS_RE = re.compile(r'''([^{}]*[^ {}])\s*(\{[^}]+\})?''', re.UNICODE)
SEMANTICS_RE = re.compile(r'''\{([^}]+)\}''', re.UNICODE)
COMMENTS_RE = re.compile('''([^#]*)(?:#.*)?''')
class Token(object):
    """
    Class representing a token.

    token => category {semantics}
    e.g. eat => S\\var[pl]/var {\\x y.eat(x,y)}

    * `token` (string)
    * `categ` (string)
    * `semantics` (Expression)
    """
    def __init__(self, token, categ, semantics: Optional[Any] = ...):
        ...
    
    def categ(self):
        ...
    
    def semantics(self):
        ...
    
    def __str__(self):
        ...
    
    def __cmp__(self, other):
        ...
    


@python_2_unicode_compatible
class CCGLexicon(object):
    """
    Class representing a lexicon for CCG grammars.

    * `primitives`: The list of primitive categories for the lexicon
    * `families`: Families of categories
    * `entries`: A mapping of words to possible categories
    """
    def __init__(self, start, primitives, families, entries):
        ...
    
    def categories(self, word):
        """
        Returns all the possible categories for a word
        """
        ...
    
    def start(self):
        """
        Return the target category for the parser
        """
        ...
    
    def __str__(self):
        """
        String representation of the lexicon. Used for debugging.
        """
        ...
    


def matchBrackets(string):
    """
    Separate the contents matching the first set of brackets from the rest of
    the input.
    """
    ...

def nextCategory(string):
    """
    Separate the string for the next portion of the category from the rest
    of the string
    """
    ...

def parseApplication(app):
    """
    Parse an application operator
    """
    ...

def parseSubscripts(subscr):
    """
    Parse the subscripts for a primitive category
    """
    ...

def parsePrimitiveCategory(chunks, primitives, families, var):
    """
    Parse a primitive category

    If the primitive is the special category 'var', replace it with the
    correct `CCGVar`.
    """
    ...

def augParseCategory(line, primitives, families, var: Optional[Any] = ...):
    """
    Parse a string representing a category, and returns a tuple with
    (possibly) the CCG variable for the category
    """
    ...

def fromstring(lex_str, include_semantics: bool = ...):
    """
    Convert string representation into a lexicon for CCGs.
    """
    ...

@deprecated('Use fromstring() instead.')
def parseLexicon(lex_str):
    ...

openccg_tinytiny = fromstring("""
    # Rather minimal lexicon based on the openccg `tinytiny' grammar.
    # Only incorporates a subset of the morphological subcategories, however.
    :- S,NP,N                    # Primitive categories
    Det :: NP/N                  # Determiners
    Pro :: NP
    IntransVsg :: S\\NP[sg]    # Tensed intransitive verbs (singular)
    IntransVpl :: S\\NP[pl]    # Plural
    TransVsg :: S\\NP[sg]/NP   # Tensed transitive verbs (singular)
    TransVpl :: S\\NP[pl]/NP   # Plural

    the => NP[sg]/N[sg]
    the => NP[pl]/N[pl]

    I => Pro
    me => Pro
    we => Pro
    us => Pro

    book => N[sg]
    books => N[pl]

    peach => N[sg]
    peaches => N[pl]

    policeman => N[sg]
    policemen => N[pl]

    boy => N[sg]
    boys => N[pl]

    sleep => IntransVsg
    sleep => IntransVpl

    eat => IntransVpl
    eat => TransVpl
    eats => IntransVsg
    eats => TransVsg

    see => TransVpl
    sees => TransVsg
    """)
