# -*- coding: utf-8 -*-

import os
from . import constants
from typing import NoReturn, Text
from argparse import ArgumentParser, RawTextHelpFormatter

class Arguments:

  def __init__(self, argv=None) -> NoReturn:
    self._parser = self._create_parser_object()
    self._adding_arguments()
    self.args = self._parser.parse_args(argv)
    args_print = vars(self.args ).copy()
    args_print["token"] = "xxxxx"
    print("running with args [%s]", args_print)

  def _create_parser_object(self) -> ArgumentParser:
    return ArgumentParser(
      description="Gitlabrc - clones all projects inside namespaces",
      prog="gitlabcr",
      epilog=constants.CLI,
      formatter_class=RawTextHelpFormatter)

  def _adding_arguments(self) -> NoReturn:
    self._parser.add_argument("-u", "--url",
                                type=str,
                                dest="url",
                                default="https://gitlab.com",
                                metavar="<url>",
                                help="base URL of GitLab instance")
    self._parser.add_argument("-t", "--token",
                                type=str,
                                dest="token",
                                default=os.environ.get("GITLAB_TOKEN"),
                                metavar="<token>",
                                help="token GitLab API")
    self._parser.add_argument("-n", "--namespace",
                                type=str,
                                dest="namespace",
                                default="",
                                metavar="<namespace>",
                                help="namespace in GitLab to clone all projects")
    self._parser.add_argument("-p", "--path",
                                type="string",
                                dest="path",
                                default=os.getenv("PWD"),
                                metavar="<path>",
                                help="destination path for cloned projects")
    self._parser.add_argument("--disable-root",
                                action="store_true",
                                dest="noroot",
                                default=False,
                                help="do not create root namepace folder in path")
    self._parser.add_argument("--version",
                                action="store_true",
                                help="show version")
