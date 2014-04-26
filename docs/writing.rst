Writing ipuz puzzles
====================

The following writes the puzzle instance to a JSONP string ``data``:

::

    import ipuz
    data = ipuz.write(puzzle)

As the specification recommends JSONP the above produces a JSONP string.
You can also write a JSON string by using:

::

    import ipuz
    data = ipuz.write(puzzle, json_only=True)

By default the callback function ``ipuz`` is used in the JSONP format. You
can specify a different callback function name as follows:

::

    import ipuz
    data = ipuz.write(puzzle, callback_name="ipuz_function")
