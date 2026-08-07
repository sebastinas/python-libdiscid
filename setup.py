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
    if os.path.exists(os.path.join(os.path.curdir, "discid", "discid.h")):
        include_dirs.append(os.path.curdir)

# Python 3.11
py_limited_api_defines = [("Py_LIMITED_API", 0x030B0000)]

setup(
    ext_modules=[
        Extension(
            "libdiscid._discid",
            ["libdiscid/_discid.pyx", "libdiscid/discid-wrapper.c"],
            define_macros=define_macros + py_limited_api_defines,
            include_dirs=include_dirs,
            library_dirs=library_dirs,
            libraries=libraries,
            py_limited_api=True,
        )
    ],
    packages=["libdiscid", "libdiscid.tests", "libdiscid.compat"],
    package_data={
        "libdiscid": ["_discid.pyi", "py.typed"],
    },
    options={"bdist_wheel": {"py_limited_api": "cp311"}},
)
