/* src/config.h.in.  Generated from configure.in by autoheader.  */

/* Where the data files are located */
#define BABEL_DATADIR ""

/* The version of Open Babel */
#define BABEL_VERSION "2.3.90"

/* Version check macro
   Can be used like #if (OB_VERSION >= OB_VERSION_CHECK(2, 2, 99)) */
#define OB_VERSION_CHECK(major, minor, patch) ((major<<16)|(minor<<8)|(patch))

/* OB_VERSION is (major << 16) + (minor << 8) + patch */
#define OB_VERSION OB_VERSION_CHECK(2, 3, 90)

// If we are using a recent GCC version with visibility support use it
#ifdef HAVE_GCC_VISIBILITY
  #define OB_EXPORT __attribute__ ((visibility("default")))
  #define OB_IMPORT __attribute__ ((visibility("default")))
  #define OB_HIDDEN __attribute__ ((visibility("hidden")))
#else
 #define OB_EXPORT
 #define OB_IMPORT
 #define OB_HIDDEN
#endif

#ifndef EXTERN
 #define EXTERN   OB_IMPORT extern
#endif
#ifndef OBAPI
 #define OBAPI    OB_IMPORT
#endif
#ifndef OBCOMMON
 #define OBCOMMON OB_IMPORT
#endif
#ifndef OBCONV
 #define OBCONV   OB_IMPORT
#endif
#ifndef OBERROR
 #define OBERROR  OB_IMPORT
#endif
#ifndef OBFPRT
 #define OBFPRT   OB_IMPORT
#endif
#ifndef OBFPTR
 #define OBFPTR   OB_IMPORT
#endif
#ifndef OBMCDL
#define OBMCDL    OB_IMPORT
 #ifndef OBDEPICT
  #define OBDEPICT OB_IMPORT
 #endif
#endif

/* have <sys/time.h> */
#define HAVE_SYS_TIME_H 1

/* have <time.h> */
#define HAVE_TIME_H 1

/* have <sstream> */
#define HAVE_SSTREAM 1

/* have symbol clock_t */
#define HAVE_CLOCK_T 1

/* have symbol rint */
/* #undef HAVE_RINT */

/* have symbol snprintf */
#define HAVE_SNPRINTF 1

/* have symbol sranddev */
/* #undef HAVE_SRANDDEV */

/* have symbol strcasecmp */
#define HAVE_STRCASECMP 1

/* have symbol strncasecmp */
#define HAVE_STRNCASECMP 1

/* have struct clock_t */
#define HAVE_CLOCK_T 1

/* shared pointer implementation to be used */
#define OB_SHARED_PTR_IMPLEMENTATION std::shared_ptr

/* header to be included for shared pointers */
#define OB_SHARED_PTR_HEADER <memory>

/* #undef SCANDIR_NEEDS_CONST */
#ifdef SCANDIR_NEEDS_CONST
 #define SCANDIR_CONST const
#else
 #define SCANDIR_CONST
#endif

#ifndef TIME_WITH_SYS_TIME
  #ifdef HAVE_SYS_TIME
    #ifdef HAVE_TIME
      #define TIME_WITH_SYS_TIME 1
    #else
      #define TIME_WITH_SYS_TIME 0
    #endif
  #else
    #define TIME_WITH_SYS_TIME 0
  #endif
#endif
