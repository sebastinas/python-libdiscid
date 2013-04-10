cimport cdiscid
cimport cpython
from cpython cimport bool

""" Python binding of libdiscid

libdiscid is a library to calculate MusicBrainz Disc IDs.
This module provides Python-bindings for libdiscid.

>>> d = DiscId()
>>> d.read()
"""

cdef bool _has_feature(int feature):
  return <bool>cdiscid.discid_has_feature(feature)

class DiscError(IOError):
  """ :func:`DiscId.read` will raise this exception when an error occured.
  """
  pass

cdef unicode _to_unicode(char* s):
  return s.decode('UTF-8', 'strict')

cdef class DiscId:
  """ Class to calculate MusicBrainz Disc IDs.

  >>> d =DiscId()
  >>> d.id
  >>> d.read()
  >>> d.id is not None
  >>> True

  Note that all the properties are only set after an successful read. """

  cdef cdiscid.DiscId *_c_discid
  cdef bint _have_read

  def __cinit__(self):
    self._c_discid = cdiscid.discid_new()
    if self._c_discid is NULL:
      raise MemoryError()

    self._have_read = False

  def __dealloc__(self):
    if self._c_discid is not NULL:
      cdiscid.discid_free(self._c_discid)

  cdef _read(self, char* device = NULL):
    if not cdiscid.discid_read(self._c_discid, device):
      raise DiscError(self._get_error_msg())
    self._have_read = True

  cpdef read(self, unicode device=None):
    """ Reads the TOC from the device given as string.

    If no device is given, the :data:`DEFAULT_DEVICE` is used.

    A :exc:`DiscError` exception is raised when reading fails, and
    :exc:`NotImplementedError` when libdiscid doesn't support reading discs on
    the current platform. """

    if device is None:
      return self._read(NULL)

    py_byte_device = device.encode('UTF-8')
    cdef char* cdevice = py_byte_device
    return self._read(cdevice)

  cdef unicode _get_error_msg(self):
    return _to_unicode(cdiscid.discid_get_error_msg(self._c_discid))

  property id:
    """ The MusicBrainz :musicbrainz:`Disc ID`. """

    def __get__(self):
      if not self._have_read:
        return None
      return _to_unicode(cdiscid.discid_get_id(self._c_discid))

  property freedb_id:
    """ The :musicbrainz:`FreeDB` Disc ID (without category). """

    def __get__(self):
      if not self._have_read:
        return None
      return _to_unicode(cdiscid.discid_get_freedb_id(self._c_discid))

  property submission_url:
    """ Disc ID / TOC Submission URL for MusicBrainz

    With this url you can submit the current TOC as a new MusicBrainz
    :musicbrainz:`Disc ID`. """

    def __get__(self):
      if not self._have_read:
        return None
      return _to_unicode(cdiscid.discid_get_submission_url(self._c_discid))

  property webservice_url:
    """ The web service URL for info about the CD

    With this url you can retrive information about the CD in XML from the
    MusicBrainz web service. """

    def __get__(self):
      if not self._have_read:
        return None
      return _to_unicode(cdiscid.discid_get_webservice_url(self._c_discid))

  property first_track:
    """ Number of the first audio track. """

    def __get__(self):
      if not self._have_read:
        return None
      return cdiscid.discid_get_first_track_num(self._c_discid)

  property last_track:
    """ Number of the last audio track. """

    def __get__(self):
      if not self._have_read:
        return None
      return cdiscid.discid_get_last_track_num(self._c_discid)

  property sectors:
    """ Total sector count. """

    def __get__(self):
      if not self._have_read:
        return None
      return cdiscid.discid_get_sectors(self._c_discid)

  property track_offsets:
    """ A list of all track offsets.

    The first element is the leadout track and contains the total number of
    sectors on the disc. The following elements are the offsets for all
    audio tracks. ``track_offsets[i]`` is the offset for the ``i``-th track.
    """

    def __get__(self):
      if not self._have_read:
        return None
      return [self.sectors] + [cdiscid.discid_get_track_offset(self._c_discid, track) for \
              track in range(self.first_track, self.last_track + 1)]

  property track_lengths:
    """ A list of all track lengths.

    The first element is the length of the pregap of the first track. The
    following elements are the lengths for all audio tracks. ``track_length[i]``
    is the length for the ``i``-th track.
    """

    def __get__(self):
      if not self._have_read:
        return None
      return [self.track_offsets[1]] + [cdiscid.discid_get_track_length(self._c_discid, track) for \
              track in range(self.first_track, self.last_track + 1)]

  property mcn:

    def __get__(self):
      if not _has_feature(cdiscid.DISCID_FEATURE_MCN):
        raise NotImplementedError("MCN is not available with this version " \
                                  "of libdiscid and/or platform")
      if not self._have_read:
        return None
      return _to_unicode(cdiscid.discid_get_mcn(self._c_discid))

  property track_isrcs:

    def __get__(self):
      if not _has_feature(cdiscid.DISCID_FEATURE_ISRC):
        raise NotImplementedError("ISRC is not available with this version " \
                                  "of libdiscid and/or platform")

      if not self._have_read:
        return None
      return [_to_unicode(cdiscid.discid_get_track_isrc(self._c_discid, track)) for \
              track in range(self.first_track, self.last_track + 1)]


DEFAULT_DEVICE = _to_unicode(cdiscid.discid_get_default_device())
""" The default device to use for :func:`DiscId.read` on this platform. """

_FEATURES = {
  cdiscid.DISCID_FEATURE_READ: cdiscid.DISCID_FEATURE_STR_READ,
  cdiscid.DISCID_FEATURE_MCN: cdiscid.DISCID_FEATURE_STR_MCN,
  cdiscid.DISCID_FEATURE_ISRC: cdiscid.DISCID_FEATURE_STR_ISRC
}

cdef _feature_list():
  res = []
  for f, s in _FEATURES.items():
    if _has_feature(f):
      res.append(_to_unicode(s))
  return res

FEATURES = _feature_list()
""" The features libdiscid supports for the libdiscid/platform combination.
"""

__discid_version__ = _to_unicode(cdiscid.discid_get_version_string())
""" Version of libdiscid. """
