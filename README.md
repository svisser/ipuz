ipuz
====

Library for reading and writing ipuz puzzle files. The specification
for the ipuz file format can be found at: http://www.ipuz.org/

ipuz is a trademark of Puzzazz, Inc., used with permission.

Reading
=======

The string `data` contains the puzzle:

    import ipuz
    puzzle = ipuz.read(data)

Writing
=======

The following writes the puzzle instance to a JSONP string `data`:

    import ipuz
    data = ipuz.write(puzzle)

As the specification recommends JSONP the above produces a JSONP string.
You can also write a JSON string by using:

    import ipuz
    data = ipuz.write(puzzle, json_only=True)

Testing
=======

You can run this library's tests by doing:

    python -m unittest discover
