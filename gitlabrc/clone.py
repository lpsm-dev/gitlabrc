# -*- coding: utf-8 -*-

import os
import sys
import re
import shutil
import time
import gitlab
import optparse
import subprocess
from .cli import Arguments
from .method import CloneMethod
from . import __version__ as VERSION

from art import *

def pname():
  return f"[gitlab-cloner - {str(os.getpid())}]"

def main():
  Art=text2art("GitLabRC")
  print(Art)

  args = Arguments(argv=None if sys.argv[1:] else ["--help"]).args

  if args.version:
    print(f"Version: {VERSION}")
    sys.exit(0) 

  perform(args)

def perform(options):

  url = options.url
  token = options.token
  namespace = options.namespace

  # TODO catch errrors
  if not url:
    sys.stderr.write("\nError: we need gitlab url information\n\n")
    exit(1)

  if not token:
    sys.stderr.write("\nError: we need gitlab token information\n\n")
    exit(1)

  if not namespace:
    sys.stderr.write("\nError: we need gitlab namespace information\n\n")
    exit(1)
  
  if not os.path.isdir(options.path):
    sys.stderr.write("\nError: destination path does not exist " + options.path + "\n\n")
    exit(1)

  git_path = shutil.which("git")
  if git_path == "None":
    sys.stderr.write("Error: git executable not installed or not in $PATH" + "\n")
    exit(2)
  else:
    print(pname() + " using " + git_path)

  t = time.time()

  gl = gitlab.Gitlab(url, token)

  group = gl.groups.get(namespace, lazy=True, include_subgroups=True)

  projects = []

  # Get all projects inside the namespace
  for project in group.projects.list(all=True):
    projects.append(project)
    print(pname() + " found " + project.path_with_namespace)

  # Get all projects inside the subgroups
  for group in gl.groups.list(all=True, owned=True, query_parameters={"id": namespace}):

    for project in group.projects.list(all=True):
      projects.append(project)
      print(pname() + " found " + project.path_with_namespace)

    subgroups = group.subgroups.list(all=True)
    while True:
      for subgroup in subgroups:

        real_group = gl.groups.get(subgroup.id, lazy=True)

        for project in real_group.projects.list(all=True):
          projects.append(project)
          print(pname() + " found " + project.path_with_namespace)

        subgroups = real_group.subgroups.list(all=True)

        if len(subgroups) == 0: next

      if len(subgroups) == 0: break

  if not options.dryrun:
    for project in projects:
      print(pname() + " clone/fetch project " + project.path_with_namespace)
      folders = [f.strip().lower() for f in project.path_with_namespace.split("/")]
      if options.noroot:
        folders.remove(namespace)

      mkdir = options.path
      for i in range(len(folders) - 1):
        mkdir = mkdir + "/" + folders[i]
        if not os.path.isdir(mkdir):
          os.mkdir(mkdir)

      clone_path = options.path + "/" + "/".join(str(x) for x in folders)
      clone_path = re.sub("/+", "/", clone_path)
      print(pname() + " folder " + clone_path)

      project_url = project.http_url_to_repo if options.method is CloneMethod.HTTP else project.ssh_url_to_repo

      if not os.path.isdir(clone_path):
        print(pname() + " cloning " + project_url)
        try:
          subprocess.run(["git", "clone", project_url, clone_path])
        except:
          sys.stderr.write("Unexpected error while cloning: terminating\n")
          exit(2)
      else:
        print(pname() + " fetching " + project_url)
        try:
          subprocess.run(["git", "-C", clone_path, "fetch", "--all"])
        except:
          sys.stderr.write("Unexpected error while fetching: terminating\n")
          exit(3)

  print(pname() + " mission accomplished in " + str(round(time.time() - t, 2)) + "s")
  exit(0)
