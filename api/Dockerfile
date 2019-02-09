FROM python:3.7.2-alpine3.9

ENV PYTHONPATH /code

RUN apk update && \
    apk upgrade && \
    apk add bash && \
    apk add asciidoctor && \
    apk add ruby-rdoc && \
    gem install concurrent-ruby && \
    gem install tilt


COPY requirements.txt /code/api/requirements.txt
RUN pip3.7 install -U pip && \
    pip3.7 install -r /code/api/requirements.txt

COPY . /code/api

