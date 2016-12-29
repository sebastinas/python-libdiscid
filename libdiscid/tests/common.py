# -*- coding: utf-8 -*-

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

""" Tests for the libdiscid module
"""

from __future__ import unicode_literals


class PutSuccess(object):
  first = 1
  last = 15
  sectors = 258725
  seconds = 3450
  offsets = (150, 17510, 33275, 45910, 57805, 78310, 94650, 109580, 132010,
             149160, 165115, 177710, 203325, 215555, 235590)
  track_seconds = (231, 210, 168, 159, 273, 218, 199, 299, 229, 213, 168, 342,
                   163, 267, 308)
  disc_id = 'TqvKjMu7dMliSfmVEBtrL7sBSno-'
  freedb_id = 'b60d770f'
  toc = ' '.join(map(str, [first, last, sectors] + list(offsets)))

class _PutFail(object):
  sectors = 200
  offsets = (1, 2, 3, 4, 5, 6, 7)

class PutFail1(_PutFail):
  first = 13
  last = 1

class PutFail2(_PutFail):
  first = 0
  last = 10

class PutFail2_2(_PutFail):
  first = 100
  last = 200

class PutFail3(_PutFail):
  first = 0
  last = 0

class PutFail3_2(_PutFail):
  first = 1
  last = 100
