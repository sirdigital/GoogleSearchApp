FROM alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip \
    && pip3 install --upgrade setuptools

WORKDIR /app

COPY . /app

RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev

RUN pip3 --no-cache-dir install -r requirements.txt

ENV FLASK_ENV="docker"

EXPOSE 5000