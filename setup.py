# -*- coding: utf-8 -*-

import io
import os
from gitlabrc import __version__
from setuptools import setup, find_packages

# Package meta-data.
NAME              = "gitlabrc"
DESCRIPTION       = "GitlabRC is a CLI that help you to clone all projects inside a specific namespace in Gitlab"
URL               = "https://github.com/lpmatos/gitlabrc"
EMAIL             = "luccapsm@gmail.com"
AUTHOR            = "Lucca Pessoa da Silva Matos"
REQUIRES_PYTHON   = ">=3.6.0"
VERSION           = __version__

# What packages are required for this module to be executed?
REQUIRED = [
  "python-gitlab"
]

# Getting current location of this file.
here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
  with io.open(os.path.join(here, "README.md"), encoding="utf-8") as longdesc:
    LONG_DESCRIPTION = "\n" + longdesc.read()
except FileNotFoundError:
  LONG_DESCRIPTION = DESCRIPTION

# Build setup package.
setup(
  name = NAME,
  version = VERSION,
  description = DESCRIPTION,
  long_description = DESCRIPTION,
  long_description_content_type = "text/markdown",
  author = AUTHOR,
  author_email = EMAIL,
  python_requires = REQUIRES_PYTHON,
  url=URL,
  packages = find_packages(include=[NAME], exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
  install_requires = REQUIRED,
  include_package_data = True,
  license = "MIT license",
  keywords = [
    "gitlab",
    "git",
    "cli",
    "python"
  ],
  entry_points = {
    "console_scripts" : [
      f"{NAME}={NAME}.clone:main",
    ]
  },
  zip_safe = False,
)
