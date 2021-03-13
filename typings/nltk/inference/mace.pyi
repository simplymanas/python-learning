"""
This type stub file was generated by pyright.
"""

from nltk.inference.api import BaseModelBuilderCommand, ModelBuilder
from nltk.inference.prover9 import Prover9CommandParent, Prover9Parent
from typing import Any, Optional

"""
A model builder that makes use of the external 'Mace4' package.
"""
class MaceCommand(Prover9CommandParent, BaseModelBuilderCommand):
    """
    A ``MaceCommand`` specific to the ``Mace`` model builder.  It contains
    a print_assumptions() method that is used to print the list
    of assumptions in multiple formats.
    """
    _interpformat_bin = ...
    def __init__(self, goal: Optional[Any] = ..., assumptions: Optional[Any] = ..., max_models=..., model_builder: Optional[Any] = ...):
        """
        :param goal: Input expression to prove
        :type goal: sem.Expression
        :param assumptions: Input expressions to use as assumptions in
            the proof.
        :type assumptions: list(sem.Expression)
        :param max_models: The maximum number of models that Mace will try before
            simply returning false. (Use 0 for no maximum.)
        :type max_models: int
        """
        ...
    
    @property
    def valuation(mbc):
        ...
    
    def _convert2val(self, valuation_str):
        """
        Transform the output file into an NLTK-style Valuation.

        :return: A model if one is generated; None otherwise.
        :rtype: sem.Valuation
        """
        ...
    
    @staticmethod
    def _make_relation_set(num_entities, values):
        """
        Convert a Mace4-style relation table into a dictionary.

        :param num_entities: the number of entities in the model; determines the row length in the table.
        :type num_entities: int
        :param values: a list of 1's and 0's that represent whether a relation holds in a Mace4 model.
        :type values: list of int
        """
        ...
    
    @staticmethod
    def _make_relation_tuple(position, values, num_entities):
        ...
    
    @staticmethod
    def _make_model_var(value):
        """
        Pick an alphabetic character as identifier for an entity in the model.

        :param value: where to index into the list of characters
        :type value: int
        """
        ...
    
    def _decorate_model(self, valuation_str, format):
        """
        Print out a Mace4 model using any Mace4 ``interpformat`` format.
        See http://www.cs.unm.edu/~mccune/mace4/manual/ for details.

        :param valuation_str: str with the model builder's output
        :param format: str indicating the format for displaying
        models. Defaults to 'standard' format.
        :return: str
        """
        ...
    
    def _transform_output(self, valuation_str, format):
        """
        Transform the output file into any Mace4 ``interpformat`` format.

        :param format: Output format for displaying models.
        :type format: str
        """
        ...
    
    def _call_interpformat(self, input_str, args=..., verbose: bool = ...):
        """
        Call the ``interpformat`` binary with the given input.

        :param input_str: A string whose contents are used as stdin.
        :param args: A list of command-line arguments.
        :return: A tuple (stdout, returncode)
        :see: ``config_prover9``
        """
        ...
    


class Mace(Prover9Parent, ModelBuilder):
    _mace4_bin = ...
    def __init__(self, end_size=...):
        ...
    
    def _build_model(self, goal: Optional[Any] = ..., assumptions: Optional[Any] = ..., verbose: bool = ...):
        """
        Use Mace4 to build a first order model.

        :return: ``True`` if a model was found (i.e. Mace returns value of 0),
        else ``False``
        """
        ...
    
    def _call_mace4(self, input_str, args=..., verbose: bool = ...):
        """
        Call the ``mace4`` binary with the given input.

        :param input_str: A string whose contents are used as stdin.
        :param args: A list of command-line arguments.
        :return: A tuple (stdout, returncode)
        :see: ``config_prover9``
        """
        ...
    


def spacer(num=...):
    ...

def decode_result(found):
    """
    Decode the result of model_found()

    :param found: The output of model_found()
    :type found: bool
    """
    ...

def test_model_found(arguments):
    """
    Try some proofs and exhibit the results.
    """
    ...

def test_build_model(arguments):
    """
    Try to build a ``nltk.sem.Valuation``.
    """
    ...

def test_transform_output(argument_pair):
    """
    Transform the model into various Mace4 ``interpformat`` formats.
    """
    ...

def test_make_relation_set():
    ...

arguments = [('mortal(Socrates)', ['all x.(man(x) -> mortal(x))', 'man(Socrates)']), ('(not mortal(Socrates))', ['all x.(man(x) -> mortal(x))', 'man(Socrates)'])]
def demo():
    ...

if __name__ == '__main__':
    ...