Writing ipuz puzzles
====================

The function ``ipuz.write`` can be used to convert a puzzle as a Python
dictionary object to a JSON / JSONP string. This function performs no validation
on the provided puzzle and as such it is the application's responsibility
to construct a valid puzzle that can be read by ``ipuz.read`` or other
applications.

The following writes a Python dictionary ``puzzle`` to a string called ``data``:

::

    import ipuz
    data = ipuz.write(puzzle)

As the specification recommends JSONP the above produces a JSONP string.
You can create a JSON string by using ``json_only=True``:

::

    import ipuz
    data = ipuz.write(puzzle, json_only=True)

By default the callback function ``ipuz`` is used in the JSONP format. You
can specify a different callback function name by using
the ``callback_name`` parameter:

::

    import ipuz
    data = ipuz.write(puzzle, callback_name="ipuz_function")
