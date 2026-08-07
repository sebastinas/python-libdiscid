# Copyright 2013-2021 Sebastian Ramacher <sebastian@ramacher.at>
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

from collections.abc import Mapping, Sequence

class DiscId:
    def __init__(self) -> None: ...
    def read(self, device: str | bytes | None, features: int = 0) -> None: ...
    def put(
        self, first: int, last: int, sectors: int, offsets: Sequence[int]
    ) -> None: ...
    @property
    def id(self) -> str: ...
    @property
    def freedb_id(self) -> str: ...
    @property
    def submission_url(self) -> str: ...
    @property
    def webservice_url(self) -> str: ...
    @property
    def first_track(self) -> int: ...
    @property
    def last_track(self) -> int: ...
    @property
    def sectors(self) -> int: ...
    @property
    def track_offsets(self) -> tuple[int]: ...
    @property
    def track_lengths(self) -> tuple[int]: ...
    @property
    def mcn(self) -> str: ...
    @property
    def track_isrcs(self) -> tuple[str]: ...
    @property
    def device(self) -> str | None: ...
    @property
    def toc(self) -> str | None: ...

def default_device() -> str: ...

FEATURES_MAPPING: Mapping[int, str]
FEATURES: tuple[str]
FEATURE_READ: int
FEATURE_MCN: int
FEATURE_ISRC: int
__discid_version__: str
