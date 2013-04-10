#include "discid-wrapper.h"
#include <string.h>

#ifndef DISCID_FEATURE_LENGTH

char* discid_get_version_string(void)
{
  return "unknown (pre 0.4)";
}

int discid_has_feature(enum discid_feature feature)
{
  if (feature == DISCID_FEATURE_READ)
    return 1;
  else
    return 0;
}

char* discid_get_mcn(DiscId* d) __atrribute__((weak))
{
  return NULL;
}

char* discid_get_track_isrc(DiscId* d, int track_num) __attribute__((weak))
{
  return NULL;
}

#endif
