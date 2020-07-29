# -*- coding: utf-8 -*-

CLI = """

Examples:

Clone all repositories inside specific namespace in current directory:
gitlabrc -u $GITLAB_URL -t $GITLAB_TOKEN -n msp/charts

Clone all repositories inside specific namespace in specific directory:
gitlabrc -u $GITLAB_URL -t $GITLAB_TOKEN -n msp/charts -p /home/ubuntu

Getting repositories with specific git clone method:
gitlabrc -u $GITLAB_URL -t $GITLAB_TOKEN -n msp/charts -p /home/ubuntu -m http

Show all repositories without clone/fetch:
gitlabrc -u $GITLAB_URL -t $GITLAB_TOKEN -n msp/charts --dry-run

Show all repositories in tree representation:
gitlabrc -u $GITLAB_URL -t $GITLAB_TOKEN -n msp/charts --tree
"""
