"""
This type stub file was generated by pyright.
"""

def str2tuple(s, sep=...):
    """
    Given the string representation of a tagged token, return the
    corresponding tuple representation.  The rightmost occurrence of
    *sep* in *s* will be used to divide *s* into a word string and
    a tag string.  If *sep* does not occur in *s*, return (s, None).

        >>> from nltk.tag.util import str2tuple
        >>> str2tuple('fly/NN')
        ('fly', 'NN')

    :type s: str
    :param s: The string representation of a tagged token.
    :type sep: str
    :param sep: The separator string used to separate word strings
        from tags.
    """
    ...

def tuple2str(tagged_token, sep=...):
    """
    Given the tuple representation of a tagged token, return the
    corresponding string representation.  This representation is
    formed by concatenating the token's word string, followed by the
    separator, followed by the token's tag.  (If the tag is None,
    then just return the bare word string.)

        >>> from nltk.tag.util import tuple2str
        >>> tagged_token = ('fly', 'NN')
        >>> tuple2str(tagged_token)
        'fly/NN'

    :type tagged_token: tuple(str, str)
    :param tagged_token: The tuple representation of a tagged token.
    :type sep: str
    :param sep: The separator string used to separate word strings
        from tags.
    """
    ...

def untag(tagged_sentence):
    """
    Given a tagged sentence, return an untagged version of that
    sentence.  I.e., return a list containing the first element
    of each tuple in *tagged_sentence*.

        >>> from nltk.tag.util import untag
        >>> untag([('John', 'NNP'), ('saw', 'VBD'), ('Mary', 'NNP')])
        ['John', 'saw', 'Mary']

    """
    ...
