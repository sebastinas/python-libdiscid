Usage
-----

Disc ID computation from a disc
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:func:`libdiscid.read` provides everything needed to read the information
from a disc and compute the disc id::

 from libdiscid import read
 disc = read()
 print("id: {}".format(disc.id))

If no additional arguments are passed to :func:`libdiscid.read`,
it will read from :func:`libdiscid.default_device`. If reading is not supported
on your platform, :py:exc:`NotImplementedError` will be raised. If anything
goes wrong while reading from the device, :exc:`libdiscid.discid.DiscError`
will be raised.

To read from a different device than the default one, you can set ``device``
accordingly::

 from libdiscid import read
 disc = read(device=u'/dev/cdrom1')
 print("id: {}".format(disc.id))

Starting with `libdiscid` 0.5.0, it is possible to explicitly state what should
be read. For example, to read the MCN, one would use::

 from libdiscid import read, FEATURE_MCN
 disc = read(features=FEATURE_MCN)
 # disc.id will be available
 print("id: {}".format(disc.id))
 # if the disc has a MCN and libdiscid is 0.4.0 or later and libdiscid
 # supports reading the MCN on this platform, disc.mcn will be non-empty.
 try:
   print("MCN: {}".format(disc.mcn))
 except NotImplementedError:
   print("MCN reading not supported on this platform/with this libdiscid")

If you only want to get the disc id and do not care about the MCN and the ISCRs,
you can tell that to :func:`libdiscid.read` by passing ``0`` or
:data:`libdiscid.FEATURE_READ` to ``features``::

 from libdiscid import read
 disc = read(features=0)

Disc ID computation from data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:func:`libdiscid.put` can be used to compute the disc ID based on the first and
last track, the number of total sectors and track offsets::

 from libdiscid import put
 disc = put(first_track, last_track, num_sectors, offsets)
 print("id: {}".format(disc.id))

Please note that :attr:`libdiscid.DiscId.mcn` and
:attr:`libdiscid.DiscId.track_isrcs` will be empty after a call to
:func:`libdiscid.put`.

python-discid compat module
^^^^^^^^^^^^^^^^^^^^^^^^^^^

:mod:`libdiscid.compat.discid` provides the same API as :py:mod:`discid` from
`python-discid` version 1.0.2. This allows applications to only care about one
API and be usable with either of `python-libdiscid` or `python-discid`
installed. Just use the following code to import the module::

 try:
   from libdiscid.compat import discid
 except ImportError:
   import discid

and then use the :py:mod:`discid` interface.
