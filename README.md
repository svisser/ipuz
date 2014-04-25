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

Full documentation can be found at http://ipuz.readthedocs.org/en/latest/ .

Reading
=======

The string `data` contains the puzzle:

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

Writing
=======

The following writes the puzzle instance to a JSONP string `data`:

    import ipuz
    data = ipuz.write(puzzle)

As the specification recommends JSONP the above produces a JSONP string.
You can also write a JSON string by using:

    import ipuz
    data = ipuz.write(puzzle, json_only=True)

By default the callback function `ipuz` is used in the JSONP format. You
can specify a different callback function name as follows:

    import ipuz
    data = ipuz.write(puzzle, callback_name="ipuz_function")

Testing
=======

You can run this library's tests by doing:

    python -m unittest discover

Note that all tests run the public interface (`read` and `write`) to ensure
we test each validation function and whether an exception is raised properly.