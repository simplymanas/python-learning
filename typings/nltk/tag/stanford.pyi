"""
This type stub file was generated by pyright.
"""

from abc import abstractmethod
from nltk.tag.api import TaggerI
from typing import Any, Optional

"""
A module for interfacing with the Stanford taggers.

Tagger models need to be downloaded from https://nlp.stanford.edu/software
and the STANFORD_MODELS environment variable set (a colon-separated
list of paths).

For more details see the documentation for StanfordPOSTagger and StanfordNERTagger.
"""
_stanford_url = 'https://nlp.stanford.edu/software'
class StanfordTagger(TaggerI):
    """
    An interface to Stanford taggers. Subclasses must define:

    - ``_cmd`` property: A property that returns the command that will be
      executed.
    - ``_SEPARATOR``: Class constant that represents that character that
      is used to separate the tokens from their tags.
    - ``_JAR`` file: Class constant that represents the jar file name.
    """
    _SEPARATOR = ...
    _JAR = ...
    def __init__(self, model_filename, path_to_jar: Optional[Any] = ..., encoding=..., verbose: bool = ..., java_options=...):
        self.java_options = ...
    
    @property
    @abstractmethod
    def _cmd(self):
        """
        A property that returns the command that will be executed.
        """
        ...
    
    def tag(self, tokens):
        ...
    
    def tag_sents(self, sentences):
        ...
    
    def parse_output(self, text, sentences: Optional[Any] = ...):
        ...
    


class StanfordPOSTagger(StanfordTagger):
    """
    A class for pos tagging with Stanford Tagger. The input is the paths to:
     - a model trained on training data
     - (optionally) the path to the stanford tagger jar file. If not specified here,
       then this jar file must be specified in the CLASSPATH envinroment variable.
     - (optionally) the encoding of the training data (default: UTF-8)

    Example:

        >>> from nltk.tag import StanfordPOSTagger
        >>> st = StanfordPOSTagger('english-bidirectional-distsim.tagger')
        >>> st.tag('What is the airspeed of an unladen swallow ?'.split())
        [('What', 'WP'), ('is', 'VBZ'), ('the', 'DT'), ('airspeed', 'NN'), ('of', 'IN'), ('an', 'DT'), ('unladen', 'JJ'), ('swallow', 'VB'), ('?', '.')]
    """
    _SEPARATOR = ...
    _JAR = ...
    def __init__(self, *args, **kwargs):
        ...
    
    @property
    def _cmd(self):
        ...
    


class StanfordNERTagger(StanfordTagger):
    """
    A class for Named-Entity Tagging with Stanford Tagger. The input is the paths to:

    - a model trained on training data
    - (optionally) the path to the stanford tagger jar file. If not specified here,
      then this jar file must be specified in the CLASSPATH envinroment variable.
    - (optionally) the encoding of the training data (default: UTF-8)

    Example:

        >>> from nltk.tag import StanfordNERTagger
        >>> st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz') # doctest: +SKIP
        >>> st.tag('Rami Eid is studying at Stony Brook University in NY'.split()) # doctest: +SKIP
        [('Rami', 'PERSON'), ('Eid', 'PERSON'), ('is', 'O'), ('studying', 'O'),
         ('at', 'O'), ('Stony', 'ORGANIZATION'), ('Brook', 'ORGANIZATION'),
         ('University', 'ORGANIZATION'), ('in', 'O'), ('NY', 'LOCATION')]
    """
    _SEPARATOR = ...
    _JAR = ...
    _FORMAT = ...
    def __init__(self, *args, **kwargs):
        ...
    
    @property
    def _cmd(self):
        ...
    
    def parse_output(self, text, sentences):
        ...
    


def setup_module(module):
    ...

