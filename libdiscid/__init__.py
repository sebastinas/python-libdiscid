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

""" cython based Python bindings of libdiscid

libdiscid is a library to calculate MusicBrainz Disc IDs.
This module provides Python-bindings for libdiscid.

>>> disc = libdiscid.read()
>>> disc.id is not None
True
"""

__version__ = '0.1'

from libdiscid.discid import __discid_version__
from libdiscid.discid import DiscId, DEFAULT_DEVICE
from libdiscid.discid import FEATURES, FEATURE_MCN, FEATURE_ISRC

def read(device=None, features=None):
  """ Reads the TOC from the device given as string.

  If no device is given, :data:`DEFAULT_DEVICE` is used. features can be any
  combination of :data:`FEATURE_MCN` and :data:`FEATURE_ISRC`. Note that prior
  to libdiscid version 0.5.0 features has no effect.

  A :exc:`libdiscid.discid.DiscError` exception is raised when reading fails,
  and :py:exc:`NotImplementedError` when libdiscid doesn't support reading
  discs on the current platform.
  """

  disc = DiscId()
  if features is None:
    disc.read(device)
  else:
    disc.read(device, features)
  return disc

def put(first, last, sectors, offsets):
  """ Creates a TOC based on the given offets.

  Takes the *first* and *last* audio tracks, as well as the number of sectors
  and *offsets* as in :attr:`track_offsets`.

  If the operation fails for some reason, a :exc:`libdiscid.discid.DiscError`
  exception raised.
  """

  disc = DiscId()
  disc.put(first, last, sectors, offsets)
  return disc
