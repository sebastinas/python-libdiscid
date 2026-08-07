# Copyright 2013-2021 Sebastian Ramacher <sebastian+dev@ramacher.at>
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

"""Tests for the libdiscid.compat.discid module"""

import unittest
import libdiscid
from libdiscid.compat import discid
from libdiscid.compat.discid import DiscError, TOCError
from . import common


class TestCompatDiscID(unittest.TestCase):
    def test_default_device(self):
        self.assertIsNotNone(discid.get_default_device())

    def test_features(self):
        self.assertIsNotNone(discid.FEATURES)

    def test_features_implementes(self):
        self.assertIsNotNone(discid.FEATURES_IMPLEMENTED)

    def test_unitialized_assertion_fails(self):
        disc = discid.Disc()
        with self.assertRaises(AssertionError):
            disc.id
        with self.assertRaises(AssertionError):
            disc.freedb_id
        with self.assertRaises(AssertionError):
            disc.submission_url
        with self.assertRaises(AssertionError):
            disc.toc_string
        with self.assertRaises(AssertionError):
            disc.first_track_num
        with self.assertRaises(AssertionError):
            disc.last_track_num
        with self.assertRaises(AssertionError):
            disc.sectors
        with self.assertRaises(AssertionError):
            disc.seconds
        self.assertEqual(len(disc.tracks), 0)

    @unittest.skipIf(
        libdiscid.FEATURES_MAPPING[libdiscid.FEATURE_READ] not in libdiscid.FEATURES,
        "not available on this platform",
    )
    def test_read_fail(self):
        self.assertRaises(DiscError, discid.read, "/does/not/exist")

    def test_read_None(self):
        try:
            discid.read()
        except (DiscError, NotImplementedError):
            pass

    @unittest.skipIf(
        libdiscid.FEATURES_MAPPING[libdiscid.FEATURE_READ] not in libdiscid.FEATURES,
        "not available on this platform",
    )
    def test_encoded_device(self):
        self.assertRaises(DiscError, discid.read, "/does/not/exist")

    @unittest.skipIf(
        libdiscid.FEATURES_MAPPING[libdiscid.FEATURE_READ] not in libdiscid.FEATURES,
        "not available on this platform",
    )
    def test_byte_device(self):
        self.assertRaises(DiscError, discid.read, b"/does/not/exist")

    def test_put(self):
        testdata = common.PutSuccess

        disc = discid.put(
            testdata.first, testdata.last, testdata.sectors, testdata.offsets
        )
        self.assertIsNotNone(disc)

        self.assertEqual(disc.id, testdata.disc_id)
        self.assertEqual(disc.freedb_id, testdata.freedb_id)
        self.assertIsNotNone(disc.submission_url)
        self.assertEqual(disc.toc_string, testdata.toc)
        self.assertEqual(disc.first_track_num, testdata.first)
        self.assertEqual(disc.last_track_num, testdata.last)
        self.assertEqual(disc.pregap, testdata.offsets[0])
        self.assertEqual(disc.sectors, testdata.sectors)
        self.assertEqual(disc.seconds, testdata.seconds)
        expected_cddb_query = [
            testdata.freedb_id,
            testdata.last,
            *testdata.offsets,
            testdata.seconds,
        ]
        self.assertEqual(
            disc.cddb_query_string, " ".join(map(str, expected_cddb_query))
        )

        self.assertEqual(len(disc.tracks), len(testdata.offsets))
        for track, offset, sec in zip(
            disc.tracks, testdata.offsets, testdata.track_seconds
        ):
            self.assertEqual(track.offset, offset)
            self.assertEqual(track.seconds, sec)

        # ISRCs are not available if one calls put
        for track in disc.tracks:
            self.assertIsNone(track.isrc)

        # MCN is not available if one calls put
        self.assertIsNone(disc.mcn)

    def test_put_fail_1(self):
        # !(first < last)
        testdata = common.PutFail1
        self.assertRaises(
            TOCError,
            discid.put,
            testdata.first,
            testdata.last,
            testdata.sectors,
            testdata.offsets,
        )

    def test_put_fail_2(self):
        # !(first >= 1)
        testdata = common.PutFail2
        self.assertRaises(
            TOCError,
            discid.put,
            testdata.first,
            testdata.last,
            testdata.sectors,
            testdata.offsets,
        )

        # !(first < 100)
        testdata = common.PutFail2_2
        self.assertRaises(
            TOCError,
            discid.put,
            testdata.first,
            testdata.last,
            testdata.sectors,
            testdata.offsets,
        )

    def test_put_fail_3(self):
        # !(last >= 1)
        testdata = common.PutFail3
        self.assertRaises(
            TOCError,
            discid.put,
            testdata.first,
            testdata.last,
            testdata.sectors,
            testdata.offsets,
        )

        # !(last < 100)
        testdata = common.PutFail3_2
        self.assertRaises(
            TOCError,
            discid.put,
            testdata.first,
            testdata.last,
            testdata.sectors,
            testdata.offsets,
        )


if __name__ == "__main__":
    unittest.main()
