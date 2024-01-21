
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension,build_ext

__version__ = "0.0.1"
ext_modules = [
    Pybind11Extension(
        "sts_random",
        ["random_bind.cpp"],  # Sort source files for reproducibility
        define_macros=[("VERSION_INFO", __version__)],
    ),
]

setup(
    name="sts_random",
    version=__version__,
    author="Keegan Hu",
    author_email="hukq16y@gmail.com",
    description="Slay the spire random number generator",
    long_description="",
    ext_modules=ext_modules,
    extras_require={"test": "pytest"},
    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
    python_requires=">=3.7",
)