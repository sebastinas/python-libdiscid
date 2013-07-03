libdiscid Python bindings
=========================

python-libdiscid implements Python bindings for libdiscid using Cython. Both
Python 2.x and 3.x are supported.

Dependencies
------------

* libdiscid
* Cython (>= 0.15)

Quick installation guide
------------------------

libdiscid can be installed via ``pip``::

  pip install libdiscid

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
  print "id: %s" % (disc.id, )

License
-------

python-libdiscid is release under the Expat license. Check LICENSE for details.
