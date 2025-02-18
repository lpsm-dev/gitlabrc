# -*- coding: utf-8 -*-

import os
import re
import sys
import time
import signal
import shutil
from art import text2art
from git import Repo

from .log import Log
from .tree import Tree
from .process import Process
from .arguments import Arguments
from .progress import CloneProgress
from .base import GitLabBase, CloneMethod
from . import __version__ as VERSION

# ==============================================================================
# GLOBAL
# ==============================================================================

logger = Log("/var/log/gitlabrc", "file.log", "INFO", "GitLabRC").logger

# ==============================================================================
# FUNCTIONS
# ==============================================================================


def pname():
    return f"[gitlabrc - {str(os.getpid())}]"


def signal_handler(sig, frame):
    print("You pressed Ctrl+C!")
    sys.exit(0)


def check_git():
    if shutil.which("git") == "None":
        logger.error("Error: git executable not installed or not in $PATH")
        exit(1)


def get_subgroups(gl, group, root=False, info=False):
    if root:
        return gl.groups.list(all=True, owned=True, query_parameters={"id": group})
    elif info:
        return gl.groups.get(group.id, lazy=True)
    else:
        return group.subgroups.list(all=True)


def get_projects(gl, group, root=False):
    if root:
        return gl.groups.get(group, lazy=True, include_subgroups=True).projects.list(
            all=True,
        )
    else:
        return group.projects.list(all=True)


def get_all_projects(gl, namespace):
    logger.info("getting all projects")
    projects = list()
    root_projects = get_projects(gl, namespace, root=True)
    root_subgroups = get_subgroups(gl, namespace, root=True)

    if root_projects:
        for project in root_projects:
            projects.append(project)

    if root_subgroups:
        for group in root_subgroups:
            group_projects = get_projects(gl, group)
            if group_projects:
                for group_project in group_projects:
                    projects.append(group_project)
            group_subgroups = get_subgroups(gl, group)
            if group_subgroups:
                while True:
                    for group in group_subgroups:
                        relative_subgroup = get_subgroups(gl, group, info=True)
                        for project in get_projects(gl, relative_subgroup):
                            projects.append(project)
                        group_subgroups = get_subgroups(gl, relative_subgroup)
                        if len(group_subgroups) == 0:
                            continue
                    if len(group_subgroups) == 0:
                        break
    return projects


def create_directories(path, folders, namespace, noroot):
    if noroot:
        folders.remove(namespace)
    mkdir = path
    for i in range(len(folders) - 1):
        mkdir = mkdir + "/" + folders[i]
        if not os.path.isdir(mkdir):
            os.mkdir(mkdir)
    return mkdir


def clone_project(project, clone_path, project_url):
    if not os.path.isdir(clone_path):
        print(text2art("Cloning"))
        try:
            if project.empty_repo:
                logger.warning(f"Repository is empty: {project.path_with_namespace}")
                print(f"Warning: Repository is empty: {project.path_with_namespace}")
                os.makedirs(clone_path, exist_ok=True)
                Repo.init(clone_path)
                repo = Repo(clone_path)
                repo.create_remote("origin", project_url)
                repo.git.checkout("-b", "main")
                repo.index.commit("Initial commit")
                repo.remote().push(refspec="main:main")
                return
            try:
                Repo.clone_from(
                    project_url,
                    clone_path,
                    branch="main",
                    progress=CloneProgress(),
                    multi_options=["-v"],
                )
            except Exception as e_main:
                logger.warning(
                    f"Failed to clone {project.path_with_namespace} with branch 'main': {e_main}",
                )
                print(
                    f"Warning: Failed to clone {project.path_with_namespace} with branch 'main': {e_main}",
                )
                try:
                    Repo.clone_from(
                        project_url,
                        clone_path,
                        branch="master",
                        progress=CloneProgress(),
                        multi_options=["-v"],
                    )
                except Exception as e_master:
                    logger.error(
                        f"Failed to clone {project.path_with_namespace} with branch 'master': {e_master}",
                    )
                    print(
                        f"Failed to clone {project.path_with_namespace} with branch 'master': {e_master}",
                    )
        except Exception as e:
            logger.error(f"Failed to clone {project.path_with_namespace}: {e}")
            print(f"Failed to clone {project.path_with_namespace}: {e}")


def fetch_project(clone_path):
    print(text2art("Fetching"))
    Process().run_command(f"git -C {clone_path} fetch --all")


def handle_tree_option(projects, t):
    print(text2art("Tree"))
    tree = Tree()
    parse = [project.path_with_namespace for project in projects]
    parse_content = [
        [value + " " for value in elemento.split("/")] for elemento in parse
    ]
    tree.show(tree.make(parse_content))
    logger.info(f"mission accomplished in {str(round(time.time() - t, 2))} s")
    exit(0)


def main():
    print(text2art("GitLabRC"))
    check_git()
    args = Arguments(argv=None if sys.argv[1:] else ["--help"]).args
    if args.version:
        print(f"Version: {VERSION}")
        exit(1)
    if args.signal:
        signal.signal(signal.SIGINT, signal_handler)
    print(f"Version: {VERSION}\n")
    run(args)


def run(options):
    url, token, namespace, path = (
        options.url,
        options.token,
        options.namespace,
        options.path,
    )
    gl, t = GitLabBase(url, token).client, time.time()

    if path:
        if not os.path.isdir(path):
            logger.error(f"error: destination path does not exist {options.path}")
            exit(1)

    if not namespace:
        logger.error("error: we need a namespace")
        exit(1)

    projects = get_all_projects(gl, namespace)

    if options.tree:
        handle_tree_option(projects, t)

    print(text2art("Projects"))
    for project in projects:
        print(f"{pname()} found {project.path_with_namespace}")

    if not options.dryrun:
        for index, project in enumerate(projects, start=1):
            print(f"{pname()} clone/fetch project {project.path_with_namespace}")
            folders = [
                f.strip().lower() for f in project.path_with_namespace.split("/")
            ]

            create_directories(path, folders, namespace, options.noroot)

            clone_path = path + "/" + "/".join(str(x) for x in folders)
            clone_path = re.sub("/+", "/", clone_path)

            print(f"{pname()} folder {clone_path}")

            project_url = (
                project.http_url_to_repo
                if options.method is CloneMethod.HTTP
                else project.ssh_url_to_repo
            )
            project_url = project_url.replace("https://", f"https://{token}@")

            clone_project(project, clone_path, project_url)
            fetch_project(clone_path)

    logger.info(f"mission accomplished in {str(round(time.time() - t, 2))} s")
    exit(0)
