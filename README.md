**GitLabRC** (GitLab Recursive Clone)

This Python CLI is a very simple tool that help you to clone all projects inside a [gitlab](http://www.gitlab.com) group.

This project is inspired from [gitup](https://github.com/ezbz/gitlabber) and has parts taken from there.

### Usage

  usage: gitlabcr [-h] [-u <url>] [-t <token>] [-n <namespace>] [-p <path>] [--disable-root] [--version]

  Gitlabrc - clones all projects inside namespaces

  optional arguments:
    -h, --help            show this help message and exit
    -u <url>, --url <url>
                          base URL of GitLab instance
    -t <token>, --token <token>
                          token GitLab API
    -n <namespace>, --namespace <namespace>
                          namespace in GitLab to clone all projects
    -p <path>, --path <path>
                          destination path for cloned projects
    --disable-root        do not create root namepace folder in path
    --version             show version

### Exemples

* Clone all repositories inside specific namespace in current directory:

    gitlabrc -u $GITLAB_URL -t $GITLAB_TOKEN -n msp/charts

* Clone all repositories inside specific namespace in specific directory:

    gitlabrc -u $GITLAB_URL -t $GITLAB_TOKEN -n msp/charts -p /home/ubuntu

* Getting repositories with specific git clone method:

    gitlabrc -u $GITLAB_URL -t $GITLAB_TOKEN -n msp/charts -p /home/ubuntu -m http

* Show all repositories without clone/fetch:

    gitlabrc -u $GITLAB_URL -t $GITLAB_TOKEN -n msp/charts --dry-run
