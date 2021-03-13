"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

_tadm_bin = None
def config_tadm(bin: Optional[Any] = ...):
    ...

def write_tadm_file(train_toks, encoding, stream):
    """
    Generate an input file for ``tadm`` based on the given corpus of
    classified tokens.

    :type train_toks: list(tuple(dict, str))
    :param train_toks: Training data, represented as a list of
        pairs, the first member of which is a feature dictionary,
        and the second of which is a classification label.
    :type encoding: TadmEventMaxentFeatureEncoding
    :param encoding: A feature encoding, used to convert featuresets
        into feature vectors.
    :type stream: stream
    :param stream: The stream to which the ``tadm`` input file should be
        written.
    """
    ...

def parse_tadm_weights(paramfile):
    """
    Given the stdout output generated by ``tadm`` when training a
    model, return a ``numpy`` array containing the corresponding weight
    vector.
    """
    ...

def call_tadm(args):
    """
    Call the ``tadm`` binary with the given arguments.
    """
    ...

def names_demo():
    ...

def encoding_demo():
    ...

if __name__ == '__main__':
    ...