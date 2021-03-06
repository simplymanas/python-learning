"""
This type stub file was generated by pyright.
"""

from nltk.compat import python_2_unicode_compatible
from typing import Any, Optional

SPEC_SEMTYPES = { 'a': 'ex_quant','an': 'ex_quant','every': 'univ_quant','the': 'def_art','no': 'no_quant','default': 'ex_quant' }
OPTIONAL_RELATIONSHIPS = ['nmod', 'vmod', 'punct']
@python_2_unicode_compatible
class GlueFormula(object):
    def __init__(self, meaning, glue, indices: Optional[Any] = ...):
        self.indices = ...
    
    def applyto(self, arg):
        """ self = (\\x.(walk x), (subj -o f))
            arg  = (john        ,  subj)
            returns ((walk john),          f)
        """
        ...
    
    def make_VariableExpression(self, name):
        ...
    
    def make_LambdaExpression(self, variable, term):
        ...
    
    def lambda_abstract(self, other):
        ...
    
    def compile(self, counter: Optional[Any] = ...):
        """From Iddo Lev's PhD Dissertation p108-109"""
        ...
    
    def simplify(self):
        ...
    
    def __eq__(self, other):
        ...
    
    def __ne__(self, other):
        ...
    
    def __lt__(self, other):
        ...
    
    def __str__(self):
        ...
    
    def __repr__(self):
        ...
    


@python_2_unicode_compatible
class GlueDict(dict):
    def __init__(self, filename, encoding: Optional[Any] = ...):
        self.filename = ...
        self.file_encoding = ...
    
    def read_file(self, empty_first: bool = ...):
        ...
    
    def __str__(self):
        ...
    
    def to_glueformula_list(self, depgraph, node: Optional[Any] = ..., counter: Optional[Any] = ..., verbose: bool = ...):
        ...
    
    def lookup(self, node, depgraph, counter):
        ...
    
    def add_missing_dependencies(self, node, depgraph):
        ...
    
    def _lookup_semtype_option(self, semtype, node, depgraph):
        ...
    
    def get_semtypes(self, node):
        """
        Based on the node, return a list of plausible semtypes in order of
        plausibility.
        """
        ...
    
    def get_glueformulas_from_semtype_entry(self, lookup, word, node, depgraph, counter):
        ...
    
    def get_meaning_formula(self, generic, word):
        """
        :param generic: A meaning formula string containing the
        parameter "<word>"
        :param word: The actual word to be replace "<word>"
        """
        ...
    
    def initialize_labels(self, expr, node, depgraph, unique_index):
        ...
    
    def find_label_name(self, name, node, depgraph, unique_index):
        ...
    
    def get_label(self, node):
        """
        Pick an alphabetic character as identifier for an entity in the model.

        :param value: where to index into the list of characters
        :type value: int
        """
        ...
    
    def lookup_unique(self, rel, node, depgraph):
        """
        Lookup 'key'. There should be exactly one item in the associated relation.
        """
        ...
    
    def get_GlueFormula_factory(self):
        ...
    


class Glue(object):
    def __init__(self, semtype_file: Optional[Any] = ..., remove_duplicates: bool = ..., depparser: Optional[Any] = ..., verbose: bool = ...):
        self.verbose = ...
        self.remove_duplicates = ...
        self.depparser = ...
        self.prover = ...
    
    def train_depparser(self, depgraphs: Optional[Any] = ...):
        ...
    
    def parse_to_meaning(self, sentence):
        ...
    
    def get_readings(self, agenda):
        ...
    
    def _add_to_reading_list(self, glueformula, reading_list):
        ...
    
    def parse_to_compiled(self, sentence):
        ...
    
    def dep_parse(self, sentence):
        """
        Return a dependency graph for the sentence.

        :param sentence: the sentence to be parsed
        :type sentence: list(str)
        :rtype: DependencyGraph
        """
        ...
    
    def depgraph_to_glue(self, depgraph):
        ...
    
    def get_glue_dict(self):
        ...
    
    def gfl_to_compiled(self, gfl):
        ...
    
    def get_pos_tagger(self):
        ...
    


class DrtGlueFormula(GlueFormula):
    def __init__(self, meaning, glue, indices: Optional[Any] = ...):
        self.indices = ...
    
    def make_VariableExpression(self, name):
        ...
    
    def make_LambdaExpression(self, variable, term):
        ...
    


class DrtGlueDict(GlueDict):
    def get_GlueFormula_factory(self):
        ...
    


class DrtGlue(Glue):
    def __init__(self, semtype_file: Optional[Any] = ..., remove_duplicates: bool = ..., depparser: Optional[Any] = ..., verbose: bool = ...):
        ...
    
    def get_glue_dict(self):
        ...
    


def demo(show_example=...):
    ...

if __name__ == '__main__':
    ...
