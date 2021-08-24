import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# Package meta-data.
NAME = "hello-world"
DESCRIPTION = "Test all you want to here."
URL = "https://github.com/riemanli/hello-world"
EMAIL = "riemanli@ucla.edu"
AUTHOR = "Rieman Li"
REQUIRES_PYTHON = ">=3.8.0"
VERSION = "0.1.0"

# What packages are required for this module to be executed?
REQUIRED = [
    "numpy",
]

# What packages are optional?
EXTRAS = {
    # 'fancy feature': ['django'],
}

# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the Trove Classifier for that!

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's __version__.py module as a dictionary.
about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(here, project_slug, "__version__.py")) as f:
        exec(f.read(), about)
else:
    about["__version__"] = VERSION


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel --universal".format(sys.executable))

        self.status("Uploading the package to PyPI via Twine…")
        os.system("twine upload dist/*")

        self.status("Pushing git tags…")
        os.system("git tag v{0}".format(about["__version__"]))
        os.system("git push --tags")

        sys.exit()


# This call to setup() does all the work
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    # package_dir is a dictionary with package names for keys and directories
    # for values. The package name represents the “root package” — the
    # directory in the project that contains all Python source files for the
    # package — so in this case the src directory is designated the root package.
    package_dir={"hello-world": "src"},
    # Use find_packages to avoid the burden of specifying all subpackages.
    packages=find_packages(
        where="src", exclude=["tests", "*.tests", "*.tests.*", "tests.*"]
    ),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    # Used to create scripts that call a function within your package.
    # See https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html
    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    # See https://setuptools.readthedocs.io/en/latest/userguide/dependency_management.html
    install_requires=REQUIRED,
    # Declare dependencies for ancillary functions such as “tests” and “docs”.
    # See use cases in
    # https://setuptools.readthedocs.io/en/latest/userguide/dependency_management.html#optional-dependencies
    extras_require=EXTRAS,
    # Tell setup() to copy non-code files.
    include_package_data=True,
    license="MIT",
    # It gives the index and pip some additional metadata about your package.
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    # To use custom commands in setuptool.
    # See https://stackoverflow.com/questions/27817190/what-does-cmdclass-do-in-pythons-setuptools
    cmdclass={
        "upload": UploadCommand,
    },
)
