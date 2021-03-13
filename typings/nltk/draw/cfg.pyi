"""
This type stub file was generated by pyright.
"""

from nltk.draw.util import ColorizedList
from typing import Any, Optional

"""
Visualization tools for CFGs.
"""
class ProductionList(ColorizedList):
    ARROW = ...
    def _init_colortags(self, textwidget, options):
        ...
    
    def _item_repr(self, item):
        ...
    


_CFGEditor_HELP = """

The CFG Editor can be used to create or modify context free grammars.
A context free grammar consists of a start symbol and a list of
productions.  The start symbol is specified by the text entry field in
the upper right hand corner of the editor; and the list of productions
are specified in the main text editing box.

Every non-blank line specifies a single production.  Each production
has the form "LHS -> RHS," where LHS is a single nonterminal, and RHS
is a list of nonterminals and terminals.

Nonterminals must be a single word, such as S or NP or NP_subj.
Currently, nonterminals must consists of alphanumeric characters and
underscores (_).  Nonterminals are colored blue.  If you place the
mouse over any nonterminal, then all occurrences of that nonterminal
will be highlighted.

Terminals must be surrounded by single quotes (') or double
quotes(\").  For example, "dog" and "New York" are terminals.
Currently, the string within the quotes must consist of alphanumeric
characters, underscores, and spaces.

To enter a new production, go to a blank line, and type a nonterminal,
followed by an arrow (->), followed by a sequence of terminals and
nonterminals.  Note that "->" (dash + greater-than) is automatically
converted to an arrow symbol.  When you move your cursor to a
different line, your production will automatically be colorized.  If
there are any errors, they will be highlighted in red.

Note that the order of the productions is significant for some
algorithms.  To re-order the productions, use cut and paste to move
them.

Use the buttons at the bottom of the window when you are done editing
the CFG:
  - Ok: apply the new CFG, and exit the editor.
  - Apply: apply the new CFG, and do not exit the editor.
  - Reset: revert to the original CFG, and do not exit the editor.
  - Cancel: revert to the original CFG, and exit the editor.

"""
class CFGEditor(object):
    """
    A dialog window for creating and editing context free grammars.
    ``CFGEditor`` imposes the following restrictions:

    - All nonterminals must be strings consisting of word
      characters.
    - All terminals must be strings consisting of word characters
      and space characters.
    """
    ARROW = ...
    _LHS_RE = ...
    _ARROW_RE = ...
    _PRODUCTION_RE = ...
    _TOKEN_RE = ...
    _BOLD = ...
    def __init__(self, parent, cfg: Optional[Any] = ..., set_cfg_callback: Optional[Any] = ...):
        ...
    
    def _init_startframe(self):
        ...
    
    def _init_buttons(self):
        ...
    
    def _init_bindings(self):
        ...
    
    def _init_prodframe(self):
        ...
    
    def _clear_tags(self, linenum):
        """
        Remove all tags (except ``arrow`` and ``sel``) from the given
        line of the text widget used for editing the productions.
        """
        ...
    
    def _check_analyze(self, *e):
        """
        Check if we've moved to a new line.  If we have, then remove
        all colorization from the line we moved to, and re-colorize
        the line that we moved from.
        """
        ...
    
    def _replace_arrows(self, *e):
        """
        Replace any ``'->'`` text strings with arrows (char \\256, in
        symbol font).  This searches the whole buffer, but is fast
        enough to be done anytime they press '>'.
        """
        ...
    
    def _analyze_token(self, match, linenum):
        """
        Given a line number and a regexp match for a token on that
        line, colorize the token.  Note that the regexp match gives us
        the token's text, start index (on the line), and end index (on
        the line).
        """
        ...
    
    def _init_nonterminal_tag(self, tag, foreground=...):
        ...
    
    def _analyze_line(self, linenum):
        """
        Colorize a given line.
        """
        ...
    
    def _mark_error(self, linenum, line):
        """
        Mark the location of an error in a line.
        """
        ...
    
    def _analyze(self, *e):
        """
        Replace ``->`` with arrows, and colorize the entire buffer.
        """
        ...
    
    def _parse_productions(self):
        """
        Parse the current contents of the textwidget buffer, to create
        a list of productions.
        """
        ...
    
    def _destroy(self, *e):
        ...
    
    def _ok(self, *e):
        ...
    
    def _apply(self, *e):
        ...
    
    def _reset(self, *e):
        ...
    
    def _cancel(self, *e):
        ...
    
    def _help(self, *e):
        ...
    


class CFGDemo(object):
    def __init__(self, grammar, text):
        ...
    
    def _init_bindings(self, top):
        ...
    
    def _init_menubar(self, parent):
        ...
    
    def _init_buttons(self, parent):
        ...
    
    def _init_grammar(self, parent):
        ...
    
    def _init_treelet(self, parent):
        ...
    
    def _init_workspace(self, parent):
        ...
    
    def reset_workspace(self):
        ...
    
    def workspace_markprod(self, production):
        ...
    
    def _markproduction(self, prod, tree: Optional[Any] = ...):
        ...
    
    def _selectprod_cb(self, production):
        ...
    
    def destroy(self, *args):
        ...
    
    def mainloop(self, *args, **kwargs):
        ...
    


def demo2():
    ...

def demo():
    ...

def demo3():
    ...

if __name__ == '__main__':
    ...
