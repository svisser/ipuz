Contributing
============

Contributions to the ipuz library are very welcome.

Issues
------

Please create a new ticket in the `issue tracker`_ if you find an issue
or if you have a suggestion for a new feature.

Contributing code
-----------------

Code contributions should follow the `PEP 8`_ style guide, include unit tests
and update the documentation where needed.

You can install the necessary dependencies by running:

::

    pip install -r dev-requirements.txt

Contributing documentation
--------------------------

You can update the documentation by making changes to the ``.rst`` files in
the ``docs`` directory and running:

::

    make html

After that you can view the HTML documentation by running:

::

    open _build/html/index.html


Testing
-------

You can run this library's tests by running:

::

    python -m unittest discover

You can run the tests in all supported Python version by running:

::

    tox

You can use `coverage`_ to check whether the tests adequately test the code.

Note that all tests run the public interface (``ipuz.read`` and ``ipuz.write``) to
ensure we test both of the following:

- The functionality of any particular validation function.
- Whether the exception is raised properly at the top-level.

.. _issue tracker: https://github.com/svisser/ipuz/issues
.. _PEP 8: http://legacy.python.org/dev/peps/pep-0008/
.. _coverage: http://nedbatchelder.com/code/coverage/
