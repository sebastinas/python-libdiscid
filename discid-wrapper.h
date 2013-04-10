#ifndef DISCID_WRAPPER_H
#define DISCID_WRAPPER_H

#include <discid/discid.h>

// use the availability of DISCID_FEATURE_LENGTH to detect libdiscid < 0.4.0
#ifndef DISCID_FEATURE_LENGTH

enum discid_feature {
	DISCID_FEATURE_READ = 1 << 0,
	DISCID_FEATURE_MCN  = 1 << 1,
	DISCID_FEATURE_ISRC = 1 << 2,
};

#define DISCID_FEATURE_STR_READ "read"
#define DISCID_FEATURE_STR_MCN "mcn"
#define DISCID_FEATURE_STR_ISRC "isrc"

int discid_has_feature(enum discid_feature feature);
char *discid_get_version_string(void);

char* discid_get_mcn(DiscId *d);
char* discid_get_track_isrc(DiscId *d, int track_num);
#endif

#endif
