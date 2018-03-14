FROM python:alpine3.6
MAINTAINER Dukekero

RUN apk update && apk add build-base && apk add nano
RUN apk add mariadb-dev
ENV HOME=/app
RUN apk add --no-cache openssl

ENV DOCKERIZE_VERSION v0.5.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz
RUN pip install Django gunicorn social-auth-app-django django-registration mysqlclient discord.py pymysql

ADD . $HOME
WORKDIR $HOME

EXPOSE 8000

