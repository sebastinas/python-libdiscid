/* Copyright 2013 Sebastian Ramacher <sebastian+dev@ramacher.at>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the “Software”), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

#include "discid-wrapper.h"
#include <string.h>

#ifndef UNUSED
# if defined(__GNUC__) || defined(__CLANG__)
#  define UNUSED(x) UNUSED_ ## x __attribute__((unused))
# elif defined(__LCLINT__)
#  define UNUSED(x) /*@unused@*/ x
# else
#  define UNUSED(x) x
# endif
#endif

#ifndef DISCID_FEATURE_LENGTH

char* discid_get_version_string(void)
{
  return "libdiscid < 0.4.0";
}

int discid_has_feature(enum discid_feature feature)
{
  /* except for GNU Hurd, read is available for all platforms */
#ifndef __GNU__
  if (feature == DISCID_FEATURE_READ)
    return 1;
  else
#endif
    return 0;
}

char* discid_get_mcn(DiscId* UNUSED(d))
{
  return NULL;
}

char* discid_get_track_isrc(DiscId* UNUSED(d), int UNUSED(track_num))
{
  return NULL;
}

#endif /* libdiscid < 0.4.0 */

#if !defined(DISCID_VERSION_MAJOR) || (DISCID_VERSION_MAJOR == 0 && DISCID_VERSION_MINOR < 5)

int discid_read_sparse(DiscId *d, const char *device,
    unsigned int UNUSED(features))
{
  return discid_read(d, device);
}

#endif /* libdiscid < 0.5.0 */
