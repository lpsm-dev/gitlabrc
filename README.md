<!-- BEGIN_DOCS -->
<div align="center">

<a name="readme-top"></a>

Hello Human 👽! Bem-vindo ao meu repositório 👋

<img alt="terraform" src="https://natanfelles.github.io/assets/img_posts/gitlab.png" width="250px" float="center"/>

Recursive clone all projects into a namespace (group) in GitLab Server

[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Semantic Release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://semantic-release.gitbook.io/semantic-release/usage/configuration)
[![Built with Devbox](https://jetpack.io/img/devbox/shield_galaxy.svg)](https://jetpack.io/devbox/docs/contributor-quickstart/)

</div>

# Sumário

<details>
  <summary><strong>Expandir</strong></summary>

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Visão Geral](#vis%C3%A3o-geral)
  - [Objetivo](#objetivo)
  - [Contexto e Motivação](#contexto-e-motiva%C3%A7%C3%A3o)
- [Instalação](#instala%C3%A7%C3%A3o)
- [Contribuição](#contribui%C3%A7%C3%A3o)
- [Versionamento](#versionamento)
- [Troubleshooting](#troubleshooting)
- [Show your support](#show-your-support)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

</details>

# Visão Geral

## Objetivo

Nesse repositório, apresento para vocês um CLI que facilita o clone de projetos do GitLab de forma recursiva.

## Contexto e Motivação

No dia a dia, muitas vezes precisamos clonar projetos do GitLab para nossa máquina local. Isso pode ser um processo tedioso e repetitivo, especialmente quando precisamos clonar vários projetos em diferentes grupos. Para facilitar esse processo, desenvolvi um CLI que permite clonar projetos do GitLab de forma recursiva.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Instalação

```bash
pip install -r requirements.txt --break-system-packages
pip install --break-system-packages .
```

# Requisitos

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Usage

> [!WARNING]
>
> - Make sure your GitLab API token (gitlab_token) has the necessary permissions to read group and project information.
> - Adjust the GitLab base URL (gitlab_base_url) according to your GitLab instance's API version and configuration.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Features

- Handle GitLab API authentication using a personal access token.
- Recursively fetch projects from a specified GitLab group, including subgroups.
- Clone each project's repository to a local directory.
- Dry-run and list all recursively fetch projects/groups structure.
- List all projects/groups structure in a tree representation.
- Disable creation of root group in the local machine.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Contribuição

Gostaria de contribuir? Isso é ótimo! Temos um guia de contribuição para te ajudar. Clique [aqui](CONTRIBUTING.md) para lê-lo.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Versionamento

Para verificar o histórico de mudanças, acesse o arquivo [**CHANGELOG.md**](CHANGELOG.md).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Troubleshooting

Se você tiver algum problema, abra uma [issue](https://github.com/lpsm-dev/gitlabrc/issues/new/choose) nesse projeto.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Show your support

<div align="center">

Dê uma ⭐️ para este projeto se ele te ajudou!

<img src="https://github.com/lpsm-dev/lpsm-dev/blob/0062b174ec9877e6dfc78817f314b4a0690f63ff/.github/assets/yoda.gif" width="225"/>

<br>
<br>

Feito com 💜 pelo **Time de DevOps** :wave: inspirado no [readme-md-generator](https://github.com/kefranabg/readme-md-generator)

</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>
<!-- END_DOCS -->
