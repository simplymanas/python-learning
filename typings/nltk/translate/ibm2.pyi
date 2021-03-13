"""
This type stub file was generated by pyright.
"""

from nltk.translate import IBMModel
from nltk.translate.ibm_model import Counts
from typing import Any, Optional

"""
Lexical translation model that considers word order.

IBM Model 2 improves on Model 1 by accounting for word order.
An alignment probability is introduced, a(i | j,l,m), which predicts
a source word position, given its aligned target word's position.

The EM algorithm used in Model 2 is:
E step - In the training data, collect counts, weighted by prior
         probabilities.
         (a) count how many times a source language word is translated
             into a target language word
         (b) count how many times a particular position in the source
             sentence is aligned to a particular position in the target
             sentence

M step - Estimate new probabilities based on the counts from the E step


Notations:
i: Position in the source sentence
    Valid values are 0 (for NULL), 1, 2, ..., length of source sentence
j: Position in the target sentence
    Valid values are 1, 2, ..., length of target sentence
l: Number of words in the source sentence, excluding NULL
m: Number of words in the target sentence
s: A word in the source language
t: A word in the target language


References:
Philipp Koehn. 2010. Statistical Machine Translation.
Cambridge University Press, New York.

Peter E Brown, Stephen A. Della Pietra, Vincent J. Della Pietra, and
Robert L. Mercer. 1993. The Mathematics of Statistical Machine
Translation: Parameter Estimation. Computational Linguistics, 19 (2),
263-311.
"""
class IBMModel2(IBMModel):
    """
    Lexical translation model that considers word order

    >>> bitext = []
    >>> bitext.append(AlignedSent(['klein', 'ist', 'das', 'haus'], ['the', 'house', 'is', 'small']))
    >>> bitext.append(AlignedSent(['das', 'haus', 'ist', 'ja', 'groß'], ['the', 'house', 'is', 'big']))
    >>> bitext.append(AlignedSent(['das', 'buch', 'ist', 'ja', 'klein'], ['the', 'book', 'is', 'small']))
    >>> bitext.append(AlignedSent(['das', 'haus'], ['the', 'house']))
    >>> bitext.append(AlignedSent(['das', 'buch'], ['the', 'book']))
    >>> bitext.append(AlignedSent(['ein', 'buch'], ['a', 'book']))

    >>> ibm2 = IBMModel2(bitext, 5)

    >>> print(round(ibm2.translation_table['buch']['book'], 3))
    1.0
    >>> print(round(ibm2.translation_table['das']['book'], 3))
    0.0
    >>> print(round(ibm2.translation_table['buch'][None], 3))
    0.0
    >>> print(round(ibm2.translation_table['ja'][None], 3))
    0.0

    >>> print(ibm2.alignment_table[1][1][2][2])
    0.938...
    >>> print(round(ibm2.alignment_table[1][2][2][2], 3))
    0.0
    >>> print(round(ibm2.alignment_table[2][2][4][5], 3))
    1.0

    >>> test_sentence = bitext[2]
    >>> test_sentence.words
    ['das', 'buch', 'ist', 'ja', 'klein']
    >>> test_sentence.mots
    ['the', 'book', 'is', 'small']
    >>> test_sentence.alignment
    Alignment([(0, 0), (1, 1), (2, 2), (3, 2), (4, 3)])

    """
    def __init__(self, sentence_aligned_corpus, iterations, probability_tables: Optional[Any] = ...):
        """
        Train on ``sentence_aligned_corpus`` and create a lexical
        translation model and an alignment model.

        Translation direction is from ``AlignedSent.mots`` to
        ``AlignedSent.words``.

        :param sentence_aligned_corpus: Sentence-aligned parallel corpus
        :type sentence_aligned_corpus: list(AlignedSent)

        :param iterations: Number of iterations to run training algorithm
        :type iterations: int

        :param probability_tables: Optional. Use this to pass in custom
            probability values. If not specified, probabilities will be
            set to a uniform distribution, or some other sensible value.
            If specified, all the following entries must be present:
            ``translation_table``, ``alignment_table``.
            See ``IBMModel`` for the type and purpose of these tables.
        :type probability_tables: dict[str]: object
        """
        ...
    
    def set_uniform_probabilities(self, sentence_aligned_corpus):
        ...
    
    def train(self, parallel_corpus):
        ...
    
    def maximize_alignment_probabilities(self, counts):
        ...
    
    def prob_all_alignments(self, src_sentence, trg_sentence):
        """
        Computes the probability of all possible word alignments,
        expressed as a marginal distribution over target words t

        Each entry in the return value represents the contribution to
        the total alignment probability by the target word t.

        To obtain probability(alignment | src_sentence, trg_sentence),
        simply sum the entries in the return value.

        :return: Probability of t for all s in ``src_sentence``
        :rtype: dict(str): float
        """
        ...
    
    def prob_alignment_point(self, i, j, src_sentence, trg_sentence):
        """
        Probability that position j in ``trg_sentence`` is aligned to
        position i in the ``src_sentence``
        """
        ...
    
    def prob_t_a_given_s(self, alignment_info):
        """
        Probability of target sentence and an alignment given the
        source sentence
        """
        ...
    
    def align_all(self, parallel_corpus):
        ...
    
    def align(self, sentence_pair):
        """
        Determines the best word alignment for one sentence pair from
        the corpus that the model was trained on.

        The best alignment will be set in ``sentence_pair`` when the
        method returns. In contrast with the internal implementation of
        IBM models, the word indices in the ``Alignment`` are zero-
        indexed, not one-indexed.

        :param sentence_pair: A sentence in the source language and its
            counterpart sentence in the target language
        :type sentence_pair: AlignedSent
        """
        ...
    


class Model2Counts(Counts):
    """
    Data object to store counts of various parameters during training.
    Includes counts for alignment.
    """
    def __init__(self):
        self.alignment = ...
        self.alignment_for_any_i = ...
    
    def update_lexical_translation(self, count, s, t):
        ...
    
    def update_alignment(self, count, i, j, l, m):
        ...
    


