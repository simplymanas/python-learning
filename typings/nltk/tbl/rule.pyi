"""
This type stub file was generated by pyright.
"""

from abc import ABCMeta, abstractmethod
from six import add_metaclass
from nltk.compat import python_2_unicode_compatible
from nltk import jsontags
from typing import Any, Optional

@add_metaclass(ABCMeta)
class TagRule(object):
    """
    An interface for tag transformations on a tagged corpus, as
    performed by tbl taggers.  Each transformation finds all tokens
    in the corpus that are tagged with a specific original tag and
    satisfy a specific condition, and replaces their tags with a
    replacement tag.  For any given transformation, the original
    tag, replacement tag, and condition are fixed.  Conditions may
    depend on the token under consideration, as well as any other
    tokens in the corpus.

    Tag rules must be comparable and hashable.
    """
    def __init__(self, original_tag, replacement_tag):
        self.original_tag = ...
        self.replacement_tag = ...
    
    def apply(self, tokens, positions: Optional[Any] = ...):
        """
        Apply this rule at every position in positions where it
        applies to the given sentence.  I.e., for each position p
        in *positions*, if *tokens[p]* is tagged with this rule's
        original tag, and satisfies this rule's condition, then set
        its tag to be this rule's replacement tag.

        :param tokens: The tagged sentence
        :type tokens: list(tuple(str, str))
        :type positions: list(int)
        :param positions: The positions where the transformation is to
            be tried.  If not specified, try it at all positions.
        :return: The indices of tokens whose tags were changed by this
            rule.
        :rtype: int
        """
        ...
    
    @abstractmethod
    def applies(self, tokens, index):
        """
        :return: True if the rule would change the tag of
            ``tokens[index]``, False otherwise
        :rtype: bool
        :param tokens: A tagged sentence
        :type tokens: list(str)
        :param index: The index to check
        :type index: int
        """
        ...
    
    def __eq__(self, other):
        ...
    
    def __ne__(self, other):
        ...
    
    def __hash__(self):
        ...
    


@python_2_unicode_compatible
@jsontags.register_tag
class Rule(TagRule):
    """
    A Rule checks the current corpus position for a certain set of conditions;
    if they are all fulfilled, the Rule is triggered, meaning that it
    will change tag A to tag B. For other tags than A, nothing happens.

    The conditions are parameters to the Rule instance. Each condition is a feature-value pair,
    with a set of positions to check for the value of the corresponding feature.
    Conceptually, the positions are joined by logical OR, and the feature set by logical AND.

    More formally, the Rule is then applicable to the M{n}th token iff:

      - The M{n}th token is tagged with the Rule's original tag; and
      - For each (Feature(positions), M{value}) tuple:
        - The value of Feature of at least one token in {n+p for p in positions}
          is M{value}.

    """
    json_tag = ...
    def __init__(self, templateid, original_tag, replacement_tag, conditions):
        """
        Construct a new Rule that changes a token's tag from
        C{original_tag} to C{replacement_tag} if all of the properties
        specified in C{conditions} hold.

        @type templateid: string
        @param templateid: the template id (a zero-padded string, '001' etc,
          so it will sort nicely)

        @type conditions: C{iterable} of C{Feature}
        @param conditions: A list of Feature(positions),
            each of which specifies that the property (computed by
            Feature.extract_property()) of at least one
            token in M{n} + p in positions is C{value}.

        """
        self.templateid = ...
    
    def encode_json_obj(self):
        ...
    
    @classmethod
    def decode_json_obj(cls, obj):
        ...
    
    def applies(self, tokens, index):
        ...
    
    def __eq__(self, other):
        ...
    
    def __ne__(self, other):
        ...
    
    def __hash__(self):
        ...
    
    def __repr__(self):
        ...
    
    def __str__(self):
        ...
    
    def format(self, fmt):
        """
        Return a string representation of this rule.

        >>> from nltk.tbl.rule import Rule
        >>> from nltk.tag.brill import Pos

        >>> r = Rule("23", "VB", "NN", [(Pos([-2,-1]), 'DT')])

        r.format("str") == str(r)
        True
        >>> r.format("str")
        'VB->NN if Pos:DT@[-2,-1]'

        r.format("repr") == repr(r)
        True
        >>> r.format("repr")
        "Rule('23', 'VB', 'NN', [(Pos([-2, -1]),'DT')])"

        >>> r.format("verbose")
        'VB -> NN if the Pos of words i-2...i-1 is "DT"'

        >>> r.format("not_found")
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "nltk/tbl/rule.py", line 256, in format
            raise ValueError("unknown rule format spec: {0}".format(fmt))
        ValueError: unknown rule format spec: not_found
        >>>

        :param fmt: format specification
        :type fmt: str
        :return: string representation
        :rtype: str
        """
        ...
    
    def _verbose_format(self):
        """
        Return a wordy, human-readable string representation
        of the given rule.

        Not sure how useful this is.
        """
        ...
    


