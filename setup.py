#!/usr/bin/python3

import os.path
import os

from setuptools import setup, Extension

try:
    import pkgconfig

    def pkgconfig_exists(package):
        try:
            return pkgconfig.exists(package)
        except OSError:
            return False

except ImportError:

    def pkgconfig_exists(package):
        return False


if pkgconfig_exists("libdiscid"):
    flags = pkgconfig.parse("libdiscid")
    define_macros = flags["define_macros"]
    include_dirs = flags["include_dirs"]
    library_dirs = flags["library_dirs"]
    libraries = list(flags["libraries"])
else:
    define_macros = []
    include_dirs = []
    library_dirs = []
    libraries = ["discid"]

    # TODO: Solve this properly by passing CFLAGS and LDFLAGS via CIBW_ENVIRONMENT. For some reason,
    # CFLAGS and LDFLAGS seem to be ignored when built through cibuildwheel.
    LIBDISCID_HOME = os.environ.get("LIBDISCID_HOME", None)
    if LIBDISCID_HOME is not None:
        library_dirs.append(os.path.join(LIBDISCID_HOME, "libdiscid-0.6.1-win32"))
        include_dirs.append(
            os.path.join(
                LIBDISCID_HOME, "libdiscid-0.6.1-win32", "libdiscid-0.6.1", "include"
            )
        )


setup(
    ext_modules=[
        Extension(
            "libdiscid._discid",
            ["libdiscid/_discid.pyx", "libdiscid/discid-wrapper.c"],
            define_macros=define_macros,
            include_dirs=include_dirs,
            library_dirs=library_dirs,
            libraries=libraries,
        )
    ],
    packages=["libdiscid", "libdiscid.tests", "libdiscid.compat"],
    package_data={
        "libdiscid": ["_discid.pyi", "py.typed"],
    },
    test_suite="libdiscid.tests",
)
