libdiscid Python bindings
=========================

python-libdiscid implements Python bindings for libdiscid using Cython. Both
Python 2.x and 3.x are supported.

Dependencies
------------

* libdiscid
* Cython (>= 0.15)

Usage
-----

::

  from libdiscid import read

  disc = read("/dev/cdrom")
  print "id: %s" % (disc.id, )

License
-------

python-libdiscid is release under the Expat license. Check LICENSE for details.
