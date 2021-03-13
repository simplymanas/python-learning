"""
This type stub file was generated by pyright.
"""

import math as _math
from abc import ABCMeta, abstractmethod
from functools import reduce
from six import add_metaclass

"""
Provides scoring functions for a number of association measures through a
generic, abstract implementation in ``NgramAssocMeasures``, and n-specific
``BigramAssocMeasures`` and ``TrigramAssocMeasures``.
"""
_log2 = lambda x: _math.log(x, 2)
_ln = _math.log
_product = lambda s: reduce(lambda x, y: x * y, s)
_SMALL = 1e-20
NGRAM = 0
UNIGRAMS = - 2
TOTAL = - 1
@add_metaclass(ABCMeta)
class NgramAssocMeasures(object):
    """
    An abstract class defining a collection of generic association measures.
    Each public method returns a score, taking the following arguments::

        score_fn(count_of_ngram,
                 (count_of_n-1gram_1, ..., count_of_n-1gram_j),
                 (count_of_n-2gram_1, ..., count_of_n-2gram_k),
                 ...,
                 (count_of_1gram_1, ..., count_of_1gram_n),
                 count_of_total_words)

    See ``BigramAssocMeasures`` and ``TrigramAssocMeasures``

    Inheriting classes should define a property _n, and a method _contingency
    which calculates contingency values from marginals in order for all
    association measures defined here to be usable.
    """
    _n = ...
    @staticmethod
    @abstractmethod
    def _contingency(*marginals):
        """Calculates values of a contingency table from marginal values."""
        ...
    
    @staticmethod
    @abstractmethod
    def _marginals(*contingency):
        """Calculates values of contingency table marginals from its values."""
        ...
    
    @classmethod
    def _expected_values(cls, cont):
        """Calculates expected values for a contingency table."""
        ...
    
    @staticmethod
    def raw_freq(*marginals):
        """Scores ngrams by their frequency"""
        ...
    
    @classmethod
    def student_t(cls, *marginals):
        """Scores ngrams using Student's t test with independence hypothesis
        for unigrams, as in Manning and Schutze 5.3.1.
        """
        ...
    
    @classmethod
    def chi_sq(cls, *marginals):
        """Scores ngrams using Pearson's chi-square as in Manning and Schutze
        5.3.3.
        """
        ...
    
    @staticmethod
    def mi_like(*marginals, **kwargs):
        """Scores ngrams using a variant of mutual information. The keyword
        argument power sets an exponent (default 3) for the numerator. No
        logarithm of the result is calculated.
        """
        ...
    
    @classmethod
    def pmi(cls, *marginals):
        """Scores ngrams by pointwise mutual information, as in Manning and
        Schutze 5.4.
        """
        ...
    
    @classmethod
    def likelihood_ratio(cls, *marginals):
        """Scores ngrams using likelihood ratios as in Manning and Schutze 5.3.4.
        """
        ...
    
    @classmethod
    def poisson_stirling(cls, *marginals):
        """Scores ngrams using the Poisson-Stirling measure."""
        ...
    
    @classmethod
    def jaccard(cls, *marginals):
        """Scores ngrams using the Jaccard index."""
        ...
    


class BigramAssocMeasures(NgramAssocMeasures):
    """
    A collection of bigram association measures. Each association measure
    is provided as a function with three arguments::

        bigram_score_fn(n_ii, (n_ix, n_xi), n_xx)

    The arguments constitute the marginals of a contingency table, counting
    the occurrences of particular events in a corpus. The letter i in the
    suffix refers to the appearance of the word in question, while x indicates
    the appearance of any word. Thus, for example:

        n_ii counts (w1, w2), i.e. the bigram being scored
        n_ix counts (w1, *)
        n_xi counts (*, w2)
        n_xx counts (*, *), i.e. any bigram

    This may be shown with respect to a contingency table::

                w1    ~w1
             ------ ------
         w2 | n_ii | n_oi | = n_xi
             ------ ------
        ~w2 | n_io | n_oo |
             ------ ------
             = n_ix        TOTAL = n_xx
    """
    _n = ...
    @staticmethod
    def _contingency(n_ii, n_ix_xi_tuple, n_xx):
        """Calculates values of a bigram contingency table from marginal values."""
        ...
    
    @staticmethod
    def _marginals(n_ii, n_oi, n_io, n_oo):
        """Calculates values of contingency table marginals from its values."""
        ...
    
    @staticmethod
    def _expected_values(cont):
        """Calculates expected values for a contingency table."""
        ...
    
    @classmethod
    def phi_sq(cls, *marginals):
        """Scores bigrams using phi-square, the square of the Pearson correlation
        coefficient.
        """
        ...
    
    @classmethod
    def chi_sq(cls, n_ii, n_ix_xi_tuple, n_xx):
        """Scores bigrams using chi-square, i.e. phi-sq multiplied by the number
        of bigrams, as in Manning and Schutze 5.3.3.
        """
        ...
    
    @classmethod
    def fisher(cls, *marginals):
        """Scores bigrams using Fisher's Exact Test (Pedersen 1996).  Less
        sensitive to small counts than PMI or Chi Sq, but also more expensive
        to compute. Requires scipy.
        """
        ...
    
    @staticmethod
    def dice(n_ii, n_ix_xi_tuple, n_xx):
        """Scores bigrams using Dice's coefficient."""
        ...
    


class TrigramAssocMeasures(NgramAssocMeasures):
    """
    A collection of trigram association measures. Each association measure
    is provided as a function with four arguments::

        trigram_score_fn(n_iii,
                         (n_iix, n_ixi, n_xii),
                         (n_ixx, n_xix, n_xxi),
                         n_xxx)

    The arguments constitute the marginals of a contingency table, counting
    the occurrences of particular events in a corpus. The letter i in the
    suffix refers to the appearance of the word in question, while x indicates
    the appearance of any word. Thus, for example:
    n_iii counts (w1, w2, w3), i.e. the trigram being scored
    n_ixx counts (w1, *, *)
    n_xxx counts (*, *, *), i.e. any trigram
    """
    _n = ...
    @staticmethod
    def _contingency(n_iii, n_iix_tuple, n_ixx_tuple, n_xxx):
        """Calculates values of a trigram contingency table (or cube) from
        marginal values.
        >>> TrigramAssocMeasures._contingency(1, (1, 1, 1), (1, 73, 1), 2000)
        (1, 0, 0, 0, 0, 72, 0, 1927)
        """
        ...
    
    @staticmethod
    def _marginals(*contingency):
        """Calculates values of contingency table marginals from its values.
        >>> TrigramAssocMeasures._marginals(1, 0, 0, 0, 0, 72, 0, 1927)
        (1, (1, 1, 1), (1, 73, 1), 2000)
        """
        ...
    


class QuadgramAssocMeasures(NgramAssocMeasures):
    """
    A collection of quadgram association measures. Each association measure
    is provided as a function with five arguments::

        trigram_score_fn(n_iiii,
                        (n_iiix, n_iixi, n_ixii, n_xiii),
                        (n_iixx, n_ixix, n_ixxi, n_xixi, n_xxii, n_xiix),
                        (n_ixxx, n_xixx, n_xxix, n_xxxi),
                        n_all)

    The arguments constitute the marginals of a contingency table, counting
    the occurrences of particular events in a corpus. The letter i in the
    suffix refers to the appearance of the word in question, while x indicates
    the appearance of any word. Thus, for example:
    n_iiii counts (w1, w2, w3, w4), i.e. the quadgram being scored
    n_ixxi counts (w1, *, *, w4)
    n_xxxx counts (*, *, *, *), i.e. any quadgram
    """
    _n = ...
    @staticmethod
    def _contingency(n_iiii, n_iiix_tuple, n_iixx_tuple, n_ixxx_tuple, n_xxxx):
        """Calculates values of a quadgram contingency table from
        marginal values.
        """
        ...
    
    @staticmethod
    def _marginals(*contingency):
        """Calculates values of contingency table marginals from its values.
        QuadgramAssocMeasures._marginals(1, 0, 2, 46, 552, 825, 2577, 34967, 1, 0, 2, 48, 7250, 9031, 28585, 356653)
        (1, (2, 553, 3, 1), (7804, 6, 3132, 1378, 49, 2), (38970, 17660, 100, 38970), 440540)
        """
        ...
    


class ContingencyMeasures(object):
    """Wraps NgramAssocMeasures classes such that the arguments of association
    measures are contingency table values rather than marginals.
    """
    def __init__(self, measures):
        """Constructs a ContingencyMeasures given a NgramAssocMeasures class"""
        ...
    
    @staticmethod
    def _make_contingency_fn(measures, old_fn):
        """From an association measure function, produces a new function which
        accepts contingency table values as its arguments.
        """
        ...
    

