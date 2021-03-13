"""
This type stub file was generated by pyright.
"""

from abc import ABCMeta, abstractmethod
from six import add_metaclass
from typing import Any, Optional

"""
Module for incrementally developing simple discourses, and checking for semantic ambiguity,
consistency and informativeness.

Many of the ideas are based on the CURT family of programs of Blackburn and Bos
(see http://homepages.inf.ed.ac.uk/jbos/comsem/book1.html).

Consistency checking is carried out  by using the ``mace`` module to call the Mace4 model builder.
Informativeness checking is carried out with a call to ``Prover.prove()`` from
the ``inference``  module.

``DiscourseTester`` is a constructor for discourses.
The basic data structure is a list of sentences, stored as ``self._sentences``. Each sentence in the list
is assigned a "sentence ID" (``sid``) of the form ``s``\ *i*. For example::

    s0: A boxer walks
    s1: Every boxer chases a girl

Each sentence can be ambiguous between a number of readings, each of which receives a
"reading ID" (``rid``) of the form ``s``\ *i* -``r``\ *j*. For example::

    s0 readings:

    s0-r1: some x.(boxer(x) & walk(x))
    s0-r0: some x.(boxerdog(x) & walk(x))

A "thread" is a list of readings, represented as a list of ``rid``\ s.
Each thread receives a "thread ID" (``tid``) of the form ``d``\ *i*.
For example::

    d0: ['s0-r0', 's1-r0']

The set of all threads for a discourse is the Cartesian product of all the readings of the sequences of sentences.
(This is not intended to scale beyond very short discourses!) The method ``readings(filter=True)`` will only show
those threads which are consistent (taking into account any background assumptions).
"""
@add_metaclass(ABCMeta)
class ReadingCommand(object):
    @abstractmethod
    def parse_to_readings(self, sentence):
        """
        :param sentence: the sentence to read
        :type sentence: str
        """
        ...
    
    def process_thread(self, sentence_readings):
        """
        This method should be used to handle dependencies between readings such
        as resolving anaphora.

        :param sentence_readings: readings to process
        :type sentence_readings: list(Expression)
        :return: the list of readings after processing
        :rtype: list(Expression)
        """
        ...
    
    @abstractmethod
    def combine_readings(self, readings):
        """
        :param readings: readings to combine
        :type readings: list(Expression)
        :return: one combined reading
        :rtype: Expression
        """
        ...
    
    @abstractmethod
    def to_fol(self, expression):
        """
        Convert this expression into a First-Order Logic expression.

        :param expression: an expression
        :type expression: Expression
        :return: a FOL version of the input expression
        :rtype: Expression
        """
        ...
    


class CfgReadingCommand(ReadingCommand):
    def __init__(self, gramfile: Optional[Any] = ...):
        """
        :param gramfile: name of file where grammar can be loaded
        :type gramfile: str
        """
        ...
    
    def parse_to_readings(self, sentence):
        """:see: ReadingCommand.parse_to_readings()"""
        ...
    
    def combine_readings(self, readings):
        """:see: ReadingCommand.combine_readings()"""
        ...
    
    def to_fol(self, expression):
        """:see: ReadingCommand.to_fol()"""
        ...
    


class DrtGlueReadingCommand(ReadingCommand):
    def __init__(self, semtype_file: Optional[Any] = ..., remove_duplicates: bool = ..., depparser: Optional[Any] = ...):
        """
        :param semtype_file: name of file where grammar can be loaded
        :param remove_duplicates: should duplicates be removed?
        :param depparser: the dependency parser
        """
        ...
    
    def parse_to_readings(self, sentence):
        """:see: ReadingCommand.parse_to_readings()"""
        ...
    
    def process_thread(self, sentence_readings):
        """:see: ReadingCommand.process_thread()"""
        ...
    
    def combine_readings(self, readings):
        """:see: ReadingCommand.combine_readings()"""
        ...
    
    def to_fol(self, expression):
        """:see: ReadingCommand.to_fol()"""
        ...
    


class DiscourseTester(object):
    """
    Check properties of an ongoing discourse.
    """
    def __init__(self, input, reading_command: Optional[Any] = ..., background: Optional[Any] = ...):
        """
        Initialize a ``DiscourseTester``.

        :param input: the discourse sentences
        :type input: list of str
        :param background: Formulas which express background assumptions
        :type background: list(Expression)
        """
        ...
    
    def sentences(self):
        """
        Display the list of sentences in the current discourse.
        """
        ...
    
    def add_sentence(self, sentence, informchk: bool = ..., consistchk: bool = ...):
        """
        Add a sentence to the current discourse.

        Updates ``self._input`` and ``self._sentences``.
        :param sentence: An input sentence
        :type sentence: str
        :param informchk: if ``True``, check that the result of adding the sentence is thread-informative. Updates ``self._readings``.
        :param consistchk: if ``True``, check that the result of adding the sentence is thread-consistent. Updates ``self._readings``.

        """
        ...
    
    def retract_sentence(self, sentence, verbose: bool = ...):
        """
        Remove a sentence from the current discourse.

        Updates ``self._input``, ``self._sentences`` and ``self._readings``.
        :param sentence: An input sentence
        :type sentence: str
        :param verbose: If ``True``,  report on the updated list of sentences.
        """
        ...
    
    def grammar(self):
        """
        Print out the grammar in use for parsing input sentences
        """
        ...
    
    def _get_readings(self, sentence):
        """
        Build a list of semantic readings for a sentence.

        :rtype: list(Expression)
        """
        ...
    
    def _construct_readings(self):
        """
        Use ``self._sentences`` to construct a value for ``self._readings``.
        """
        ...
    
    def _construct_threads(self):
        """
        Use ``self._readings`` to construct a value for ``self._threads``
        and use the model builder to construct a value for ``self._filtered_threads``
        """
        ...
    
    def _show_readings(self, sentence: Optional[Any] = ...):
        """
        Print out the readings for  the discourse (or a single sentence).
        """
        ...
    
    def _show_threads(self, filter: bool = ..., show_thread_readings: bool = ...):
        """
        Print out the value of ``self._threads`` or ``self._filtered_hreads``
        """
        ...
    
    def readings(self, sentence: Optional[Any] = ..., threaded: bool = ..., verbose: bool = ..., filter: bool = ..., show_thread_readings: bool = ...):
        """
        Construct and show the readings of the discourse (or of a single sentence).

        :param sentence: test just this sentence
        :type sentence: str
        :param threaded: if ``True``, print out each thread ID and the corresponding thread.
        :param filter: if ``True``, only print out consistent thread IDs and threads.
        """
        ...
    
    def expand_threads(self, thread_id, threads: Optional[Any] = ...):
        """
        Given a thread ID, find the list of ``logic.Expression`` objects corresponding to the reading IDs in that thread.

        :param thread_id: thread ID
        :type thread_id: str
        :param threads: a mapping from thread IDs to lists of reading IDs
        :type threads: dict
        :return: A list of pairs ``(rid, reading)`` where reading is the ``logic.Expression`` associated with a reading ID
        :rtype: list of tuple
        """
        ...
    
    def _check_consistency(self, threads, show: bool = ..., verbose: bool = ...):
        ...
    
    def models(self, thread_id: Optional[Any] = ..., show: bool = ..., verbose: bool = ...):
        """
        Call Mace4 to build a model for each current discourse thread.

        :param thread_id: thread ID
        :type thread_id: str
        :param show: If ``True``, display the model that has been found.
        """
        ...
    
    def add_background(self, background, verbose: bool = ...):
        """
        Add a list of background assumptions for reasoning about the discourse.

        When called,  this method also updates the discourse model's set of readings and threads.
        :param background: Formulas which contain background information
        :type background: list(Expression)
        """
        ...
    
    def background(self):
        """
        Show the current background assumptions.
        """
        ...
    
    @staticmethod
    def multiply(discourse, readings):
        """
        Multiply every thread in ``discourse`` by every reading in ``readings``.

        Given discourse = [['A'], ['B']], readings = ['a', 'b', 'c'] , returns
        [['A', 'a'], ['A', 'b'], ['A', 'c'], ['B', 'a'], ['B', 'b'], ['B', 'c']]

        :param discourse: the current list of readings
        :type discourse: list of lists
        :param readings: an additional list of readings
        :type readings: list(Expression)
        :rtype: A list of lists
        """
        ...
    


def load_fol(s):
    """
    Temporarily duplicated from ``nltk.sem.util``.
    Convert a  file of first order formulas into a list of ``Expression`` objects.

    :param s: the contents of the file
    :type s: str
    :return: a list of parsed formulas.
    :rtype: list(Expression)
    """
    ...

def discourse_demo(reading_command: Optional[Any] = ...):
    """
    Illustrate the various methods of ``DiscourseTester``
    """
    ...

def drt_discourse_demo(reading_command: Optional[Any] = ...):
    """
    Illustrate the various methods of ``DiscourseTester``
    """
    ...

def spacer(num=...):
    ...

def demo():
    ...

if __name__ == '__main__':
    ...
