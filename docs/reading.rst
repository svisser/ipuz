Reading ipuz puzzles
====================

The string ``data`` contains the puzzle in JSON or JSONP format:

::

    import ipuz

    try:
        puzzle = ipuz.read(data)
    except ipuz.IPUZException:
        # invalid puzzle

This function provides:

* Validation of puzzle structure in JSON or JSONP format.
* Validation of mandatory missing fields.
* Sanity checks for fields where possible.

The error messages are not intended as API but only for informative purposes.
If you read a puzzle from a string and no exception was raised then your code
should not need to perform validation to see whether the puzzle is well-formed.
This library will check types of values and perform various sanity checks to
see whether the JSON conforms to the ipuz specification.

Validation
==========

Note that ``null`` in JSON / JSONP becomes ``None`` in Python.

Validation for all puzzles
--------------------------

The follows checks are performed for fields that apply to all PuzzleKinds:

===========  =========  ===============================================
Field        Mandatory  Validation
===========  =========  ===============================================
version      Yes        Must be "http://ipuz.org/v1".
kind         Yes        Must be a non-empty list of strings.
copyright    No         Must be a string.
publisher    No         Must be a string.
publication  No         Must be a string.
url          No         Must be a string.
uniqueid     No         Must be a string.
title        No         Must be a string.
intro        No         Must be a string.
explanation  No         Must be a string.
annotation   No         Must be a string.
author       No         Must be a string.
editor       No         Must be a string.
date         No         Must be a string with a date "mm/dd/yyyy".
notes        No         Must be a string.
difficulty   No         Must be a string.
origin       No         Must be a string.
block        No         Must be a string.
empty        No         Must be a string or integer.
styles       No         Must be a dictionary with StyleSpec values.
===========  =========  ===============================================

Validation for Crossword puzzles
--------------------------------

The following checks are performed for PuzzleKinds belonging to ``http://ipuz.org/crossword``:

================  =========  ==============================================================================================
Field             Mandatory  Validation
================  =========  ==============================================================================================
dimensions        Yes        Must be a dictionary containing "width" and "height" keys with integer values of at least one.
puzzle            Yes        Must be a list of lists containing LabeledCell values.
saved             No         Must be a list of lists containing CrosswordValue values.
solution          No         Must be a list of lists containing CrosswordValue values.
zones             No         Must be a list of GroupSpec values.
clues             No         Must be a dictionary with Direction keys and non-empty lists of Clue values.
showenumerations  No         Must be a boolean.
clueplacement     No         Must be an element from ``["before", "after", "blocks", null]``.
answer            No         Must be a non-empty string.
answers           No         Must be a non-empty list of non-empty strings.
enumeration       No         Must be a string.
enumerations      No         Must be a list of strings.
misses            No         Must be a dictionary with string keys and string values.
================  =========  ==============================================================================================
