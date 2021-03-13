"""
This type stub file was generated by pyright.
"""

from six.moves.tkinter import Frame
from typing import Any, Optional

"""
Tkinter widgets for displaying multi-column listboxes and tables.
"""
class MultiListbox(Frame):
    """
    A multi-column listbox, where the current selection applies to an
    entire row.  Based on the MultiListbox Tkinter widget
    recipe from the Python Cookbook (http://code.activestate.com/recipes/52266/)

    For the most part, ``MultiListbox`` methods delegate to its
    contained listboxes.  For any methods that do not have docstrings,
    see ``Tkinter.Listbox`` for a description of what that method does.
    """
    FRAME_CONFIG = ...
    LABEL_CONFIG = ...
    LISTBOX_CONFIG = ...
    def __init__(self, master, columns, column_weights: Optional[Any] = ..., cnf=..., **kw):
        """
        Construct a new multi-column listbox widget.

        :param master: The widget that should contain the new
            multi-column listbox.

        :param columns: Specifies what columns should be included in
            the new multi-column listbox.  If ``columns`` is an integer,
            the it is the number of columns to include.  If it is
            a list, then its length indicates the number of columns
            to include; and each element of the list will be used as
            a label for the corresponding column.

        :param cnf, kw: Configuration parameters for this widget.
            Use ``label_*`` to configure all labels; and ``listbox_*``
            to configure all listboxes.  E.g.:

                >>> mlb = MultiListbox(master, 5, label_foreground='red')
        """
        ...
    
    def _resize_column(self, event):
        """
        Callback used to resize a column of the table.  Return ``True``
        if the column is actually getting resized (if the user clicked
        on the far left or far right 5 pixels of a label); and
        ``False`` otherwies.
        """
        ...
    
    def _resize_column_motion_cb(self, event):
        ...
    
    def _resize_column_buttonrelease_cb(self, event):
        ...
    
    @property
    def column_names(self):
        """
        A tuple containing the names of the columns used by this
        multi-column listbox.
        """
        ...
    
    @property
    def column_labels(self):
        """
        A tuple containing the ``Tkinter.Label`` widgets used to
        display the label of each column.  If this multi-column
        listbox was created without labels, then this will be an empty
        tuple.  These widgets will all be augmented with a
        ``column_index`` attribute, which can be used to determine
        which column they correspond to.  This can be convenient,
        e.g., when defining callbacks for bound events.
        """
        ...
    
    @property
    def listboxes(self):
        """
        A tuple containing the ``Tkinter.Listbox`` widgets used to
        display individual columns.  These widgets will all be
        augmented with a ``column_index`` attribute, which can be used
        to determine which column they correspond to.  This can be
        convenient, e.g., when defining callbacks for bound events.
        """
        ...
    
    def _select(self, e):
        ...
    
    def _scroll(self, delta):
        ...
    
    def _pagesize(self):
        """:return: The number of rows that makes up one page"""
        ...
    
    def select(self, index: Optional[Any] = ..., delta: Optional[Any] = ..., see: bool = ...):
        """
        Set the selected row.  If ``index`` is specified, then select
        row ``index``.  Otherwise, if ``delta`` is specified, then move
        the current selection by ``delta`` (negative numbers for up,
        positive numbers for down).  This will not move the selection
        past the top or the bottom of the list.

        :param see: If true, then call ``self.see()`` with the newly
            selected index, to ensure that it is visible.
        """
        ...
    
    def configure(self, cnf=..., **kw):
        """
        Configure this widget.  Use ``label_*`` to configure all
        labels; and ``listbox_*`` to configure all listboxes.  E.g.:

                >>> mlb = MultiListbox(master, 5)
                >>> mlb.configure(label_foreground='red')
                >>> mlb.configure(listbox_foreground='red')
        """
        ...
    
    def __setitem__(self, key, val):
        """
        Configure this widget.  This is equivalent to
        ``self.configure({key,val``)}.  See ``configure()``.
        """
        ...
    
    def rowconfigure(self, row_index, cnf=..., **kw):
        """
        Configure all table cells in the given row.  Valid keyword
        arguments are: ``background``, ``bg``, ``foreground``, ``fg``,
        ``selectbackground``, ``selectforeground``.
        """
        ...
    
    def columnconfigure(self, col_index, cnf=..., **kw):
        """
        Configure all table cells in the given column.  Valid keyword
        arguments are: ``background``, ``bg``, ``foreground``, ``fg``,
        ``selectbackground``, ``selectforeground``.
        """
        ...
    
    def itemconfigure(self, row_index, col_index, cnf: Optional[Any] = ..., **kw):
        """
        Configure the table cell at the given row and column.  Valid
        keyword arguments are: ``background``, ``bg``, ``foreground``,
        ``fg``, ``selectbackground``, ``selectforeground``.
        """
        ...
    
    def insert(self, index, *rows):
        """
        Insert the given row or rows into the table, at the given
        index.  Each row value should be a tuple of cell values, one
        for each column in the row.  Index may be an integer or any of
        the special strings (such as ``'end'``) accepted by
        ``Tkinter.Listbox``.
        """
        ...
    
    def get(self, first, last: Optional[Any] = ...):
        """
        Return the value(s) of the specified row(s).  If ``last`` is
        not specified, then return a single row value; otherwise,
        return a list of row values.  Each row value is a tuple of
        cell values, one for each column in the row.
        """
        ...
    
    def bbox(self, row, col):
        """
        Return the bounding box for the given table cell, relative to
        this widget's top-left corner.  The bounding box is a tuple
        of integers ``(left, top, width, height)``.
        """
        ...
    
    def hide_column(self, col_index):
        """
        Hide the given column.  The column's state is still
        maintained: its values will still be returned by ``get()``, and
        you must supply its values when calling ``insert()``.  It is
        safe to call this on a column that is already hidden.

        :see: ``show_column()``
        """
        ...
    
    def show_column(self, col_index):
        """
        Display a column that has been hidden using ``hide_column()``.
        It is safe to call this on a column that is not hidden.
        """
        ...
    
    def bind_to_labels(self, sequence: Optional[Any] = ..., func: Optional[Any] = ..., add: Optional[Any] = ...):
        """
        Add a binding to each ``Tkinter.Label`` widget in this
        mult-column listbox that will call ``func`` in response to the
        event sequence.

        :return: A list of the identifiers of replaced binding
            functions (if any), allowing for their deletion (to
            prevent a memory leak).
        """
        ...
    
    def bind_to_listboxes(self, sequence: Optional[Any] = ..., func: Optional[Any] = ..., add: Optional[Any] = ...):
        """
        Add a binding to each ``Tkinter.Listbox`` widget in this
        mult-column listbox that will call ``func`` in response to the
        event sequence.

        :return: A list of the identifiers of replaced binding
            functions (if any), allowing for their deletion (to
            prevent a memory leak).
        """
        ...
    
    def bind_to_columns(self, sequence: Optional[Any] = ..., func: Optional[Any] = ..., add: Optional[Any] = ...):
        """
        Add a binding to each ``Tkinter.Label`` and ``Tkinter.Listbox``
        widget in this mult-column listbox that will call ``func`` in
        response to the event sequence.

        :return: A list of the identifiers of replaced binding
            functions (if any), allowing for their deletion (to
            prevent a memory leak).
        """
        ...
    
    def curselection(self, *args, **kwargs):
        ...
    
    def selection_includes(self, *args, **kwargs):
        ...
    
    def itemcget(self, *args, **kwargs):
        ...
    
    def size(self, *args, **kwargs):
        ...
    
    def index(self, *args, **kwargs):
        ...
    
    def nearest(self, *args, **kwargs):
        ...
    
    def activate(self, *args, **kwargs):
        ...
    
    def delete(self, *args, **kwargs):
        ...
    
    def scan_mark(self, *args, **kwargs):
        ...
    
    def scan_dragto(self, *args, **kwargs):
        ...
    
    def see(self, *args, **kwargs):
        ...
    
    def selection_anchor(self, *args, **kwargs):
        ...
    
    def selection_clear(self, *args, **kwargs):
        ...
    
    def selection_set(self, *args, **kwargs):
        ...
    
    def yview(self, *args, **kwargs):
        ...
    
    def yview_moveto(self, *args, **kwargs):
        ...
    
    def yview_scroll(self, *args, **kwargs):
        ...
    
    itemconfig = ...
    rowconfig = ...
    columnconfig = ...
    select_anchor = ...
    select_clear = ...
    select_includes = ...
    select_set = ...


class Table(object):
    """
    A display widget for a table of values, based on a ``MultiListbox``
    widget.  For many purposes, ``Table`` can be treated as a
    list-of-lists.  E.g., table[i] is a list of the values for row i;
    and table.append(row) adds a new row with the given lits of
    values.  Individual cells can be accessed using table[i,j], which
    refers to the j-th column of the i-th row.  This can be used to
    both read and write values from the table.  E.g.:

        >>> table[i,j] = 'hello'

    The column (j) can be given either as an index number, or as a
    column name.  E.g., the following prints the value in the 3rd row
    for the 'First Name' column:

        >>> print(table[3, 'First Name'])
        John

    You can configure the colors for individual rows, columns, or
    cells using ``rowconfig()``, ``columnconfig()``, and ``itemconfig()``.
    The color configuration for each row will be preserved if the
    table is modified; however, when new rows are added, any color
    configurations that have been made for *columns* will not be
    applied to the new row.

    Note: Although ``Table`` acts like a widget in some ways (e.g., it
    defines ``grid()``, ``pack()``, and ``bind()``), it is not itself a
    widget; it just contains one.  This is because widgets need to
    define ``__getitem__()``, ``__setitem__()``, and ``__nonzero__()`` in
    a way that's incompatible with the fact that ``Table`` behaves as a
    list-of-lists.

    :ivar _mlb: The multi-column listbox used to display this table's data.
    :ivar _rows: A list-of-lists used to hold the cell values of this
        table.  Each element of _rows is a row value, i.e., a list of
        cell values, one for each column in the row.
    """
    def __init__(self, master, column_names, rows: Optional[Any] = ..., column_weights: Optional[Any] = ..., scrollbar: bool = ..., click_to_sort: bool = ..., reprfunc: Optional[Any] = ..., cnf=..., **kw):
        """
        Construct a new Table widget.

        :type master: Tkinter.Widget
        :param master: The widget that should contain the new table.
        :type column_names: list(str)
        :param column_names: A list of names for the columns; these
            names will be used to create labels for each column;
            and can be used as an index when reading or writing
            cell values from the table.
        :type rows: list(list)
        :param rows: A list of row values used to initialze the table.
            Each row value should be a tuple of cell values, one for
            each column in the row.
        :type scrollbar: bool
        :param scrollbar: If true, then create a scrollbar for the
            new table widget.
        :type click_to_sort: bool
        :param click_to_sort: If true, then create bindings that will
            sort the table's rows by a given column's values if the
            user clicks on that colum's label.
        :type reprfunc: function
        :param reprfunc: If specified, then use this function to
            convert each table cell value to a string suitable for
            display.  ``reprfunc`` has the following signature:
            reprfunc(row_index, col_index, cell_value) -> str
            (Note that the column is specified by index, not by name.)
        :param cnf, kw: Configuration parameters for this widget's
            contained ``MultiListbox``.  See ``MultiListbox.__init__()``
            for details.
        """
        ...
    
    def pack(self, *args, **kwargs):
        """Position this table's main frame widget in its parent
        widget.  See ``Tkinter.Frame.pack()`` for more info."""
        ...
    
    def grid(self, *args, **kwargs):
        """Position this table's main frame widget in its parent
        widget.  See ``Tkinter.Frame.grid()`` for more info."""
        ...
    
    def focus(self):
        """Direct (keyboard) input foxus to this widget."""
        ...
    
    def bind(self, sequence: Optional[Any] = ..., func: Optional[Any] = ..., add: Optional[Any] = ...):
        """Add a binding to this table's main frame that will call
        ``func`` in response to the event sequence."""
        ...
    
    def rowconfigure(self, row_index, cnf=..., **kw):
        """:see: ``MultiListbox.rowconfigure()``"""
        ...
    
    def columnconfigure(self, col_index, cnf=..., **kw):
        """:see: ``MultiListbox.columnconfigure()``"""
        ...
    
    def itemconfigure(self, row_index, col_index, cnf: Optional[Any] = ..., **kw):
        """:see: ``MultiListbox.itemconfigure()``"""
        ...
    
    def bind_to_labels(self, sequence: Optional[Any] = ..., func: Optional[Any] = ..., add: Optional[Any] = ...):
        """:see: ``MultiListbox.bind_to_labels()``"""
        ...
    
    def bind_to_listboxes(self, sequence: Optional[Any] = ..., func: Optional[Any] = ..., add: Optional[Any] = ...):
        """:see: ``MultiListbox.bind_to_listboxes()``"""
        ...
    
    def bind_to_columns(self, sequence: Optional[Any] = ..., func: Optional[Any] = ..., add: Optional[Any] = ...):
        """:see: ``MultiListbox.bind_to_columns()``"""
        ...
    
    rowconfig = ...
    columnconfig = ...
    itemconfig = ...
    def insert(self, row_index, rowvalue):
        """
        Insert a new row into the table, so that its row index will be
        ``row_index``.  If the table contains any rows whose row index
        is greater than or equal to ``row_index``, then they will be
        shifted down.

        :param rowvalue: A tuple of cell values, one for each column
            in the new row.
        """
        ...
    
    def extend(self, rowvalues):
        """
        Add new rows at the end of the table.

        :param rowvalues: A list of row values used to initialze the
            table.  Each row value should be a tuple of cell values,
            one for each column in the row.
        """
        ...
    
    def append(self, rowvalue):
        """
        Add a new row to the end of the table.

        :param rowvalue: A tuple of cell values, one for each column
            in the new row.
        """
        ...
    
    def clear(self):
        """
        Delete all rows in this table.
        """
        ...
    
    def __getitem__(self, index):
        """
        Return the value of a row or a cell in this table.  If
        ``index`` is an integer, then the row value for the ``index``th
        row.  This row value consists of a tuple of cell values, one
        for each column in the row.  If ``index`` is a tuple of two
        integers, ``(i,j)``, then return the value of the cell in the
        ``i``th row and the ``j``th column.
        """
        ...
    
    def __setitem__(self, index, val):
        """
        Replace the value of a row or a cell in this table with
        ``val``.

        If ``index`` is an integer, then ``val`` should be a row value
        (i.e., a tuple of cell values, one for each column).  In this
        case, the values of the ``index``th row of the table will be
        replaced with the values in ``val``.

        If ``index`` is a tuple of integers, ``(i,j)``, then replace the
        value of the cell in the ``i``th row and ``j``th column with
        ``val``.
        """
        ...
    
    def __delitem__(self, row_index):
        """
        Delete the ``row_index``th row from this table.
        """
        ...
    
    def __len__(self):
        """
        :return: the number of rows in this table.
        """
        ...
    
    def _checkrow(self, rowvalue):
        """
        Helper function: check that a given row value has the correct
        number of elements; and if not, raise an exception.
        """
        ...
    
    @property
    def column_names(self):
        """A list of the names of the columns in this table."""
        ...
    
    def column_index(self, i):
        """
        If ``i`` is a valid column index integer, then return it as is.
        Otherwise, check if ``i`` is used as the name for any column;
        if so, return that column's index.  Otherwise, raise a
        ``KeyError`` exception.
        """
        ...
    
    def hide_column(self, column_index):
        """:see: ``MultiListbox.hide_column()``"""
        ...
    
    def show_column(self, column_index):
        """:see: ``MultiListbox.show_column()``"""
        ...
    
    def selected_row(self):
        """
        Return the index of the currently selected row, or None if
        no row is selected.  To get the row value itself, use
        ``table[table.selected_row()]``.
        """
        ...
    
    def select(self, index: Optional[Any] = ..., delta: Optional[Any] = ..., see: bool = ...):
        """:see: ``MultiListbox.select()``"""
        ...
    
    def sort_by(self, column_index, order=...):
        """
        Sort the rows in this table, using the specified column's
        values as a sort key.

        :param column_index: Specifies which column to sort, using
            either a column index (int) or a column's label name
            (str).

        :param order: Specifies whether to sort the values in
            ascending or descending order:

              - ``'ascending'``: Sort from least to greatest.
              - ``'descending'``: Sort from greatest to least.
              - ``'toggle'``: If the most recent call to ``sort_by()``
                sorted the table by the same column (``column_index``),
                then reverse the rows; otherwise sort in ascending
                order.
        """
        ...
    
    def _sort(self, event):
        """Event handler for clicking on a column label -- sort by
        that column."""
        ...
    
    def _fill_table(self, save_config: bool = ...):
        """
        Re-draw the table from scratch, by clearing out the table's
        multi-column listbox; and then filling it in with values from
        ``self._rows``.  Note that any cell-, row-, or column-specific
        color configuration that has been done will be lost.  The
        selection will also be lost -- i.e., no row will be selected
        after this call completes.
        """
        ...
    
    def _get_itemconfig(self, r, c):
        ...
    
    def _save_config_info(self, row_indices: Optional[Any] = ..., index_by_id: bool = ...):
        """
        Return a 'cookie' containing information about which row is
        selected, and what color configurations have been applied.
        this information can the be re-applied to the table (after
        making modifications) using ``_restore_config_info()``.  Color
        configuration information will be saved for any rows in
        ``row_indices``, or in the entire table, if
        ``row_indices=None``.  If ``index_by_id=True``, the the cookie
        will associate rows with their configuration information based
        on the rows' python id.  This is useful when performing
        operations that re-arrange the rows (e.g. ``sort``).  If
        ``index_by_id=False``, then it is assumed that all rows will be
        in the same order when ``_restore_config_info()`` is called.
        """
        ...
    
    def _restore_config_info(self, cookie, index_by_id: bool = ..., see: bool = ...):
        """
        Restore selection & color configuration information that was
        saved using ``_save_config_info``.
        """
        ...
    
    _DEBUG = ...
    def _check_table_vs_mlb(self):
        """
        Verify that the contents of the table's ``_rows`` variable match
        the contents of its multi-listbox (``_mlb``).  This is just
        included for debugging purposes, to make sure that the
        list-modifying operations are working correctly.
        """
        ...
    


def demo():
    ...

if __name__ == '__main__':
    ...
