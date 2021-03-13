"""
This type stub file was generated by pyright.
"""

from nltk.tokenize.api import TokenizerI

r"""

Penn Treebank Tokenizer

The Treebank tokenizer uses regular expressions to tokenize text as in Penn Treebank.
This implementation is a port of the tokenizer sed script written by Robert McIntyre
and available at http://www.cis.upenn.edu/~treebank/tokenizer.sed.
"""
class MacIntyreContractions:
    """
    List of contractions adapted from Robert MacIntyre's tokenizer.
    """
    CONTRACTIONS2 = ...
    CONTRACTIONS3 = ...
    CONTRACTIONS4 = ...


class TreebankWordTokenizer(TokenizerI):
    """
    The Treebank tokenizer uses regular expressions to tokenize text as in Penn Treebank.
    This is the method that is invoked by ``word_tokenize()``.  It assumes that the
    text has already been segmented into sentences, e.g. using ``sent_tokenize()``.

    This tokenizer performs the following steps:

    - split standard contractions, e.g. ``don't`` -> ``do n't`` and ``they'll`` -> ``they 'll``
    - treat most punctuation characters as separate tokens
    - split off commas and single quotes, when followed by whitespace
    - separate periods that appear at the end of line

        >>> from nltk.tokenize import TreebankWordTokenizer
        >>> s = '''Good muffins cost $3.88\\nin New York.  Please buy me\\ntwo of them.\\nThanks.'''
        >>> TreebankWordTokenizer().tokenize(s)
        ['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York.', 'Please', 'buy', 'me', 'two', 'of', 'them.', 'Thanks', '.']
        >>> s = "They'll save and invest more."
        >>> TreebankWordTokenizer().tokenize(s)
        ['They', "'ll", 'save', 'and', 'invest', 'more', '.']
        >>> s = "hi, my name can't hello,"
        >>> TreebankWordTokenizer().tokenize(s)
        ['hi', ',', 'my', 'name', 'ca', "n't", 'hello', ',']
    """
    STARTING_QUOTES = ...
    PUNCTUATION = ...
    PARENS_BRACKETS = ...
    CONVERT_PARENTHESES = ...
    DOUBLE_DASHES = ...
    ENDING_QUOTES = ...
    _contractions = ...
    CONTRACTIONS2 = ...
    CONTRACTIONS3 = ...
    def tokenize(self, text, convert_parentheses: bool = ..., return_str: bool = ...):
        ...
    
    def span_tokenize(self, text):
        """
        Uses the post-hoc nltk.tokens.align_tokens to return the offset spans.

            >>> from nltk.tokenize import TreebankWordTokenizer
            >>> s = '''Good muffins cost $3.88\\nin New (York).  Please (buy) me\\ntwo of them.\\n(Thanks).'''
            >>> expected = [(0, 4), (5, 12), (13, 17), (18, 19), (19, 23),
            ... (24, 26), (27, 30), (31, 32), (32, 36), (36, 37), (37, 38),
            ... (40, 46), (47, 48), (48, 51), (51, 52), (53, 55), (56, 59),
            ... (60, 62), (63, 68), (69, 70), (70, 76), (76, 77), (77, 78)]
            >>> list(TreebankWordTokenizer().span_tokenize(s)) == expected
            True
            >>> expected = ['Good', 'muffins', 'cost', '$', '3.88', 'in',
            ... 'New', '(', 'York', ')', '.', 'Please', '(', 'buy', ')',
            ... 'me', 'two', 'of', 'them.', '(', 'Thanks', ')', '.']
            >>> [s[start:end] for start, end in TreebankWordTokenizer().span_tokenize(s)] == expected
            True

            Additional example
            >>> from nltk.tokenize import TreebankWordTokenizer
            >>> s = '''I said, "I'd like to buy some ''good muffins" which cost $3.88\\n each in New (York)."'''
            >>> expected = [(0, 1), (2, 6), (6, 7), (8, 9), (9, 10), (10, 12),
            ... (13, 17), (18, 20), (21, 24), (25, 29), (30, 32), (32, 36),
            ... (37, 44), (44, 45), (46, 51), (52, 56), (57, 58), (58, 62),
            ... (64, 68), (69, 71), (72, 75), (76, 77), (77, 81), (81, 82),
            ... (82, 83), (83, 84)]
            >>> list(TreebankWordTokenizer().span_tokenize(s)) == expected
            True
            >>> expected = ['I', 'said', ',', '"', 'I', "'d", 'like', 'to',
            ... 'buy', 'some', "''", "good", 'muffins', '"', 'which', 'cost',
            ... '$', '3.88', 'each', 'in', 'New', '(', 'York', ')', '.', '"']
            >>> [s[start:end] for start, end in TreebankWordTokenizer().span_tokenize(s)] == expected
            True

        """
        ...
    


class TreebankWordDetokenizer(TokenizerI):
    """
    The Treebank detokenizer uses the reverse regex operations corresponding to
    the Treebank tokenizer's regexes.

    Note:
    - There're additional assumption mades when undoing the padding of [;@#$%&]
      punctuation symbols that isn't presupposed in the TreebankTokenizer.
    - There're additional regexes added in reversing the parentheses tokenization,
       - the r'([\]\)\}\>])\s([:;,.])' removes the additional right padding added
         to the closing parentheses precedding [:;,.].
    - It's not possible to return the original whitespaces as they were because
      there wasn't explicit records of where '\n', '\t' or '\s' were removed at
      the text.split() operation.

        >>> from nltk.tokenize.treebank import TreebankWordTokenizer, TreebankWordDetokenizer
        >>> s = '''Good muffins cost $3.88\\nin New York.  Please buy me\\ntwo of them.\\nThanks.'''
        >>> d = TreebankWordDetokenizer()
        >>> t = TreebankWordTokenizer()
        >>> toks = t.tokenize(s)
        >>> d.detokenize(toks)
        'Good muffins cost $3.88 in New York. Please buy me two of them. Thanks.'

    The MXPOST parentheses substitution can be undone using the `convert_parentheses`
    parameter:

    >>> s = '''Good muffins cost $3.88\\nin New (York).  Please (buy) me\\ntwo of them.\\n(Thanks).'''
    >>> expected_tokens = ['Good', 'muffins', 'cost', '$', '3.88', 'in',
    ... 'New', '-LRB-', 'York', '-RRB-', '.', 'Please', '-LRB-', 'buy',
    ... '-RRB-', 'me', 'two', 'of', 'them.', '-LRB-', 'Thanks', '-RRB-', '.']
    >>> expected_tokens == t.tokenize(s, convert_parentheses=True)
    True
    >>> expected_detoken = 'Good muffins cost $3.88 in New (York). Please (buy) me two of them. (Thanks).'
    >>> expected_detoken == d.detokenize(t.tokenize(s, convert_parentheses=True), convert_parentheses=True)
    True

    During tokenization it's safe to add more spaces but during detokenization,
    simply undoing the padding doesn't really help.

    - During tokenization, left and right pad is added to [!?], when
      detokenizing, only left shift the [!?] is needed.
      Thus (re.compile(r'\s([?!])'), r'\g<1>')

    - During tokenization [:,] are left and right padded but when detokenizing,
      only left shift is necessary and we keep right pad after comma/colon
      if the string after is a non-digit.
      Thus (re.compile(r'\s([:,])\s([^\d])'), r'\1 \2')

    >>> from nltk.tokenize.treebank import TreebankWordDetokenizer
    >>> toks = ['hello', ',', 'i', 'ca', "n't", 'feel', 'my', 'feet', '!', 'Help', '!', '!']
    >>> twd = TreebankWordDetokenizer()
    >>> twd.detokenize(toks)
    "hello, i can't feel my feet! Help!!"

    >>> toks = ['hello', ',', 'i', "can't", 'feel', ';', 'my', 'feet', '!',
    ... 'Help', '!', '!', 'He', 'said', ':', 'Help', ',', 'help', '?', '!']
    >>> twd.detokenize(toks)
    "hello, i can't feel; my feet! Help!! He said: Help, help?!"
    """
    _contractions = ...
    CONTRACTIONS2 = ...
    CONTRACTIONS3 = ...
    ENDING_QUOTES = ...
    DOUBLE_DASHES = ...
    CONVERT_PARENTHESES = ...
    PARENS_BRACKETS = ...
    PUNCTUATION = ...
    STARTING_QUOTES = ...
    def tokenize(self, tokens, convert_parentheses: bool = ...):
        """
        Treebank detokenizer, created by undoing the regexes from 
        the TreebankWordTokenizer.tokenize.

        :param tokens: A list of strings, i.e. tokenized text.
        :type tokens: list(str)
        :return: str
        """
        ...
    
    def detokenize(self, tokens, convert_parentheses: bool = ...):
        """ Duck-typing the abstract *tokenize()*."""
        ...
    


