Changelog
=========

1.0 (2021-03-20)
----------------

* Added support for ipuz v2 (by @maiamcc)
* Add support for Python 3.6, 3.7, 3.8 and 3.9.
* Drop support for Python 3.5 and below. These versions of Python are
  no longer officially supported.
* Removed `six` dependency as we no longer need it.
* Removed `IPUZ_MANDATORY_FIELDS` and `IPUZ_OPTIONAL_FIELDS` as constants
  available from `ipuz.core`. These constants should not be relied upon for
  validation as in the future we may need to support different sets of
  mandatory / optional fields depending on the ipuz version).

0.1.4 (2015-08-21)
------------------

* New version number needed thanks to PyPI.

0.1.3 (2015-08-21)
------------------

* Fixed incorrect README file in setup.py.

0.1.2 (2015-08-21)
------------------

* Dropped version number for six to allow more flexibility in what six version is used.

0.1.1 (2014-08-15)
------------------

* Fixed package structure.
* Added support for Python 3.2.
* Added ability to validate multiple versions of the standard.
* Added constant ipuz.IPUZ_VERSIONS containing versions that this library can validate.

0.1 (2014-05-24)
----------------

* Initial release.
