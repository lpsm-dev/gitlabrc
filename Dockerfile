FROM python:3.8-alpine3.11 as base
FROM base as install-env
COPY [ "requirements.txt", "."]
RUN pip install --upgrade pip && \
  pip install --upgrade setuptools && \
  pip install --user --no-warn-script-location -r ./requirements.txt

FROM base
RUN set -ex && apk update
RUN apk add --update --no-cache bash git
COPY --from=install-env [ "/root/.local", "/usr/local" ]
WORKDIR /usr/src/code
COPY [ ".", "." ]
RUN git config --global user.name "root" && \
  git config --global user.email "root@root.com" && \
  git config --global credential.helper cache
RUN find ./ -iname "*.py" -type f -exec chmod a+x {} \; -exec echo {} \;;
RUN python -m pip install --upgrade pip && pip install .
