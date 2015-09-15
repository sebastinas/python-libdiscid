/* Copyright 2013 Sebastian Ramacher <sebastian+dev@ramacher.at>
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
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

#ifndef DISCID_WRAPPER_H
#define DISCID_WRAPPER_H

#include <discid/discid.h>

#if (defined(__GNUC__) && (__GNUC__ >= 4)) || defined(__clang__)
#	define INTERNAL __attribute__((visibility("hidden")))
#elif defined(__SUNPRO_C)
#	define INTERNAL __hidden
#else
#	define INTERNAL
#endif

/* use the availability of DISCID_FEATURE_LENGTH to detect libdiscid < 0.4.0 */
#ifndef DISCID_FEATURE_LENGTH

enum discid_feature {
	DISCID_FEATURE_READ = 1,
	DISCID_FEATURE_MCN  = 2,
	DISCID_FEATURE_ISRC = 4
};

#define DISCID_FEATURE_STR_READ "read"
#define DISCID_FEATURE_STR_MCN "mcn"
#define DISCID_FEATURE_STR_ISRC "isrc"

#endif /* libdiscid < 0.4.0 */

int wrap_has_feature(enum discid_feature feature) INTERNAL;
char* wrap_get_version_string(void) INTERNAL;

/* discid_get_mcn and discid_get_track_isrc were introduced in 0.3.0 but there
 * is no way to reliable detect if the current platform supports mcn and isrc,
 * so let's assume they are not available and replace them with placeholders */
char* wrap_get_mcn(DiscId* d) INTERNAL;
char* wrap_get_track_isrc(DiscId* d, int track_num) INTERNAL;

/* discid_read_sparse appeared in 0.5.0 */
int wrap_read_sparse(DiscId *d, const char *device, unsigned int features)
  INTERNAL;

/* discid_get_toc_string appeared in 0.6.0 */
char* wrap_get_toc(DiscId* d) INTERNAL;

#endif

