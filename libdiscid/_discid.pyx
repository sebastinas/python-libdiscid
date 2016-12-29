# -*- coding: utf-8 -*-

# Copyright 2013 Sebastian Ramacher <sebastian+dev@ramacher.at>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

cimport cdiscid
cimport cpython
from libc cimport limits
from libc.stdlib cimport malloc, free
from cpython cimport bool
from libdiscid.exceptions import DiscError

cdef bool _has_feature(int feature):
  return cdiscid.wrap_has_feature(feature) == 1

cdef unicode _to_unicode(char* s):
  return s.decode('UTF-8', 'strict')

cdef class DiscId:
  """ Class to calculate MusicBrainz Disc IDs.

  >>> d = DiscId()
  >>> d.read()
  >>> d.id is not None
  True

  Note that all the properties are only set after an successful call to
  :func:`DiscId.read` or :func:`DiscId.put`.
  """

  cdef cdiscid.DiscId *_c_discid
  cdef bool _have_read
  cdef unicode _device

  def __cinit__(self):
    self._c_discid = cdiscid.discid_new()
    if self._c_discid is NULL:
      raise MemoryError('Failed to allocate DiscId object')

    self._have_read = False
    self._device = None

  def __dealloc__(self):
    if self._c_discid is not NULL:
      cdiscid.discid_free(self._c_discid)

  cdef _read(self, char* device, unsigned int features):
    if not _has_feature(cdiscid.DISCID_FEATURE_READ):
      raise NotImplementedError('read is not available with this version of '
                                'libdiscid and/or platform')

    if not cdiscid.wrap_read_sparse(self._c_discid, device, features):
      raise DiscError(self._get_error_msg())
    self._have_read = True

  def read(self, unicode device=None, unsigned int features=limits.UINT_MAX):
    """ Reads the TOC from the device given as string.

    If *device* is ``None``, :func:`libdiscid.default_device` is used.
    *features* can be any combination of :data:`FEATURE_MCN` and
    :data:`FEATURE_ISRC` and :data:`FEATURE_READ`. Note that prior to libdiscid
    version 0.5.0 *features* has no effect and that :data:`FEATURE_READ` is
    always assumed, even if not given.

    A :exc:`libdiscid.DiscError` exception is raised when reading fails, and
    :py:exc:`NotImplementedError` when libdiscid does not support reading discs
    on the current platform.
    """

    if device is None:
      device = default_device()

    py_byte_device = device.encode('UTF-8')
    cdef char* cdevice = py_byte_device
    ret = self._read(cdevice, features)
    self._device = device

  cdef _put(self, int first, int last, int* offsets):
    if not cdiscid.discid_put(self._c_discid, first, last, offsets):
      raise DiscError(self._get_error_msg())
    self._device = None
    self._have_read = True

  def put(self, int first, int last, int sectors, offsets):
    """ Creates a TOC based on the given offsets.

    Takes the *first* and *last* audio track, as well as the number of
    *sectors* and a list of *offsets* as in :attr:`DiscId.track_offsets`.

    If the operation fails for some reason, a :exc:`libdiscid.DiscError`
    exception is raised.
    """

    cdef int* coffsets = <int*> malloc((len(offsets) + 1) * sizeof(int))
    if coffsets is NULL:
      raise MemoryError('Failed to allocate memory to store offsets')

    try:
      coffsets[0] = sectors
      for (i, v) in enumerate(offsets):
        coffsets[i + 1] = v
      return self._put(first, last, coffsets)
    finally:
      free(coffsets)

  cdef unicode _get_error_msg(self):
    return _to_unicode(cdiscid.discid_get_error_msg(self._c_discid))

  property id:
    """ The MusicBrainz :musicbrainz:`Disc ID`.
    """

    def __get__(self):
      return _to_unicode(cdiscid.discid_get_id(self._c_discid))

  property freedb_id:
    """ The :musicbrainz:`FreeDB` Disc ID (without category).
    """

    def __get__(self):
      return _to_unicode(cdiscid.discid_get_freedb_id(self._c_discid))

  property submission_url:
    """ Disc ID / TOC Submission URL for MusicBrainz

    With this url you can submit the current TOC as a new MusicBrainz
    :musicbrainz:`Disc ID`.
    """

    def __get__(self):
      return _to_unicode(cdiscid.discid_get_submission_url(self._c_discid))

  property webservice_url:
    """ The web service URL for info about the CD

    With this url you can retrieve information about the CD in XML from the
    MusicBrainz web service.
    """

    def __get__(self):
      return _to_unicode(cdiscid.discid_get_webservice_url(self._c_discid))

  property first_track:
    """ Number of the first audio track.
    """

    def __get__(self):
      return cdiscid.discid_get_first_track_num(self._c_discid)

  property last_track:
    """ Number of the last audio track.
    """

    def __get__(self):
      return cdiscid.discid_get_last_track_num(self._c_discid)

  property sectors:
    """ Total sector count.
    """

    def __get__(self):
      return cdiscid.discid_get_sectors(self._c_discid)

  property track_offsets:
    """ Tuple of all track offsets (in sectors).

    The first element corresponds to the offset of the track denoted by
    :attr:`first_track` and so on.
    """

    def __get__(self):
      return tuple(cdiscid.discid_get_track_offset(self._c_discid, track)
                   for track in range(self.first_track, self.last_track + 1))

  property track_lengths:
    """ Tuple of all track lengths (in sectors).

    The first element corresponds to the length of the track denoted by
    :attr:`first_track` and so on.
    """

    def __get__(self):
      return tuple(cdiscid.discid_get_track_length(self._c_discid, track)
                   for track in range(self.first_track, self.last_track + 1))

  property mcn:
    """ Media Catalogue Number of the disc.
    """

    def __get__(self):
      if not _has_feature(cdiscid.DISCID_FEATURE_MCN):
        return None
      return _to_unicode(cdiscid.wrap_get_mcn(self._c_discid))

  property track_isrcs:
    """ Tuple of :musicbrainz:`ISRCs <ISRC>` of all tracks.

    The first element of the list corresponds to the ISRC of the
    :attr:`first_track` and so on.
    """

    def __get__(self):
      if not _has_feature(cdiscid.DISCID_FEATURE_ISRC):
        return None
      return tuple(_to_unicode(cdiscid.wrap_get_track_isrc(self._c_discid,
                                                           track)) for
                   track in range(self.first_track, self.last_track + 1))

  property device:
    """ The device the data was read from.

    If it is ``None``, :func:`libdiscid.put` was called to create the instance.
    """

    def __get__(self):
      return self._device

  property toc:
    """ String representing the CD's Table of Contents (TOC).
    """

    def __get__(self):
      assert self._have_read

      cdef char* tocstr = cdiscid.wrap_get_toc(self._c_discid)
      if tocstr is not NULL:
        return _to_unicode(tocstr)
      return None

FEATURES_MAPPING = {
    cdiscid.DISCID_FEATURE_READ: _to_unicode(cdiscid.DISCID_FEATURE_STR_READ),
    cdiscid.DISCID_FEATURE_MCN: _to_unicode(cdiscid.DISCID_FEATURE_STR_MCN),
    cdiscid.DISCID_FEATURE_ISRC: _to_unicode(cdiscid.DISCID_FEATURE_STR_ISRC)
}

cdef _feature_list():
  res = []
  for f, s in FEATURES_MAPPING.items():
    if _has_feature(f):
      res.append(s)
  return res

def default_device():
  """ The default device on this platform.
  """

  return _to_unicode(cdiscid.discid_get_default_device())

FEATURES = _feature_list()
FEATURE_READ = cdiscid.DISCID_FEATURE_READ
FEATURE_MCN = cdiscid.DISCID_FEATURE_MCN
FEATURE_ISRC = cdiscid.DISCID_FEATURE_ISRC
__discid_version__ = _to_unicode(cdiscid.wrap_get_version_string())

