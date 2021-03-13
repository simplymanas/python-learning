"""
This type stub file was generated by pyright.
"""

import logging
import optparse
from nltk.internals import deprecated
from nltk.compat import python_2_unicode_compatible
from typing import Any, Optional
from nltk.metrics import distance

"""
Implementations of inter-annotator agreement coefficients surveyed by Artstein
and Poesio (2007), Inter-Coder Agreement for Computational Linguistics.

An agreement coefficient calculates the amount that annotators agreed on label
assignments beyond what is expected by chance.

In defining the AnnotationTask class, we use naming conventions similar to the
paper's terminology.  There are three types of objects in an annotation task:

    the coders (variables "c" and "C")
    the items to be annotated (variables "i" and "I")
    the potential categories to be assigned (variables "k" and "K")

Additionally, it is often the case that we don't want to treat two different
labels as complete disagreement, and so the AnnotationTask constructor can also
take a distance metric as a final argument.  Distance metrics are simply
functions that take two arguments, and return a value between 0.0 and 1.0
indicating the distance between them.  If not supplied, the default is binary
comparison between the arguments.

The simplest way to initialize an AnnotationTask is with a list of triples,
each containing a coder's assignment for one object in the task:

    task = AnnotationTask(data=[('c1', '1', 'v1'),('c2', '1', 'v1'),...])

Note that the data list needs to contain the same number of triples for each
individual coder, containing category values for the same set of items.

Alpha (Krippendorff 1980)
Kappa (Cohen 1960)
S (Bennet, Albert and Goldstein 1954)
Pi (Scott 1955)


TODO: Describe handling of multiple coders and missing data

Expected results from the Artstein and Poesio survey paper:

    >>> from nltk.metrics.agreement import AnnotationTask
    >>> import os.path
    >>> t = AnnotationTask(data=[x.split() for x in open(os.path.join(os.path.dirname(__file__), "artstein_poesio_example.txt"))])
    >>> t.avg_Ao()
    0.88
    >>> t.pi()
    0.7995322418977615...
    >>> t.S()
    0.8199999999999998...

    This would have returned a wrong value (0.0) in @785fb79 as coders are in
    the wrong order. Subsequently, all values for pi(), S(), and kappa() would
    have been wrong as they are computed with avg_Ao().
    >>> t2 = AnnotationTask(data=[('b','1','stat'),('a','1','stat')])
    >>> t2.avg_Ao()
    1.0

    The following, of course, also works.
    >>> t3 = AnnotationTask(data=[('a','1','othr'),('b','1','othr')])
    >>> t3.avg_Ao()
    1.0

"""
log = logging.getLogger(__name__)
@python_2_unicode_compatible
class AnnotationTask(object):
    """Represents an annotation task, i.e. people assign labels to items.

    Notation tries to match notation in Artstein and Poesio (2007).

    In general, coders and items can be represented as any hashable object.
    Integers, for example, are fine, though strings are more readable.
    Labels must support the distance functions applied to them, so e.g.
    a string-edit-distance makes no sense if your labels are integers,
    whereas interval distance needs numeric values.  A notable case of this
    is the MASI metric, which requires Python sets.
    """
    def __init__(self, data: Optional[Any] = ..., distance=...):
        """Initialize an annotation task.

        The data argument can be None (to create an empty annotation task) or a sequence of 3-tuples,
        each representing a coder's labeling of an item:
            (coder,item,label)

        The distance argument is a function taking two arguments (labels) and producing a numerical distance.
        The distance from a label to itself should be zero:
            distance(l,l) = 0
        """
        self.distance = ...
        self.I = ...
        self.K = ...
        self.C = ...
        self.data = ...
    
    def __str__(self):
        ...
    
    def load_array(self, array):
        """Load an sequence of annotation results, appending to any data already loaded.

        The argument is a sequence of 3-tuples, each representing a coder's labeling of an item:
            (coder,item,label)
        """
        ...
    
    def agr(self, cA, cB, i, data: Optional[Any] = ...):
        """Agreement between two coders on a given item

        """
        ...
    
    def Nk(self, k):
        ...
    
    def Nik(self, i, k):
        ...
    
    def Nck(self, c, k):
        ...
    
    @deprecated('Use Nk, Nik or Nck instead')
    def N(self, k: Optional[Any] = ..., i: Optional[Any] = ..., c: Optional[Any] = ...):
        """Implements the "n-notation" used in Artstein and Poesio (2007)

        """
        ...
    
    def _grouped_data(self, field, data: Optional[Any] = ...):
        ...
    
    def Ao(self, cA, cB):
        """Observed agreement between two coders on all items.

        """
        ...
    
    def _pairwise_average(self, function):
        """
        Calculates the average of function results for each coder pair
        """
        ...
    
    def avg_Ao(self):
        """Average observed agreement across all coders and items.

        """
        ...
    
    def Do_Kw_pairwise(self, cA, cB, max_distance=...):
        """The observed disagreement for the weighted kappa coefficient.

        """
        ...
    
    def Do_Kw(self, max_distance=...):
        """Averaged over all labelers

        """
        ...
    
    def S(self):
        """Bennett, Albert and Goldstein 1954

        """
        ...
    
    def pi(self):
        """Scott 1955; here, multi-pi.
        Equivalent to K from Siegel and Castellan (1988).

        """
        ...
    
    def Ae_kappa(self, cA, cB):
        ...
    
    def kappa_pairwise(self, cA, cB):
        """

        """
        ...
    
    def kappa(self):
        """Cohen 1960
        Averages naively over kappas for each coder pair.

        """
        ...
    
    def multi_kappa(self):
        """Davies and Fleiss 1982
        Averages over observed and expected agreements for each coder pair.

        """
        ...
    
    def Disagreement(self, label_freqs):
        ...
    
    def alpha(self):
        """Krippendorff 1980

        """
        ...
    
    def weighted_kappa_pairwise(self, cA, cB, max_distance=...):
        """Cohen 1968

        """
        ...
    
    def weighted_kappa(self, max_distance=...):
        """Cohen 1968

        """
        ...
    


if __name__ == '__main__':
    parser = optparse.OptionParser()
    data = []
