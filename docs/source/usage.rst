Usage
-----

:func:`libdiscid.read` provides everything needed to read the information
from a disc and compute the disc id::

 from libdiscid import read
 disc = read()
 print "id: %s" % (disc.id, )

If no additional arguments are passed to :func:`libdiscid.read`,
it will read from :data:`libdiscid.DEFAULT_DEVICE`. If reading is not supported
on your platform, :py:exc:`NotImplementedError` will be raised. If anything
goes wrong while reading from the device, :exc:`libdiscid.discid.DiscError`
will be raised.

Starting with `libdiscid` 0.5.0, it is possible to explicitly state what should
be read. For example, to read the MCN, one would use::

 from libdiscid import read, FEATURE_MCN
 disc = read(features=FEATURE_MCN)
 # if the the disc has a MCN and libdiscid is 0.4.0 or later and libdiscid
 # supports reading on this platform, disc.id will be non-empty.
 try:
   print "MCN: %s" % (disc.mcn, )
 except NotImplementedError:
   print "MCN reading not supported on this platform/with this libdiscid"

:func:`libdiscid.put` can be used to compute the disc ID based on the first and
last track, the number of total sectors and track offsets::

 from libdiscid import put
 disc = put(first_track, last_track, num_sectors, offsets)
 print "id: %s" % (disc.id, )

Please note that MCN and ICSRs will be empty after a call to
:func:`libdiscid.put`.
