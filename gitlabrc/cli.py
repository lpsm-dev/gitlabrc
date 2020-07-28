# -*- coding: utf-8 -*-

import os
import sys
import re
import shutil
import time
import gitlab
import optparse
from art import *
import subprocess
from .arguments import Arguments
from .method import CloneMethod
from .process import Process
from . import __version__ as VERSION

from anytree import Node, RenderTree
from anytree.exporter import DictExporter, JsonExporter
from anytree.importer import DictImporter

def pname():
  return f"[gitlabrc - {str(os.getpid())}]"

def make_node(name, parent, url):
  node = Node(name=name, parent=parent, url=url)
  node.root_path = "/".join([str(n.name) for n in node.path])
  return node

def add_projects(parent, projects):
  for project in projects:
    node = make_node(project.name, parent, url=project.http_url_to_repo)

def get_projects(group, parent):
  projects = group.projects.list(as_list=False)
  add_projects(parent, projects)

def get_subgroups(group, parent, gitlab):
  subgroups = group.subgroups.list(as_list=False)
  for subgroup_def in subgroups:
    subgroup = gitlab.groups.get(subgroup_def.id)
    node = make_node(subgroup.name, parent, url=subgroup.web_url)
    get_subgroups(subgroup, node, gitlab)
    get_projects(subgroup, node)

def load_gitlab_tree(gitlab, root):
  groups = gitlab.groups.list(as_list=False)
  for group in groups:
    if group.parent_id is None:
      node = make_node(group.name, root, url=group.web_url)
      get_subgroups(group, node, gitlab)
      get_projects(group, node)

def print_tree_native(root, url):
  for pre, _, node in RenderTree(root):
    line = ""
    if node.is_root:
      line = "%s%s [%s]" % (pre, "root", url)
    else:
      line = "%s%s [%s]" % (pre, node.name, node.root_path)
    print(line)

def main():
  Art=text2art("GitLabRC")
  print(Art)
  args = Arguments(argv=None if sys.argv[1:] else ["--help"]).args
  if args.version:
    print(f"Version: {VERSION}")
    sys.exit(0) 
  perform(args)

def perform(options):
  url, token, namespace = options.url, options.token, options.namespace

  root = Node("", root_path="", url=url)

  gl = gitlab.Gitlab(url, token)

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

  if options.dryrun:
    load_gitlab_tree(gl, root)
    print_tree_native(root, url)

  git_path = shutil.which("git")
  if git_path == "None":
    sys.stderr.write("Error: git executable not installed or not in $PATH" + "\n")
    exit(2)
  else:
    print(pname() + " using " + git_path)

  t = time.time()

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
  print([project.path_with_namespace for project in projects])
  
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
        print(f"{pname()} cloning {project_url}")
        Process().run_command(f"git clone {project_url} {clone_path}")
      else:
        print(f"{pname()} fetching {project_url}")
        Process().run_command(f"git -C {clone_path} fetch --all")

  print(pname() + " mission accomplished in " + str(round(time.time() - t, 2)) + "s")
  exit(0)
