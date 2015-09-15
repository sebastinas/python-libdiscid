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

from libc.string cimport const_char

cdef extern from "discid-wrapper.h":
  ctypedef void* DiscId

  DiscId* discid_new()
  void discid_free(DiscId* d)
  int wrap_read_sparse(DiscId *d, const_char* device, unsigned int features)
  int discid_put(DiscId *d, int first, int last, int *offsets)
  char *discid_get_error_msg(DiscId *d)
  char *discid_get_id(DiscId *d)
  char *discid_get_freedb_id(DiscId *d)
  char *discid_get_submission_url(DiscId *d)
  char *discid_get_webservice_url(DiscId *d)
  char *discid_get_default_device()
  int discid_get_first_track_num(DiscId *d)
  int discid_get_last_track_num(DiscId *d)
  int discid_get_sectors(DiscId *d)
  int discid_get_track_offset(DiscId *d, int track_num)
  int discid_get_track_length(DiscId *d, int track_num)

  cdef enum discid_feature:
    DISCID_FEATURE_READ
    DISCID_FEATURE_MCN
    DISCID_FEATURE_ISRC

  char* DISCID_FEATURE_STR_READ
  char* DISCID_FEATURE_STR_MCN
  char* DISCID_FEATURE_STR_ISRC

  int wrap_has_feature(int feature)
  char* wrap_get_version_string()

  char* wrap_get_mcn(DiscId *d)
  char* wrap_get_track_isrc(DiscId *d, int track_num)

  char* wrap_get_toc(DiscId *d)

