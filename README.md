ipuz
====

Python library for reading and writing ipuz puzzle files. The specification
for the ipuz file format can be found at: http://www.ipuz.org/. The ipuz file
format supports representing various types of puzzles, including crossword,
sudoku and word search. This Python library provides validation and wrapping
around the puzzle data.

As the puzzle is inherently JSON data it is the application's responsibility
to ensure that the JSON satisfies the constraints of the PuzzleKind prior to
writing the puzzle. This library provides validation and additional
functionality that you might want to use.

The library supports Python 2.7, Python 3.3 and Python 3.4.

ipuz is a trademark of Puzzazz, Inc., used with permission.

Documentation
=============

Documentation can be found at http://ipuz.readthedocs.org/en/latest/.
