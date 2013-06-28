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

""" Tests for the libdiscid.compat.discid module
"""

import unittest
from libdiscid.compat import discid
from libdiscid.compat.discid import DiscError, TOCError

class TestCompatDiscID(unittest.TestCase):
  def test_default_device(self):
    self.assertTrue(discid.get_default_device() is not None)

  def test_features(self):
    self.assertTrue(discid.FEATURES is not None)

  def test_features_implementes(self):
    self.assertTrue(discid.FEATURES_IMPLEMENTED is not None)


  def test_read_fail(self):
    self.assertRaises(DiscError, discid.read, u'/does/not/exist')

  def test_put(self):
    first = 1
    last = 15
    sectors = 258725
    offsets = (150, 17510, 33275, 45910, 57805, 78310, 94650,109580, 132010,
               149160, 165115, 177710, 203325, 215555, 235590)
    disc_id = 'TqvKjMu7dMliSfmVEBtrL7sBSno-'
    freedb_id = 'b60d770f'

    disc = discid.put(first, last, sectors, offsets)
    self.assertTrue(disc is not None)

    self.assertEqual(disc.id, disc_id)
    self.assertEqual(disc.freedb_id, freedb_id)
    self.assertTrue(disc.submission_url is not None)
    self.assertEqual(disc.first_track_num, first)
    self.assertEqual(disc.last_track_num, last)
    self.assertEqual(disc.sectors, sectors)

    self.assertEqual(len(disc.tracks), len(offsets))
    for track, offset in zip(disc.tracks, offsets):
      self.assertEqual(track.offset, offset)

    # ISRCs are not available if one calls put
    for track in disc.tracks:
        self.assertTrue(track.isrc is None)

    # MCN is not available if one calls put
    self.assertTrue(disc.mcn is None)

  def test_put_fail_1(self):
    # !(first < last)
    first = 13
    last = 1
    sectors = 200
    offsets = (1, 2, 3, 4, 5, 6, 7)
    self.assertRaises(TOCError, discid.put, first, last, sectors, offsets)

  def test_put_fail_2(self):
    # !(first >= 1)
    first = 0
    last = 10
    sectors = 200
    offsets = (1, 2, 3, 4, 5, 6, 7)
    self.assertRaises(TOCError, discid.put, first, last, sectors, offsets)

    # !(first < 100)
    first = 100
    last = 200
    self.assertRaises(TOCError, discid.put, first, last, sectors, offsets)

  def test_put_fail_3(self):
    # !(last >= 1)
    first = 0
    last = 0
    sectors = 200
    offsets = (1, 2, 3, 4, 5, 6, 7)
    self.assertRaises(TOCError, discid.put, first, last, sectors, offsets)

    # !(last < 100)
    first = 1
    last = 100
    self.assertRaises(TOCError, discid.put, first, last, sectors, offsets)


if __name__ == '__main__':
  unittest.main()
