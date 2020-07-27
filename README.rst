=================
gitlab-clone-recursive
=================


Tool for easy cloning whole gitlab structure to your local machine.


* Free software: MIT license



Requirements
------------

* Python-GitLab
* Python >= 3.6


Installation
------------

You can install "gitlab-clone-recursive" via `pip`_::

    $ pip install gitlab-clone-recursive


Usage
-----


>>> gitlab-clone-recursive:
  optional arguments:
  -h, --help           show this help message and exit
  --group_id group_id  Id of a group in gitlab
  --token token        Gitlab Token
  --branch branch      Branch to clone in all repos [by default master]
  --gitlab-url gitlab  Gitlab address [by default gitlab.com]
