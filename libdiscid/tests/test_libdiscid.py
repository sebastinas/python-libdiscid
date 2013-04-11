import unittest
import libdiscid
from libdiscid.discid import DiscError

class TestLibDiscId(unittest.TestCase):
  def test_default_device(self):
    self.assertTrue(libdiscid.DEFAULT_DEVICE is not None)

  def test_features(self):
    self.assertTrue(libdiscid.FEATURES is not None)

  def test_read_fail(self):
    self.assertRaises(DiscError, libdiscid.read, u'/does/not/exist')

  def test_put(self):
    first = 1
    last = 15
    sectors = 258725
    offsets = (150, 17510, 33275, 45910, 57805, 78310, 94650,109580, 132010,
               149160, 165115, 177710, 203325, 215555, 235590)
    disc_id = 'TqvKjMu7dMliSfmVEBtrL7sBSno-'
    freedb_id = 'b60d770f'

    disc = libdiscid.put(first, last, sectors, offsets)
    self.assertTrue(disc is not None)

    self.assertEqual(disc.id, disc_id)
    self.assertEqual(disc.freedb_id, freedb_id)
    self.assertTrue(disc.submission_url is not None)
    self.assertTrue(disc.webservice_url is not None)
    self.assertEqual(disc.first_track, first)
    self.assertEqual(disc.last_track, last)
    self.assertEqual(disc.sectors, sectors)

    self.assertEqual(len(disc.track_offsets), len(offsets))
    for l, r in zip(disc.track_offsets, offsets):
      self.assertEqual(l, r)

  def test_put_fail(self):
    first = 13
    last = 1
    sectors = 13
    offsets = (1, 2, 3, 4, 5, 6, 7)
    self.assertRaises(DiscError, libdiscid.put, first, last, sectors, offsets)

if __name__ == '__main__':
  unittest.main()
