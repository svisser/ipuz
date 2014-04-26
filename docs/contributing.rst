Contributing
============

Testing
-------

You can run this library's tests by doing:

::

    python -m unittest discover

Note that all tests run the public interface (``read`` and ``write``) to ensure
we test both of the following:

- The functionality of any particular validation function.
- Whether the exception is raised properly at the top-level.
