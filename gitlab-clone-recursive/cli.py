import os
import sys
import re
import shutil
import time
import gitlab
import optparse
import subprocess

def pname():
  pid = os.getpid()
  return f"[gitlab-cloner - {str(pid)}]"

def main():
  parser = optparse.OptionParser("usage: %prog [options]")

  parser.add_option(
    "-u",
    "--url",
    dest="url",
    default="https://gitlab.com",
    type="string",
    help="base URL of the GitLab instance",
  )

  parser.add_option(
    "-t", "--token", dest="token", default="", type="string", help="API token"
  )

  parser.add_option(
    "-n",
    "--namespace",
    dest="namespace",
    default="",
    type="string",
    help="namespace to clone",
  )

  parser.add_option(
    "-p",
    "--path",
    dest="path",
    default=os.getenv("PWD"),
    type="string",
    help="destination path for cloned projects",
  )

  parser.add_option(
    "--disable-root",
    action="store_true",
    dest="noroot",
    default=False,
    help="do not create root namepace folder in path",
  )

  parser.add_option(
    "--dry-run",
    action="store_true",
    dest="dryrun",
    default=False,
    help="list the repositories without clone/fetch",
  )

  (options, args) = parser.parse_args()

  clone(options)

def clone(options):
  # TODO catch errrors
  if not os.path.isdir(options.path):
    sys.stderr.write("Error: destination path does not exist " + options.path + "\n")
    exit(1)

  git_path = shutil.which("git")
  if git_path == "None":
    sys.stderr.write("Error: git executable not installed or not in $PATH" + "\n")
    exit(2)
  else:
    print(pname() + " using " + git_path)

  t = time.time()

  gl = gitlab.Gitlab(options.url, options.token)

  group = gl.groups.get(options.namespace, lazy=True, include_subgroups=True)

  projects = []

  # Get all projects inside the namespace
  for project in group.projects.list(all=True):
    projects.append(project)
    print(pname() + " found " + project.path_with_namespace)

  # Get all projects inside the subgroups
  for group in gl.groups.list(
    all=True, owned=True, query_parameters={"id": options.namespace}
  ):

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
        folders.remove(options.namespace)

      mkdir = options.path
      for i in range(len(folders) - 1):
        mkdir = mkdir + "/" + folders[i]
        if not os.path.isdir(mkdir):
          os.mkdir(mkdir)

      clone_path = options.path + "/" + "/".join(str(x) for x in folders)
      clone_path = re.sub("/+", "/", clone_path)
      print(pname() + " folder " + clone_path)
      if not os.path.isdir(clone_path):
        print(pname() + " cloning " + project.http_url_to_repo)
        try:
          subprocess.run(["git", "clone", project.http_url_to_repo, clone_path])
        except:
          sys.stderr.write("Unexpected error while cloning: terminating\n")
          exit(2)
      else:
        print(pname() + " fetching " + project.http_url_to_repo)
        try:
          subprocess.run(["git", "-C", clone_path, "fetch", "--all"])
        except:
          sys.stderr.write("Unexpected error while fetching: terminating\n")
          exit(3)

  print(pname() + " mission accomplished in " + str(round(time.time() - t, 2)) + "s")
  exit(0)

if __name__ == '__main__':
  main()
