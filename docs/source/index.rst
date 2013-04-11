python-libdiscid
================

`python-libdiscid` provides Python bindings for :musicbrainz:`libdiscid`.
`libdiscid`'s main purpose is the calculation of identifiers for audio discs
to use for the MusicBrainz_ database.

`python-libdiscid` is released under the Expat_ license.

Please report bugs to the project's issue tracker at GitHub_.

Installation
------------

`python-libdiscid` depends on the following components:

* :musicbrainz:`libdiscid`
* Cython_ (>= 0.15)

On Debian based systems, the dependencies are only an `apt-get` away::

 apt-get install cython libdiscid0-dev

`Cython` is also available via `PyPI <_CythonPyPI>`_::

 pip install cython

libdiscid features support
--------------------------

`python-libdiscid` supports all the features introduced by `libdiscid` up to
version 0.5.0, meaning:

* retrieval of the disc's Media Catalogue Number and retrieving the ISRCs of
  the tracks if you're using `libdiscid` 0.4.0 and above
* selective reading support if you're using `libdiscid` 0.5.0 and above

Contents
--------

.. toctree::
   :maxdepth: 2

   usage
   api

.. _Expat: https://en.wikipedia.org/wiki/MIT_License
.. _GitHub: https://github.com/sebastinas/python-libdiscid
.. _MusicBrainz: http://musicbrainz.org
.. _Cython: http://www.cython.org/
.. _CythonPyPI: https://pypi.python.org/pypi/Cython/
