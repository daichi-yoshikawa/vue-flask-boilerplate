FROM python:3.7.8-slim-buster

WORKDIR /root
COPY ./server/requirements.txt requirements.txt
RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

RUN apt-get update &&\
    apt-get install -y --no-install-recommends procps

EXPOSE 5000


