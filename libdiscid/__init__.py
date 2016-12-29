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

""" Python bindings for libdiscid

libdiscid is a library to calculate MusicBrainz Disc IDs.
This module provides Python-bindings for libdiscid.

>>> disc = libdiscid.read()
>>> disc.id is not None
True
"""

from __future__ import division

import libdiscid._discid
from libdiscid.exceptions import DiscError
import re
import warnings

__version__ = '0.4.1'

DEFAULT_DEVICE = libdiscid._discid.default_device()
""" The default device to use for :func:`DiscId.read` on this platform.

.. deprecated:: 0.2.0
   Please use :func:`default_device` instead.
"""

FEATURES = libdiscid._discid.FEATURES
""" List of all available features supported by libdiscid on this platform.
"""
FEATURE_READ = libdiscid._discid.FEATURE_READ
""" Read the TOC of the disc to get the disc ID. This feature is always enabled.
"""
FEATURE_MCN = libdiscid._discid.FEATURE_MCN
"""  Read the Media Catalogue Number of the disc.
"""
FEATURE_ISRC = libdiscid._discid.FEATURE_ISRC
""" Read :musicbrainz:`International Standard Recording Codes <ISRC>` of all the
    tracks.
"""
FEATURES_MAPPING = libdiscid._discid.FEATURES_MAPPING
""" Mapping between the constants representing a feature and their string
    representation.
"""
__discid_version__ = libdiscid._discid.__discid_version__
""" The version of the underlying libdiscid.
"""

class DiscId(object):
  """ Disc information

  Class holding all the information obtained from a disc.
  """

  def __init__(self, cdiscid):
      self._id = cdiscid.id
      self._freedb_id = cdiscid.freedb_id
      self._submission_url = cdiscid.submission_url
      self._webservice_url = cdiscid.webservice_url
      self._first_track = cdiscid.first_track
      self._last_track = cdiscid.last_track
      self._sectors = cdiscid.sectors
      self._track_offsets = cdiscid.track_offsets
      self._track_lengths = cdiscid.track_lengths
      self._mcn = cdiscid.mcn
      self._track_isrcs = cdiscid.track_isrcs
      self._device = cdiscid.device
      self._toc = cdiscid.toc

  @property
  def id(self):
    """ The MusicBrainz :musicbrainz:`Disc ID`.
    """

    return self._id

  @property
  def freedb_id(self):
    """ The :musicbrainz:`FreeDB` Disc ID (without category).
    """

    return self._freedb_id

  @property
  def submission_url(self):
    """ Disc ID / TOC Submission URL for MusicBrainz

    With this url you can submit the current TOC as a new MusicBrainz
    :musicbrainz:`Disc ID`.
    """

    return self._submission_url

  @property
  def webservice_url(self):
    """ The web service URL for info about the CD

    With this url you can retrieve information about the CD in XML from the
    MusicBrainz web service.
    """

    warnings.warn('webservice_url is deprecated since it points to the old '
                  'webservice. Please use python-musicbrainz-ngs to access '
                  'the webservice.', DeprecationWarning)
    return self._webservice_url

  @property
  def first_track(self):
    """ Number of the first audio track.
    """

    return self._first_track

  @property
  def last_track(self):
    """ Number of the last audio track.
    """

    return self._last_track

  @property
  def sectors(self):
    """ Total sector count.
    """

    return self._sectors

  @property
  def leadout_track(self):
    """ Leadout track.
    """

    return self.sectors

  @property
  def track_offsets(self):
    """ Tuple of all track offsets (in sectors).

    The first element corresponds to the offset of the track denoted by
    :attr:`first_track` and so on.
    """

    return self._track_offsets

  @property
  def pregap(self):
    """ Pregap of the first track (in sectors).
    """

    return self.track_offsets[0]


  @property
  def track_lengths(self):
    """ Tuple of all track lengths (in sectors).

    The first element corresponds to the length of the track denoted by
    :attr:`first_track` and so on.
    """

    return self._track_lengths

  @property
  def mcn(self):
    """ Media Catalogue Number of the disc.

    :raises NotImplementedError: reading MCN is not supported on this platform
    """

    if self._mcn is None:
      raise NotImplementedError('MCN is not available with this version '
                                'of libdiscid and/or platform')
    return self._mcn

  @property
  def track_isrcs(self):
    """ Tuple of :musicbrainz:`ISRCs <ISRC>` of all tracks.

    The first element of the list corresponds to the ISRC of the
    :attr:`first_track` and so on.

    :raises NotImplementedError: reading ISRCs is not supported on this platform
    """

    if self._track_isrcs is None:
      raise NotImplementedError('ISRC is not available with this version '
                                'of libdiscid and/or platform')
    return self._track_isrcs

  @property
  def device(self):
    """ The device the data was read from.

    If it is ``None``, :func:`libdiscid.put` was called to create the instance.
    """

    return self._device

  @property
  def toc(self):
    """ String representing the CD's Table of Contents (TOC).

    :raises ValueError: extracting TOC string from the submission URL failed
    """

    if self._toc is None:
      # extract TOC string from submission URL
      match = re.match(r'.*toc=([0-9+]+)$', self.submission_url)
      if match is None:
        raise ValueError('Failed to extract TOC from submission URL')
      self._toc = match.group(1).replace('+', ' ')
    return self._toc

def read(device=None, features=None):
  """ Reads the TOC from the device given as string.

  If *device* is ``None``, :func:`default_device` is used to determine
  the device. *features* can be any combination of :data:`FEATURE_MCN` and
  :data:`FEATURE_ISRC` and :data:`FEATURE_READ`. Note that prior to libdiscid
  version 0.5.0 *features* has no effect and that :data:`FEATURE_READ` is always
  assumed, even if not given.

  :param device: device to read from
  :type device: unicode or None
  :param features: selected features, possible values are :data:`FEATURE_READ` \
    :data:`FEATURE_MCN`, :data:`FEATURE_ISRC` and any of these values combined \
    with bitwise or.
  :type features: integer or None
  :raises libdiscid.DiscError: reading the disc failed
  :raises NotImplementedError: reading discs is not supported
  :raises MemoryError: failed to allocate the internal DiscId object
  :rtype: :class:`DiscId` object
  """

  disc = libdiscid._discid.DiscId()
  if features is None:
    disc.read(device)
  else:
    disc.read(device, features)
  return DiscId(disc)

def put(first, last, sectors, offsets):
  """ Creates a TOC based on the given offsets.

  Takes the *first* and *last* audio track, as well as the number of
  *sectors* and a list of *offsets* as in :attr:`track_offsets`.

  :param first: number of the first audio track
  :type first: integer
  :param last: number of the last audio track
  :type last: integer
  :param sectors: total number of sectors on the disc
  :type sectors: integer
  :param offsets: offsets of each track
  :type offsets: list or tuple of integers
  :raises libdiscid.DiscError: operation failed for some reason
  :raises MemoryError: failed to allocated memory to store the offsets or the \
    internal DiscId object
  :rtype: :class:`DiscId` object
  """

  disc = libdiscid._discid.DiscId()
  disc.put(first, last, sectors, offsets)
  return DiscId(disc)

def default_device():
  """ The default device on this platform.

  The default device can change during the run-time of the program. This can
  happen with removable devices for example.

  :rtype: unicode
  """

  return libdiscid._discid.default_device()

def sectors_to_seconds(sectors):
  """ Convert sectors to seconds rounded to the nearest second.

  :param sectors: number of sectors
  :type sectors: integer
  :rtype: integer
  """

  SECTORS_PER_SECOND = 75
  remainder = sectors % SECTORS_PER_SECOND
  return sectors // SECTORS_PER_SECOND + \
    (1 if remainder > SECTORS_PER_SECOND // 2 else 0)

__all__ = (
  'read', 'put', 'default_device', 'sectors_to_seconds',
  '__version__', '__discid_version__',
  'FEATURES', 'FEATURES_MAPPING', 'FEATURE_READ', 'FEATURE_MCN', 'FEATURE_ISRC',
  'DEFAULT_DEVICE',
  'DiscId', 'DiscError'
)
