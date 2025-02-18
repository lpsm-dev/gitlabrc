# -*- coding: utf-8 -*-

from gitlabrc import __version__
from setuptools import setup, find_packages

# ==============================================================================
# CONSTANTS
# ==============================================================================

NAME              = "gitlabrc"
DESCRIPTION       = "GitlabRC is a python CLI that help you to clone projects inside namespace (groups) in Gitlab"
URL               = "https://github.com/lpsm-dev/gitlabrc"
EMAIL             = "lpsn-dev@protonmail.com"
AUTHOR            = "Lucca Matos"
REQUIRES_PYTHON   = ">=3.8.0"
VERSION           = __version__
REQUIRED = [
  "art",
  "tqdm",
  "GitPython",
  "coloredlogs",
  "python-gitlab",
  "python-json-logger",
]

# ==============================================================================
# BUILD PACKAGE
# ==============================================================================

setup(
  name = "GitLabRC",
  version = VERSION,
  description = DESCRIPTION,
  long_description = DESCRIPTION,
  author = AUTHOR,
  author_email = EMAIL,
  python_requires = REQUIRES_PYTHON,
  url=URL,
  packages = find_packages(include=[NAME], exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
  install_requires = REQUIRED,
  include_package_data = True,
  license = "MIT license",
  keywords = [
    "git",
    "cli",
    "python",
    "gitlab",
    "gitlab-cli",
  ],
  entry_points = {
    "console_scripts" : [
      f"{NAME}={NAME}.cli:main",
    ],
  },
  zip_safe = False,
)
