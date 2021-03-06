"""
This type stub file was generated by pyright.
"""

from nltk import compat
from nltk.lm.api import LanguageModel
from typing import Any, Optional

"""Language Models"""
@compat.python_2_unicode_compatible
class MLE(LanguageModel):
    """Class for providing MLE ngram model scores.

    Inherits initialization from BaseNgramModel.
    """
    def unmasked_score(self, word, context: Optional[Any] = ...):
        """Returns the MLE score for a word given a context.

        Args:
        - word is expcected to be a string
        - context is expected to be something reasonably convertible to a tuple
        """
        ...
    


@compat.python_2_unicode_compatible
class Lidstone(LanguageModel):
    """Provides Lidstone-smoothed scores.

    In addition to initialization arguments from BaseNgramModel also requires
    a number by which to increase the counts, gamma.
    """
    def __init__(self, gamma, *args, **kwargs):
        self.gamma = ...
    
    def unmasked_score(self, word, context: Optional[Any] = ...):
        """Add-one smoothing: Lidstone or Laplace.

        To see what kind, look at `gamma` attribute on the class.

        """
        ...
    


@compat.python_2_unicode_compatible
class Laplace(Lidstone):
    """Implements Laplace (add one) smoothing.

    Initialization identical to BaseNgramModel because gamma is always 1.
    """
    def __init__(self, *args, **kwargs):
        ...
    


class InterpolatedLanguageModel(LanguageModel):
    """Logic common to all interpolated language models.

    The idea to abstract this comes from Chen & Goodman 1995.
    """
    def __init__(self, smoothing_cls, order, **kwargs):
        self.estimator = ...
    
    def unmasked_score(self, word, context: Optional[Any] = ...):
        ...
    


class WittenBellInterpolated(InterpolatedLanguageModel):
    """Interpolated version of Witten-Bell smoothing."""
    def __init__(self, order, **kwargs):
        ...
    


class KneserNeyInterpolated(InterpolatedLanguageModel):
    """Interpolated version of Kneser-Ney smoothing."""
    def __init__(self, order, discount=..., **kwargs):
        ...
    


