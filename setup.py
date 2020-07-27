#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

requirements = ['requests']

setup(
  author="Lucca Pessoa da Silva Matos",
  author_email='luccapsm@gmail.com',
  description="Gitlab tool for recursive clone",
  install_requires=requirements,
  license="MIT license",
  include_package_data=True,
  keywords=[
    'gitlab', 'gitlab-api',
  ],
  name='gitlab-clone-recursive',
  packages=find_packages(include=['gitlab']),
  url='https://github.com/lpmatos/gitlab-clone-recursive',
  version='0.0.2',
  entry_points={
    "console_scripts": [
      "gitlab-clone-recursive=gitlab.cli:main",
    ]
  },
  zip_safe=False,
)
