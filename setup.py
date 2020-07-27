from setuptools import setup

setup(name='gitlab-clone',
  version='1.0',
  description='Command line tool to clone projects inside groups in GitLab',
  url='https://github.com/lpmatos/gitlab-clone',
  author='Lucca Pessoa da Silva Matos',
  license='MIT',
  packages=['gitlab-clone'],
  zip_safe=False,
  install_requires=[
    'python-gitlab'
  ],
  entry_points = {
    'console_scripts': ['gitlab-clone=gitlab-clone.cli:main'],
  }
)
