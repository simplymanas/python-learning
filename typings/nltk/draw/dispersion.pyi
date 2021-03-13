"""
This type stub file was generated by pyright.
"""

"""
A utility for displaying lexical dispersion.
"""
def dispersion_plot(text, words, ignore_case: bool = ..., title=...):
    """
    Generate a lexical dispersion plot.

    :param text: The source text
    :type text: list(str) or enum(str)
    :param words: The target words
    :type words: list of str
    :param ignore_case: flag to set if case should be ignored when searching text
    :type ignore_case: bool
    """
    ...

if __name__ == '__main__':
    words = ['Elinor', 'Marianne', 'Edward', 'Willoughby']