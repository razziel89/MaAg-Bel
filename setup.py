import os
import itertools
import fnmatch
from subprocess import Popen, PIPE
from setuptools import setup, Extension, find_packages
from distutils.command.build import build as build_orig

# Misc executables
UNAME = "uname"


def get_long_description():
    """Load the contents of README.md to use as a long description
    
    Returns:
        The content of README.md as a string.
    """
    this_directory = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
    return long_description


# Error classes
class SetupError(RuntimeError):
    """Base error class for this setup file"""

    pass


class CommandNotFoundError(SetupError):
    """Raised when running a command cannot be found"""

    pass


class CannotRunCommandError(SetupError):
    """Raised when running a command returns with an error"""

    pass


# Helper functions
def call_prog(prog, args):
    """Call an executable and return its standard output
    Args:
        prog: (str) - the executable's name
        args: (list of str) - arguments for the executable

    Returns:
        The standard output of the executable called with the given arguments.

    Raises:
        CommandNotFoundError if the executable cannot be found.
        CannotRunCommandError if the executable did not yield an exit code of zero.
    """
    try:
        process = Popen([prog] + args, stdout=PIPE)
    except FileNotFoundError:
        raise CommandNotFoundError("Command '{}' not found".format(prog))
    (output, err) = process.communicate()
    exit_code = process.wait()
    if exit_code != 0:
        raise CannotRunCommandError(
            "Error running '{} {}', error: {}".format(prog, " ".join(args), err)
        )
    else:
        return output


def get_sys_lib_dirs():
    """Obtain system library dirs depending on the architecture.

    This may not be necessary depending on the compiler used. If the program "uname" is
    not installed, the system's architecture cannot be determined and a standard set of
    directories is returned.

    Returns:
        A list of strings containing the paths of the system libraries.
    """
    dirs = ["/usr/lib/"]
    try:
        arch = call_prog(UNAME, ["-m"])
    except CommandNotFoundError:
        arch = None
    if arch is not None:
        dirs.append("/usr/lib/{}-linux-gnu/".format(arch))
    return dirs


def get_sys_include_dirs():
    """Obtain system include dirs depending on the architecture.

    This may not be necessary depending on the compiler used. If the program "uname" is
    not installed, the system's architecture cannot be determined and a standard set of
    directories is returned.

    Returns:
        A list of strings containing the system include paths.
    """
    dirs = ["/usr/include/"]
    try:
        arch = call_prog(UNAME, ["-m"])
    except CommandNotFoundError:
        arch = None
    if arch is not None:
        dirs.append("/usr/include/{}-linux-gnu/".format(arch))
    return dirs


class build(build_orig):
    """A class that allows re-ordering the build process.

    Re-order the commands build_py and build_ext so that build_ext is run first. That
    way, swig-generated Python files will be available for the build_py step.

    Taken from https://stackoverflow.com/questions/50239473/building-a-module-with-setuptools-and-swig
    """

    def finalize_options(self):
        super().finalize_options()
        condition = lambda l: l[0] == "build_ext"
        t1, t2 = itertools.tee(self.sub_commands)
        rest, sub_build_ext = (
            itertools.filterfalse(condition, t1),
            filter(condition, t2),
        )
        self.sub_commands[:] = list(sub_build_ext) + list(rest)


def is_file_type(file, type):
    """Determine whether a file is of a certain type.

    Supported types are "source" and "header". Files ending in ".cpp" or ".c" are
    considered "source" files, whereas files ending in ".hpp" or ".h" are considered
    "header" files.

    Args:
        file: (string) - the name of a file to be checked
        type: (string) - one of the supported file types

    Raises:
        ValueError if the type of file is not known
    """
    if type == "source":
        matches = fnmatch.fnmatch(file, "*.cpp") or fnmatch.fnmatch(file, "*.c")
    elif type == "header":
        matches = fnmatch.fnmatch(file, "*.hpp") or fnmatch.fnmatch(file, "*.h")
    else:
        raise ValueError("Unsupported file type '{}'".format(type))


def get_files_in_dir(dir):
    """Return a list of relative paths to all files in a directory recursively.

    Args:
        dir: (string) - path to a directory
    """
    result = []
    for root, __, files in os.walk(os.path.join(dir)):
        result += [os.path.join(root, f) for f in files]
    return result


def get_ext_modules(basename):
    """Get a list of external modules.

    This will install the OpenBabel C++ module with reduced functionality.

    Args:
        basename: (str) - the name of the main module, used to ensure that any
            extensions are sub-modules

    Returns:
        A list of extensions to be passed to the ext_modules argument of the setup
        function.
    """

    # Determine source files
    files = get_files_in_dir(os.path.join(os.path.curdir, "src"))
    sources = [f for f in files if is_file_type(f, "source")]
    sources.append("maagbel/cpp.i")

    # # Determine header files
    # files += get_files_in_dir(os.path.join(os.path.curdir, "include"))
    # headers = [f for f in files if is_file_type(f, "header")]

    libraries = ["pthread"]
    extra_compile_args = [
        "-std=c++14",
        "-v",
        "-pedantic",
        "-Wall",
        "-Wextra",
        "-fPIC",
        "-O3",
    ]
    swig_opts = ["-c++", "-Iinclude"]

    # Create the main C++ extension with either min or max funtionality
    maagbel_cpp_ext = Extension(
        basename + "._cpp",
        sources=sources,
        include_dirs=get_sys_include_dirs() + ["include"],
        library_dirs=get_sys_lib_dirs(),
        libraries=libraries,
        language="c++",
        swig_opts=swig_opts,
        extra_compile_args=extra_compile_args,
    )
    ext_modules = [maagbel_cpp_ext]

    return ext_modules


def main():
    # Package data
    PACKAGE_DATA = {
        "name": "maagbel",
        "version": 0.1,
        "description": "Reduced fork of OpenBabel for the ManipulateAggregates tools",
        "author": "Torsten Sachse",
        "mail": "torsten.sachse@gmail.com",
        "url": "https://github.com/razziel89/MaAg-bel",
        "long_description": get_long_description(),
        "long_description_content_type": "text/markdown",
    }

    setup(
        ext_modules=get_ext_modules(PACKAGE_DATA["name"]),
        packages=find_packages(),
        cmdclass={"build": build},
        package_data={'': [PACKAGE_DATA["name"]+'/data']},
        **PACKAGE_DATA,
    )


if __name__ == "__main__":
    main()
