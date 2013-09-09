# -*- coding: utf-8 -*-

# Copyright 2013 Sebastian Ramacher <sebastian+dev@ramacher.at>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
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

__version__ = '0.3.1'

import libdiscid._discid
from libdiscid._discid import DiscId
from libdiscid.exceptions import DiscError

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


def read(device=None, features=None):
  """ Reads the TOC from the device given as string.

  If *device* is ``None``, :data:`DEFAULT_DEVICE` is used. *features* can be
  any combination of :data:`FEATURE_MCN` and :data:`FEATURE_ISRC` and
  :data:`FEATURE_READ`. Note that prior to libdiscid version 0.5.0 *features*
  has no effect and that :data:`FEATURE_READ` is always assumed, even if not
  given.

  A :exc:`libdiscid.DiscError` exception is raised when reading fails, and
  :py:exc:`NotImplementedError` when libdiscid does not support reading discs on
  the current platform.
  """

  disc = DiscId()
  if features is None:
    disc.read(device)
  else:
    disc.read(device, features)
  return disc

def put(first, last, sectors, offsets):
  """ Creates a TOC based on the given offets.

  Takes the *first* and *last* audio track, as well as the number of
  *sectors* and a list of *offsets* as in :attr:`track_offsets`.

  If the operation fails for some reason, a :exc:`libdiscid.DiscError`
  exception is raised.
  """

  disc = DiscId()
  disc.put(first, last, sectors, offsets)
  return disc

def default_device():
  """ The default device on this platform.

  The default device can change during the run-time of the program. This can
  happen with removable devices for example.
  """

  return libdiscid._discid.default_device()

__all__ = [
  'read', 'put', 'default_device',
  '__version__', '__discid_version__',
  'FEATURES', 'FEATURES_MAPPING', 'FEATURE_READ', 'FEATURE_MCN', 'FEATURE_ISRC',
  'DEFAULT_DEVICE',
  'DiscId', 'DiscError'
]
