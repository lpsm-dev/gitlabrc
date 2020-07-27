from setuptools import setup, find_packages

with open("README.rst") as readme_file:
  readme = readme_file.read()

requirements = ["python-gitlab"]

setup(
  author="Lucca Pessoa da Silva Matos",
  author_email="luccapsm@gmail.com",
  description="Command line tool to clone projects inside groups in GitLab",
  install_requires=requirements,
  license="MIT license",
  long_description=readme + "\n\n",
  include_package_data=True,
  keywords=[
    "gitlab", 
    "gitlab-clone",
  ],
  name="gitlab-clone-recurisve",
  packages=find_packages(include=["gitlab_clone_recursive"]),
  url="https://github.com/lpmatos/gitlab-clone",
  version="1.2",
  entry_points={
    "console_scripts": [
      "gitlab-clone-recursive=gitlab_clone_recursive.cli:main",
    ]
  },
  zip_safe=False,
)
