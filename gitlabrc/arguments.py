# -*- coding: utf-8 -*-

from .constants import CLI
from .settings import Config
from .method import CloneMethod
from typing import NoReturn, Text, Optional, Type, Dict
from argparse import ArgumentParser, RawTextHelpFormatter

class Arguments:

  def __init__(self, argv: Optional[Type[Dict]] = None) -> NoReturn:
    self._config = Config()
    self._parser = self._create_parser_object()
    self._adding_arguments()
    self.args = self._parser.parse_args(argv)

  def _create_parser_object(self) -> ArgumentParser:
    return ArgumentParser(
      description="GitlabRC is a CLI that help you clone projects inside a specific group (namespace) in Gitlab",
      prog="gitlabrc",
      epilog=CLI,
      formatter_class=RawTextHelpFormatter)

  def _adding_arguments(self) -> NoReturn:
    self._parser.add_argument("-u", "--url",
      type = str,
      dest = "url",
      default = self._config.get_env("GITLAB_URL"),
      metavar = "<url>",
      help = "base URL of GitLab instance")
    self._parser.add_argument("-t", "--token",
      type = str,
      dest = "token",
      default = self._config.get_env("GITLAB_TOKEN"),
      metavar = "<token>",
      help = "token GitLab API")
    self._parser.add_argument("-n", "--namespace",
      type = str,
      dest = "namespace",
      default = "",
      metavar = "<namespace>",
      help = "namespace that represent a GitLab group used to clone/fetch all projects")
    self._parser.add_argument("-p", "--path",
      dest = "path",
      default = self._config.get_env("PWD"),
      metavar = "<path>",
      help = "destination path into your system to clone/fetch all projects")
    self._parser.add_argument("-m", "--method",
      type = CloneMethod.parse,
      dest = "method",
      default = self._config.get_env("GITLAB_CLONE_METHOD", "http"),
      metavar = "<method>",
      choices = list(CloneMethod),
      help = "method used in GitLabRC to cloning repositories (either <http> or <ssh>)")
    self._parser.add_argument("--disable-root",
      action ="store_true",
      dest = "noroot",
      default = False,
      help = "don't create root namespace folder in path")
    self._parser.add_argument("--dry-run",
      action = "store_true",
      dest = "dryrun",
      default = False,
      help = "list all repositories without clone/fetch")
    self._parser.add_argument("--tree",
      action = "store_true",
      dest = "tree",
      default = False,
      help = "list all repositories in a tree representation without clone/fetch")
    self._parser.add_argument("--version",
      action = "store_true",
      help = "show version")
