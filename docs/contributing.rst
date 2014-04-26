Contributing
============

Contributions to the ipuz library are very welcome.

Issues
------

If you find an issue or have a suggestion for a new feature then you can
create a new ticket in the `issue tracker`_ or you can comment on an existing
ticket if a similar ticket already exists.

Contributing code
-----------------

Code contributions should follow the `PEP 8`_ style guide, include unit tests
and update the documentation where needed.

You can install the necessary dependencies by running:

::

    pip install -r dev-requirements.txt


Testing
-------

You can run this library's tests by doing:

::

    python -m unittest discover

Note that all tests run the public interface (``read`` and ``write``) to ensure
we test both of the following:

- The functionality of any particular validation function.
- Whether the exception is raised properly at the top-level.

.. _issue tracker: https://github.com/svisser/ipuz/issues
.. _PEP 8: http://legacy.python.org/dev/peps/pep-0008/
