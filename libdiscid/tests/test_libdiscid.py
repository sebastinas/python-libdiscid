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

""" Tests for the libdiscid module
"""

try:
  import unittest2 as unittest
except ImportError:
  import unittest
import libdiscid
from libdiscid import DiscError

# as long as Python 3.2 is supported, hack around the missing u
try:
  u = unicode
except NameError:
  u = str

class TestLibDiscId(unittest.TestCase):
  def test_version(self):
    self.assertIsNotNone(libdiscid.__version__)
    self.assertIsNotNone(libdiscid.__discid_version__)

  def test_default_device(self):
    self.assertIsNotNone(libdiscid.DEFAULT_DEVICE)

  def test_default_device_2(self):
    self.assertIsNotNone(libdiscid.default_device())

  def test_features(self):
    self.assertIsNotNone(libdiscid.FEATURES)
    self.assertIsNotNone(libdiscid.FEATURE_READ)
    self.assertIsNotNone(libdiscid.FEATURE_MCN)
    self.assertIsNotNone(libdiscid.FEATURE_ISRC)
    self.assertIsNotNone(libdiscid.FEATURES_MAPPING)

  @unittest.skipIf(libdiscid.FEATURES_MAPPING[libdiscid.FEATURE_READ] not in
                   libdiscid.FEATURES, 'not available on this platform')
  def test_read_fail(self):
    self.assertRaises(DiscError, libdiscid.read, u('/does/not/exist'))

  def test_read_None(self):
    try:
      libdiscid.read()
    except (DiscError, NotImplementedError):
      pass

  @unittest.skipIf(libdiscid.FEATURES_MAPPING[libdiscid.FEATURE_READ] in
                   libdiscid.FEATURES, 'available on this platform')
  def test_read_not_implemented(self):
    self.assertRaises(NotImplemented, libdiscid.read)

  def test_put(self):
    first = 1
    last = 15
    sectors = 258725
    offsets = (150, 17510, 33275, 45910, 57805, 78310, 94650,109580, 132010,
               149160, 165115, 177710, 203325, 215555, 235590)
    disc_id = u('TqvKjMu7dMliSfmVEBtrL7sBSno-')
    freedb_id = u('b60d770f')
    toc = u(' ').join(map(u, [first, last, sectors] + list(offsets)))

    disc = libdiscid.put(first, last, sectors, offsets)
    self.assertIsNotNone(disc)
    self.assertIsNone(disc.device)

    self.assertEqual(disc.id, disc_id)
    self.assertEqual(disc.freedb_id, freedb_id)
    self.assertIsNotNone(disc.submission_url)
    self.assertEqual(disc.first_track, first)
    self.assertEqual(disc.last_track, last)
    self.assertEqual(disc.sectors, sectors)
    self.assertEqual(disc.pregap, offsets[0])
    self.assertEqual(disc.leadout_track, sectors)
    self.assertEqual(disc.toc, toc)

    self.assertEqual(len(disc.track_offsets), len(offsets))
    for read_offset, expected_offset in zip(disc.track_offsets, offsets):
      self.assertEqual(read_offset, expected_offset)

    # ISRCs are not available if one calls put
    if libdiscid.FEATURES_MAPPING[libdiscid.FEATURE_ISRC] in libdiscid.FEATURES:
      self.assertEqual(len(disc.track_isrcs), 15)
      for read_isrc in disc.track_isrcs:
        self.assertEqual(read_isrc, u(''))

    # MCN is not available if one calls put
    if libdiscid.FEATURES_MAPPING[libdiscid.FEATURE_MCN] in libdiscid.FEATURES:
      self.assertEqual(disc.mcn, u(''))

  def test_put_fail_1(self):
    # !(first < last)
    first = 13
    last = 1
    sectors = 200
    offsets = (1, 2, 3, 4, 5, 6, 7)
    self.assertRaises(DiscError, libdiscid.put, first, last, sectors, offsets)

  def test_put_fail_2(self):
    # !(first >= 1)
    first = 0
    last = 10
    sectors = 200
    offsets = (1, 2, 3, 4, 5, 6, 7)
    self.assertRaises(DiscError, libdiscid.put, first, last, sectors, offsets)

    # !(first < 100)
    first = 100
    last = 200
    self.assertRaises(DiscError, libdiscid.put, first, last, sectors, offsets)

  def test_put_fail_3(self):
    # !(last >= 1)
    first = 0
    last = 0
    sectors = 200
    offsets = (1, 2, 3, 4, 5, 6, 7)
    self.assertRaises(DiscError, libdiscid.put, first, last, sectors, offsets)

    # !(last < 100)
    first = 1
    last = 100
    self.assertRaises(DiscError, libdiscid.put, first, last, sectors, offsets)

  def test_sectors_to_seconds(self):
    # there are 75 sectors per second
    for sectors in range(38):
      # round down for sectors in the first half
      self.assertEqual(libdiscid.sectors_to_seconds(sectors), 0)
    for sectors in range(38, 76):
      # round up for sectors in the second half
      self.assertEqual(libdiscid.sectors_to_seconds(sectors), 1)

if __name__ == '__main__':
  unittest.main()
