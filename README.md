<p align="center">
  <img alt="commitlint" src="https://res.cloudinary.com/practicaldev/image/fetch/s--0GjySa5t--/c_imagga_scale,f_auto,fl_progressive,h_720,q_auto,w_1280/https://dev-to-uploads.s3.amazonaws.com/i/r1gk3rq3o70t3zghna8w.png" width="250px" float="center"/>
</p>

<h1 align="center">Welcome to commitlint template repository</h1>

<p align="center">
  <strong>Automating the standardization of good commit messages with commitlint + husky + commitizen</strong>
</p>

<p align="center">
  <a href="https://github.com/lpmatos/commitlint">
    <img alt="Open Source" src="https://badges.frapsoft.com/os/v1/open-source.svg?v=102">
  </a>

  <a href="https://github.com/lpmatos/commitlint">
    <img alt="GitHub Language Count" src="https://img.shields.io/github/languages/count/lpmatos/commitlint">
  </a>

  <a href="https://github.com/lpmatos/commitlint">
    <img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/lpmatos/commitlint">
  </a>

  <a href="https://github.com/lpmatos/commitlint/stargazers">
    <img alt="GitHub Stars" src="https://img.shields.io/github/stars/lpmatos/commitlint?style=social">
  </a>

  <a href="https://github.com/lpmatos/commitlint/commits/master">
    <img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/lpmatos/commitlint">
  </a>

  <a href="https://github.com/lpmatos/commitlint">
    <img alt="Repository Size" src="https://img.shields.io/github/repo-size/lpmatos/commitlint">
  </a>

  <a href="https://github.com/lpmatos/commitlint/blob/master/LICENSE">
    <img alt="MIT License" src="https://img.shields.io/github/license/lpmatos/commitlint">
  </a>
</p>

### Menu

<p align="left">
  <a href="#pre-requisites">Pre-Requisites</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#description">Description</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#how-to-contribute">How to contribute</a>
</p>

### Getting Started

If you want use this repository you need to make a **git clone**:

```bash
git clone --depth 1 https://github.com/lpmatos/commitlint.git -b master
```

This will give access on your **local machine**.

### Pre-Requisites

To this project you yeed:

* NPM | Yarn (package tool)
* Install Packages
  * Husky
  * Commitlint
  * Commitizen


### How to use it?

#### Locale

1. Install package.json dependencies.
2. Git add files.
3. Run npm run commit to call commitizen, build your commit message and husky validate it. 
4. Push to remote repository.
5. Profit.

### Description

#### Create good commit messages

We all did bad commit messages. Lucky us, Conventional Commits specification exists, and with it a set of powerful tools to help us.

To enforce a standard every time we make a commit, we have husky and commitlint. Husky listen to git hooks, and we will use it to trigger the commitlint when we type a commit message.

Commitizen is a package that makes it easier to create commit messages following the previous specification.

* husky
* commitlint
* commitizen

#### Commit Lint

<strong>Requirements:</strong>

> OBS: Required .git folder in project
* .git in folder
* Node
* yarn | npm

<strong>Install by default [package.json](package.json):</strong>

```cmd
yarn install
```

<strong>Manual Installment:</strong>

```cmd
yarn init -y

yarn add @commitlint/config-conventional @commitlint/cli husky commitizen -D

echo module.exports = {extends: ['@commitlint/config-conventional']} > commitlint.config.js
```

add configuration in package.json:

```json
"husky": {
    "hooks": {
        "commit-msg": "commitlint -E HUSKY_GIT_PARAMS"
    }
},
"config": {
    "commitizen": {
        "path": "./node_modules/cz-conventional-changelog"
    }
}
```

<strong>Use:</strong>

with dependencies already installed, commits that do not follow the semmantic commit rules will be automatically blocked in the development environment

```cmd
C:\>  git add .
C:\>  git commit -m "commit"


husky > commit-msg (node v12.14.0)
⧗   input: commit
✖   subject may not be empty [subject-empty]
✖   type may not be empty [type-empty]

✖   found 2 problems, 0 warnings
ⓘ   Get help: https://github.com/conventional-changelog/commitlint/#what-is-commitlint

husky > commit-msg hook failed (add --no-verify to bypass)
```

using the commitzen, previously installed, an auxiliary service will be available to build the commits

```cmd
C:\>  git add .
C:\>  npm run commit


cz-cli@4.0.3, cz-conventional-changelog@3.2.0

? Select the type of change that you're committing: (Use arrow keys)
> feat:     A new feature
  fix:      A bug fix
  docs:     Documentation only changes
  style:    Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
  refactor: A code change that neither fixes a bug nor adds a feature
  perf:     A code change that improves performance
  test:     Adding missing tests or correcting existing tests
  build:    Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
  ci:       Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs) 
  chore:    Other changes that don't modify src or test files
  revert:   Reverts a previous commit
```

### How to contribute

>
> 1. Make a **Fork**.
> 2. Follow the project organization.
> 3. Add the file to the appropriate level folder - If the folder does not exist, create according to the standard.
> 4. Make the **Commit**.
> 5. Open a **Pull Request**.
> 6. Wait for your pull request to be accepted.. 🚀
>

Remember: There is no bad code, there are different views/versions of solving the same problem. 😊

### Add to git and push

You must send the project to your GitHub after the modifications

```bash
git add -f .
git commit -m "Added - Fixing somethings"
git push -u origin master
```

### License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

### Author

👤 **Lucca Pessoa**

Hey!! If you like this project or if you find some bugs feel free to contact me in my channels:

> * Email: luccapsm@gmail.com
> * Website: https://github.com/lpmatos
> * Github: [@lpmatos](https://github.com/lpmatos)
> * LinkedIn: [@luccapessoa](https://www.linkedin.com/in/lucca-pessoa-4abb71138/)

### Show your support

Give a ⭐️ if this project helped you!

---

<p align="center">Feito com ❤️ by <strong>Lucca Pessoa :wave:</p>