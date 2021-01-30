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

from typing import Optional, Union, List, Tuple, Mapping

class DiscId:
    def __init__(self) -> None: ...
    def read(self, device: Optional[Union[str, bytes]], features: int = 0) -> None: ...
    def put(
        self, first: int, last: int, sectors: int, offsets: Union[List[int], Tuple[int]]
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
    def track_offsets(self) -> Tuple[int]: ...
    @property
    def track_lengths(self) -> Tuple[int]: ...
    @property
    def mcn(self) -> str: ...
    @property
    def track_isrcs(self) -> Tuple[str]: ...
    @property
    def device(self) -> Optional[str]: ...
    @property
    def toc(self) -> Optional[str]: ...

def default_device() -> str: ...

FEATURES_MAPPING: Mapping[int, str]
FEATURES: Tuple[str]
FEATURE_READ: int
FEATURE_MCN: int
FEATURE_ISRC: int
__discid_version__: str
