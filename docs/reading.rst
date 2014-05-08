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
* Validation of missing mandatory fields.
* Sanity checks for fields where possible.

The error messages are not intended as API but only for informative purposes.
If you read a puzzle from a string and no exception was raised then your code
should not need to perform validation to see whether the puzzle is well-formed.
This library will check types of values and perform various sanity checks to
see whether the JSON conforms to the ipuz specification.

Validation for all puzzles
--------------------------

The ``ipuz.read`` function performs validation for fields that are common to
all PuzzleKinds and validation for fields that are specific to a PuzzleKind.
The function expects a puzzle in JSON or JSONP with either the default
``ipuz`` callback function or a differently named callback function.

Note that ``true``, ``false`` and ``null`` in JSON / JSONP respectively
become ``True``, ``False`` and ``None`` in Python.

The follows checks are performed for fields that apply to all PuzzleKinds:

===========  =========  ===============================================
Field        Mandatory  Validation
===========  =========  ===============================================
version      Yes        Must be the string ``"http://ipuz.org/vX"`` where ``X`` is an integer of at least one.
kind         Yes        Must be a non-empty list of non-empty strings.
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
date         No         Must be a string with a date ``"mm/dd/yyyy"``.
notes        No         Must be a string.
difficulty   No         Must be a string.
origin       No         Must be a string.
block        No         Must be a string.
empty        No         Must be a string or integer.
styles       No         Must be a dictionary with StyleSpec values.
===========  =========  ===============================================

Validation for Acrostic puzzles
-------------------------------

The following checks are performed for PuzzleKinds belonging to ``http://ipuz.org/acrostic``:

===============  =========  ============================================================================
Field            Mandatory  Validation
===============  =========  ============================================================================
puzzle           Yes        Must be a list of lists containing LabeledCell values.
solution         No         Must be a list of lists containing CrosswordValue values.
clues            No         Must be a dictionary with Direction keys and lists of Clue values.
===============  =========  ============================================================================

Validation for Answer puzzles
-----------------------------

The following checks are performed for PuzzleKinds belonging to ``http://ipuz.org/answer``:

===============  =========  ========================================================
Field            Mandatory  Validation
===============  =========  ========================================================
choices          No         Must be a list of strings.
randomize        No         Must be a boolean.
answer           No         Must be a string.
answers          No         Must be a list of strings.
enumeration      No         Must be a string.
enumerations     No         Must be a list of strings.
requiredanswers  No         Must be an integer of at least zero.
misses           No         Must be a dictionary with string keys and string values.
guesses          No         Must be a list of strings.
===============  =========  ========================================================

Validation for Block puzzles
----------------------------

The following checks are performed for PuzzleKinds belonging to ``http://ipuz.org/block``:

==========  =========  ======================================================================================================
Field       Mandatory  Validation
==========  =========  ======================================================================================================
dimensions  Yes        Must be a dictionary containing ``"width"`` and ``"height"`` keys with integer values of at least one.
slide       No         Must be a boolean.
move        No         Must be a boolean.
rotatable   No         Must be a boolean.
flippable   No         Must be a boolean.
field       No         Must be a list of lists containing StyledCell values.
enter       No         Must be a dictionary with string keys and GroupSpec values.
start       No         Must be a dictionary with string keys and GroupSpec values.
saved       No         Must be a dictionary with string keys and GroupSpec values.
end         No         Must be a dictionary with string keys and GroupSpec values.
exit        No         Must be a dictionary with string keys and GroupSpec values.
==========  =========  ======================================================================================================

Validation for Crossword puzzles
--------------------------------

The following checks are performed for PuzzleKinds belonging to ``http://ipuz.org/crossword``:

================  =========  ======================================================================================================
Field             Mandatory  Validation
================  =========  ======================================================================================================
dimensions        Yes        Must be a dictionary containing ``"width"`` and ``"height"`` keys with integer values of at least one.
puzzle            Yes        Must be a list of lists containing LabeledCell values.
saved             No         Must be a list of lists containing CrosswordValue values.
solution          No         Must be a list of lists containing CrosswordValue values.
zones             No         Must be a list of GroupSpec values.
clues             No         Must be a dictionary with Direction keys and lists of Clue values.
showenumerations  No         Must be a boolean.
clueplacement     No         Must be an element from ``["before", "after", "blocks", null]``.
answer            No         Must be a string.
answers           No         Must be a list of strings.
enumeration       No         Must be a string.
enumerations      No         Must be a list of strings.
misses            No         Must be a dictionary with string keys and string values.
================  =========  ======================================================================================================

Validation for Fill puzzles
---------------------------

None yet.

Validation for Sudoku puzzles
-----------------------------

The following checks are performed for PuzzleKinds belonging to ``http://ipuz.org/sudoku``:

==============   =========  ======================================================
Field            Mandatory  Validation
==============   =========  ======================================================
charset          No         Must be a string.
displaycharset   No         Must be a boolean.
boxes            No         Must be a boolean.
showoperators    No         Must be a boolean.
cageborder       No         Must be an element from ``["thick", "dashed"]``.
puzzle           Yes        Must be a list of lists containing SudokuGiven values.
saved            No         Must be a list of lists containing SudokuGuess values.
solution         No         Must be a list of lists containing SudokuValue values.
zones            No         Must be a list of GroupSpec values.
cages            No         Must be a list of CalcSpec values.
==============   =========  ======================================================

Validation for WordSearch puzzles
---------------------------------

The following checks are performed for PuzzleKinds belonging to ``http://ipuz.org/wordsearch``:

===============  =========  ======================================================================================================
Field            Mandatory  Validation
===============  =========  ======================================================================================================
dimensions       Yes        Must be a dictionary containing ``"width"`` and ``"height"`` keys with integer values of at least one.
puzzle           No         Must be a list of lists containing CrosswordValue values.
solution         No         Must be a string, a list of strings or a dictionary with string keys and GroupSpec values.
dictionary       No         Must be a string or the boolean value ``false``.
saved            No         Must be a list of strings.
showanswers      No         Must be an element from ``["during", "after", null]``.
time             No         Must be an integer of at least zero.
points           No         Must be an element from ``["linear", "log", null]``.
zigzag           No         Must be a boolean.
retrace          No         Must be a boolean.
useall           No         Must be a boolean.
misses           No         Must be a dictionary with string keys and string values.
===============  =========  ======================================================================================================

Parameters
----------

The ``ipuz.read`` function supports the following keyword parameters to
configure what puzzles can be loaded:

- ``puzzlekinds``
      Specifies the ``"kind"`` values that your application supports. This
      means ``ipuz.read`` only accepts puzzles where all ``"kind"`` values
      are in your list. For example, if your application only loads crossword
      puzzles you can use ``puzzlekinds=["http://ipuz.org/crossword#1"]``.
      By default ``ipuz.read`` accepts all official PuzzleKinds in the
      ipuz specification.

      Note that this is a list of exact strings so if your application supports
      both version one and two of the Crossword PuzzleKind then you must specify
      ``puzzlekinds=["http://ipuz.org/crossword#1", "http://ipuz.org/crossword#2"]``.

Extensions
----------

For extensions to the ipuz specification the following validation is performed:

========  =========  ========================================================
Field     Mandatory  Validation
========  =========  ========================================================
volatile  No         Must be a dictionary with string keys and string values.
========  =========  ========================================================

It is the application's responsibility to ensure that the volatility of the
fields is handled properly.
