ARG PYTHON_VERSION=3.8-alpine3.11

FROM python:${PYTHON_VERSION} as base

FROM base as install-env
ARG GIT_PASSWORD

COPY [ "requirements.txt", "."]

RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install --user --no-warn-script-location -r ./requirements.txt

FROM base

ENV GIT_PASSWORD=$GIT_PASSWORD

RUN set -ex && apk update

RUN apk add --update --no-cache \
      bash=5.0.11-r1 \
      git=2.24.3-r0

COPY --from=install-env [ "/root/.local", "/usr/local" ]

WORKDIR /usr/src/code

COPY [ "./gitlab-clone", "." ]

RUN git config --global user.name "Lucca Pessoa" && \
    git config --global user.email "luccapsm@gmail.com" && \
    git config --global credential.helper cache

RUN find ./ -iname "*.py" -type f -exec chmod a+x {} \; -exec echo {} \;;
