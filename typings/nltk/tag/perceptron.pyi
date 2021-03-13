"""
This type stub file was generated by pyright.
"""

from nltk.tag.api import TaggerI
from nltk.compat import python_2_unicode_compatible
from typing import Any, Optional

PICKLE = "averaged_perceptron_tagger.pickle"
class AveragedPerceptron(object):
    '''An averaged perceptron, as implemented by Matthew Honnibal.

    See more implementation details here:
        https://explosion.ai/blog/part-of-speech-pos-tagger-in-python
    '''
    def __init__(self):
        self.weights = ...
        self.classes = ...
        self.i = ...
    
    def _softmax(self, scores):
        ...
    
    def predict(self, features, return_conf: bool = ...):
        '''Dot-product the features and current weights and return the best label.'''
        ...
    
    def update(self, truth, guess, features):
        '''Update the feature weights.'''
        ...
    
    def average_weights(self):
        '''Average weights from all iterations.'''
        ...
    
    def save(self, path):
        '''Save the pickled model weights.'''
        ...
    
    def load(self, path):
        '''Load the pickled model weights.'''
        self.weights = ...
    


@python_2_unicode_compatible
class PerceptronTagger(TaggerI):
    '''
    Greedy Averaged Perceptron tagger, as implemented by Matthew Honnibal.
    See more implementation details here:
        https://explosion.ai/blog/part-of-speech-pos-tagger-in-python

    >>> from nltk.tag.perceptron import PerceptronTagger

    Train the model

    >>> tagger = PerceptronTagger(load=False)

    >>> tagger.train([[('today','NN'),('is','VBZ'),('good','JJ'),('day','NN')],
    ... [('yes','NNS'),('it','PRP'),('beautiful','JJ')]])

    >>> tagger.tag(['today','is','a','beautiful','day'])
    [('today', 'NN'), ('is', 'PRP'), ('a', 'PRP'), ('beautiful', 'JJ'), ('day', 'NN')]

    Use the pretrain model (the default constructor)

    >>> pretrain = PerceptronTagger()

    >>> pretrain.tag('The quick brown fox jumps over the lazy dog'.split())
    [('The', 'DT'), ('quick', 'JJ'), ('brown', 'NN'), ('fox', 'NN'), ('jumps', 'VBZ'), ('over', 'IN'), ('the', 'DT'), ('lazy', 'JJ'), ('dog', 'NN')]

    >>> pretrain.tag("The red cat".split())
    [('The', 'DT'), ('red', 'JJ'), ('cat', 'NN')]
    '''
    START = ...
    END = ...
    def __init__(self, load: bool = ...):
        '''
        :param load: Load the pickled model upon instantiation.
        '''
        self.model = ...
        self.tagdict = ...
        self.classes = ...
    
    def tag(self, tokens, return_conf: bool = ..., use_tagdict: bool = ...):
        '''
        Tag tokenized sentences.
        :params tokens: list of word
        :type tokens: list(str)
        '''
        ...
    
    def train(self, sentences, save_loc: Optional[Any] = ..., nr_iter=...):
        '''Train a model from sentences, and save it at ``save_loc``. ``nr_iter``
        controls the number of Perceptron training iterations.

        :param sentences: A list or iterator of sentences, where each sentence
            is a list of (words, tags) tuples.
        :param save_loc: If not ``None``, saves a pickled model in this location.
        :param nr_iter: Number of training iterations.
        '''
        ...
    
    def load(self, loc):
        '''
        :param loc: Load a pickled model at location.
        :type loc: str
        '''
        ...
    
    def normalize(self, word):
        '''
        Normalization used in pre-processing.
        - All words are lower cased
        - Groups of digits of length 4 are represented as !YEAR;
        - Other digits are represented as !DIGITS

        :rtype: str
        '''
        ...
    
    def _get_features(self, i, word, context, prev, prev2):
        '''Map tokens into a feature representation, implemented as a
        {hashable: int} dict. If the features change, a new model must be
        trained.
        '''
        ...
    
    def _make_tagdict(self, sentences):
        '''
        Make a tag dictionary for single-tag words.
        :param sentences: A list of list of (word, tag) tuples.
        '''
        ...
    


def _pc(n, d):
    ...

def _load_data_conll_format(filename):
    ...

def _get_pretrain_model():
    ...

if __name__ == '__main__':
    ...
