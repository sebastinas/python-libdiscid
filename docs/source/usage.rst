Usage
=====

:class:`libdiscid.DiscId` provides everything needed to read the information
from a disc and compute the disc id::

 from libdiscid import DiscId
 d = DiscId()
 d.read()
 print "id: %s" % (d.id, )

If no additional arguments are passed to :func:`libdiscid.DiscId.read`,
it will read from :data:`libdiscid.DEFAULT_DEVICE`. If reading is not supported
on your platform, :exc:`NotImplentedError` will be raised. If anything goes
wrong while reading from the device, :exc:`libdiscid.discid.DiscError` will
be raised.
