ipuz
====

Python 2 library for reading and writing ipuz puzzle files. The specification
for the ipuz file format can be found at: http://www.ipuz.org/ . This library
provides validation and wrapping around the puzzle data.

As the puzzle is inherently JSON data it is the application's responsibility
to ensure that the JSON satisfies the constraints of the PuzzleKind prior to
writing the puzzle. This library provides validation and additional
functionality that you might want to use.

ipuz is a trademark of Puzzazz, Inc., used with permission.

Full documentation can be found at http://ipuz.readthedocs.org/en/latest/ or
by installing Sphinx and running `make html` in the docs directory.
