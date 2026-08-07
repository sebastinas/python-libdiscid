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

"""python-discid compat layer

This module provides a compatible layer so that python-libdiscid can be used as
a replacement for python-discid. It provides an interface compatible with
python-discid version 1.4.0.
"""

from collections.abc import Iterable, Sequence
import libdiscid
import operator
import functools
import sys

_INVERSE_FEATURES = {
    libdiscid.FEATURES_MAPPING[libdiscid.FEATURE_READ]: libdiscid.FEATURE_READ,
    libdiscid.FEATURES_MAPPING[libdiscid.FEATURE_MCN]: libdiscid.FEATURE_MCN,
    libdiscid.FEATURES_MAPPING[libdiscid.FEATURE_ISRC]: libdiscid.FEATURE_ISRC,
}


def _decode(string: str | bytes, encoding: str | None = None) -> str:
    # Let's do the same thing discid is doing. It always accepts both strings and
    # bytes objects and encodes/decodes them as it sees fit. libdiscid always
    # wants string objects, so let's decode it here on a best effort basis.
    if not isinstance(string, str):
        if encoding is None:
            encoding = sys.getfilesystemencoding() or "ascii"
        return string.decode(encoding)
    return string


# exceptions defined in discid
DiscError = libdiscid.DiscError


class TOCError(Exception):
    pass


# classes defined in discid
class Track:
    def __init__(self, disc: libdiscid.DiscId, number: int) -> None:
        self._disc = disc
        self.number = number

    def __str__(self) -> str:
        return str(self.number)

    @property
    def offset(self) -> int:
        return self._disc.track_offsets[self.number - self._disc.first_track]

    @property
    def sectors(self) -> int:
        return self._disc.track_lengths[self.number - self._disc.first_track]

    length = sectors

    @property
    def seconds(self) -> int:
        return libdiscid.sectors_to_seconds(self.sectors)

    @property
    def isrc(self) -> str | None:
        try:
            value = self._disc.track_isrcs[self.number - self._disc.first_track]
        except NotImplementedError:
            return None
        return value if value != "" else None


class Disc:
    def __init__(self) -> None:
        self._disc: libdiscid.DiscId | None = None
        self.tracks: list[Track] = []

    def read(
        self, device: str | bytes | None = None, features: Iterable[str] | None = None
    ) -> bool:
        if features is None:
            features = []

        self._disc = libdiscid.read(
            device,
            functools.reduce(
                operator.or_,
                (
                    _INVERSE_FEATURES[feature]
                    for feature in features
                    if feature in FEATURES
                ),
                0,
            ),
        )
        self._populate_tracks()
        return True

    def put(
        self, first: int, last: int, disc_sectors: int, track_offsets: Sequence[int]
    ) -> bool:
        try:
            self._disc = libdiscid.put(first, last, disc_sectors, list(track_offsets))
        except DiscError as disc_error:
            raise TOCError(str(disc_error))

        self._populate_tracks()
        return True

    def _populate_tracks(self) -> None:
        assert self._disc is not None
        self.tracks = [
            Track(self._disc, num)
            for num in range(self._disc.first_track, self._disc.last_track + 1)
        ]

    @property
    def id(self) -> str:
        assert self._disc is not None
        return self._disc.id

    @property
    def freedb_id(self) -> str:
        assert self._disc is not None
        return self._disc.freedb_id

    @property
    def submission_url(self) -> str | None:
        assert self._disc is not None
        return self._disc.submission_url

    @property
    def toc_string(self) -> str | None:
        assert self._disc is not None
        return self._disc.toc

    @property
    def first_track_num(self) -> int:
        assert self._disc is not None
        return self._disc.first_track

    @property
    def last_track_num(self) -> int:
        assert self._disc is not None
        return self._disc.last_track

    @property
    def pregap(self) -> int:
        assert self._disc is not None
        return self._disc.pregap

    @property
    def sectors(self) -> int:
        assert self._disc is not None
        return self._disc.sectors

    length = sectors

    @property
    def seconds(self) -> int:
        return libdiscid.sectors_to_seconds(self.sectors)

    @property
    def mcn(self) -> str | None:
        assert self._disc is not None
        try:
            value = self._disc.mcn
        except NotImplementedError:
            return None
        return value if value != "" else None

    @property
    def cddb_query_string(self) -> str:
        assert self._disc is not None
        cddb_query = [
            self.freedb_id,
            self.last_track_num,
            *self._disc.track_offsets,
            libdiscid.sectors_to_seconds(self.sectors),
        ]
        return " ".join(map(str, cddb_query))


# functions defined in discid
get_default_device = libdiscid.default_device


def read(
    device: str | bytes | None = None, features: Iterable[str] | None = None
) -> Disc:
    disc = Disc()
    if features:
        features = map(lambda feature: _decode(feature, "ascii"), features)
    disc.read(_decode(device) if device is not None else None, features)
    return disc


def put(first: int, last: int, disc_sectors: int, track_offsets: Sequence[int]) -> Disc:
    disc = Disc()
    disc.put(first, last, disc_sectors, track_offsets)
    return disc


# constants defined in discid
__version__ = f"1.4.0 (compat layer from python-libdiscid {libdiscid.__version__})"
"""This is the version of python-discid this layer is compatible with. """

LIBDISCID_VERSION_STRING = libdiscid.__discid_version__
FEATURES = libdiscid.FEATURES
FEATURES_IMPLEMENTED = (
    libdiscid.FEATURE_READ,
    libdiscid.FEATURE_MCN,
    libdiscid.FEATURE_ISRC,
)

__all__ = (
    "read",
    "put",
    "get_default_device",
    "__version__",
    "LIBDISCID_VERSION_STRING",
    "FEATURES",
    "FEATURES_IMPLEMENTED",
    "Disc",
    "DiscError",
    "TOCError",
)
