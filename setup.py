# -*- coding: utf-8 -*-

from cloner import __version__
from setuptools import setup, find_packages

requirements = [
  "python-gitlab"
]

setup(
  author = "Lucca Pessoa da Silva Matos",
  author_email = "luccapsm@gmail.com",
  description = "Gitlab tool for recursive clone",
  install_requires = requirements,
  license = "MIT license",
  include_package_data = True,
  keywords = [
    "gitlab",
    "gitlab-api",
  ],
  name = "gitlab-cr",
  packages = find_packages(include=["cloner"]),
  url = "https://github.com/lpmatos/gitlab-clone-recursive",
  version = __version__,
  entry_points = {
    "console_scripts" : [
      "gitlab-cr=cloner.cli:main",
    ]
  },
  zip_safe = False,
)
