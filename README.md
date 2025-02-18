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
- [Features](#features)
- [Requirements](#requirements)
- [Como Instalar?](#como-instalar)
- [Como Usar?](#como-usar)
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

# Features

- Lidar com a autenticação da API do GitLab usando tokens de acesso pessoal.
- Buscar/Listar toda a estrutura de projetos/grupos recursivamente a partir de um grupo root do GitLab.
- Exibir a estrutura de projetos/grupos em formato de árvore (dry-run).
- Clonar o repositório de cada projeto para um diretório local.
- Desativar a criação do grupo root no diretório local quando acontecer o clone.
- Controlar a verbosidade do CLI para melhorar a experiência do usuário.
- Permitir utilizar os métodos HTTPS e SSH para clonar projetos.
- Customizar o diretório local onde os projetos serão clonados.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Requirements

- Python >= 3.8

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Como Instalar?

```bash
pip install -r requirements.txt --break-system-packages
pip install --break-system-packages .
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Como Usar?

> [!WARNING]
>
> - Certifique-se de que o seu token da API do GitLab (gitlab_token) tem as permissões necessárias para ler as informações do grupo e do projeto.
> - Ajuste o URL base do GitLab (gitlab_base_url) de acordo com a versão e a configuração da API da sua instância do GitLab.

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
