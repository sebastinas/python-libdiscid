# distutils: libraries = discid

from libc.string cimport const_char

cdef extern from "discid-wrapper.h":
  ctypedef void* DiscId

  DiscId* discid_new()
  void discid_free(DiscId* d)
  int discid_read(DiscId *d, const_char* device)
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

  ctypedef enum discid_feature:
    DISCID_FEATURE_READ
    DISCID_FEATURE_MCN
    DISCID_FEATURE_ISRC

  char* DISCID_FEATURE_STR_READ
  char* DISCID_FEATURE_STR_MCN
  char* DISCID_FEATURE_STR_ISRC

  int discid_has_feature(int feature)
  char *discid_get_version_string()

  char* discid_get_mcn(DiscId *d)
  char* discid_get_track_isrc(DiscId *d, int track_num)
