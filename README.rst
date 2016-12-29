libdiscid Python bindings
=========================

python-libdiscid implements Python bindings for libdiscid using Cython. Both
Python 2 (>= 2.7) and 3 (>= 3.4) are supported.

Dependencies
------------

* libdiscid
* Cython (>= 0.15, optional)
* pkgconfig (optional)

Note that the tarballs come with pre-built C source for the Cython module. So
Cython is only required if one builds python-libdiscid from the git repository
or if one wants to change anything in the Cython module.

If pkgconfig is installed, setup.py uses libdiscid's pkg-config information to
set include directories, libraries to link, etc.

Quick installation guide
------------------------

python-libdiscid is available in some distributions:

* Debian/Ubuntu: ``apt-get install python-libdiscid`` (Python 2) or
  ``apt-get install python3-libdiscid`` (Python 3)

python-libdiscid can be installed via ``pip``::

  pip install python-libdiscid

or by running::

  python setup.py install

If you just want to try it locally, run::

  python setup.py build_ext -i

and hack right away. You can also run::

  python setup.py build

but please make sure that ``build/lib.*`` is in ``sys.path`` before the source
folder.

A note for Windows users
------------------------

There are eggs available from PyPI that don't require the extension module to be
built. If these are used, it is still required to drop a working discid.dll in
``C:\WINDOWS\system32`` (or wherever it can be found).

Usage
-----

::

  from libdiscid import read

  disc = read("/dev/cdrom")
  print("id: {}".format(disc.id))

License
-------

python-libdiscid is released under the Expat license. Check LICENSE for details.

Build status
------------

|TravisCI|_

.. |TravisCI| image:: https://travis-ci.org/sebastinas/python-libdiscid.svg?branch=master
.. _TravisCI: https://travis-ci.org/sebastinas/python-libdiscid
