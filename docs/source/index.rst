python-libdiscid |release|
==========================

`python-libdiscid` provides Python bindings for :musicbrainz:`libdiscid`.
`libdiscid`'s main purpose is the calculation of identifiers for audio discs
to use for the MusicBrainz_ database.

`python-libdiscid` is released under the :ref:`Expat license <license>`.

Contents
--------

.. toctree::
   :maxdepth: 2

   api
   changelog
   license

Installation
------------

Dependencies
^^^^^^^^^^^^

`python-libdiscid` depends on the following components:

* :musicbrainz:`libdiscid`
* `Cython`__ (>= 0.15)

On Debian based systems, the dependencies are only an `apt-get` away::

 apt-get install cython libdiscid0-dev

`Cython` is also available via `PyPI`__::

 pip install cython

.. __: http://www.cython.org/
.. __: https://pypi.python.org/pypi/Cython/

PyPI
^^^^

`python-libdiscid` is available from `PyPI`__::

 pip install libdiscid

You can also download the tarball from `PyPI`__ manually, unpack
it and run::

 python setup.py install

.. __: https://pypi.python.org/pypi/python-libdiscid/
.. __: https://pypi.python.org/pypi/python-libdiscid/

Usage
-----

:func:`libdiscid.read` provides everything needed to read the information
from a disc and compute the disc id::

 from libdiscid import read
 disc = read()
 print "id: %s" % (disc.id, )

If no additional arguments are passed to :func:`libdiscid.read`,
it will read from :data:`libdiscid.DEFAULT_DEVICE`. If reading is not supported
on your platform, :py:exc:`NotImplentedError` will be raised. If anything goes
wrong while reading from the device, :exc:`libdiscid.discid.DiscError` will
be raised.

Starting with `libdiscid` 0.5.0, it is possible to explicitly state what should
be read. For example, to read the MCN, one would use::

 from libdiscid import read, FEATURE_MCN
 disc = read(features=FEATURE_MCN)

:func:`libdiscid.put` can be used to compute the disc ID based on the first and
last track, the number of total sectors and track offsets::

 from libdiscid import put
 disc = put(first_track, last_track, num_sectors, offsets)
 print "id: %s" % (disc.id, )

Bugs
----

Please report bugs to the project's issue tracker at `GitHub`_.


libdiscid features support
--------------------------

`python-libdiscid` supports all the features introduced by `libdiscid` up to
version 0.5.0, meaning:

* Retrieval of the disc's Media Catalogue Number and retrieving the ISRCs of
  the tracks if you're using `libdiscid` 0.4.0 and above.
* Selective reading support if you're using `libdiscid` 0.5.0 and above.

Please note that if `python-libdiscid` was built against versions of `libdiscid`
prior to 0.4.0 or 0.5.0, `python-libdiscid` has to be rebuilt against the newer
version to detect the features of the newer `libdiscid`.

Other Python bindings
---------------------

There are other Python bindings available. For a full list of bindings check
:musicbrainz:`libdiscid`.

Note that there are similarities between `python-libdiscid` and `python-discid`.
However, there are subtle differences:

* `python-discid` follows the typical usage of `libdiscid`'s API more closely::

    from discid import DiscId
    with DiscId() as disc:
      disc.read()
      # now disk.id, etc. are available

  This also requires the user to clean up the memory manually if the ``with``
  statement is not used. These details are hidden in `python-libdiscid`.
* Although `python-discid`'s ``DiscId`` properties are named similarly to the
  ones of the objects returned by :func:`libdiscid.read` and
  :func:`libdiscid.read`, there are a few properties where the values are not
  the same: :data:`libdiscid.DiscId.track_lengths` and
  :data:`libdiscid.DiscId.track_offsets`
  are noteworthy examples.

.. _GitHub: https://github.com/sebastinas/python-libdiscid
.. _MusicBrainz: http://musicbrainz.org
