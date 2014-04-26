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
