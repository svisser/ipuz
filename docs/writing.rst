Writing ipuz puzzles
====================

The function ``ipuz.write`` converts a puzzle as a Python dictionary object
to a JSON / JSONP string. This function performs no validation
on the provided puzzle and it is the application's responsibility
to construct a valid puzzle that can be read by ``ipuz.read`` or other
applications.

The following writes a Python dictionary ``puzzle`` to a string ``data``:

::

    import ipuz
    data = ipuz.write(puzzle)

For security reasons this function encourages the use of JSON and it therefore
produces a JSON string by default. You can create a JSONP string by
using ``jsonp=True``:

::

    import ipuz
    data = ipuz.write(puzzle, jsonp=True)

By default the callback function ``ipuz`` is used in the JSONP format. You
can specify a different callback function name by using
the ``callback_name`` parameter:

::

    import ipuz
    data = ipuz.write(puzzle, jsonp=True, callback_name="ipuz_function")
