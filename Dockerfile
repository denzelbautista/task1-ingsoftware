FROM python:3-slim

ARG uid
ARG gid
ARG user
ARG group

RUN groupadd -g ${gid} ${group} || true
RUN useradd -l -u ${uid} -g ${group} -m ${user} || true

COPY requirements.txt /temp/requirements.txt
RUN pip3 install -r /temp/requirements.txt
RUN rm /temp/requirements.txt
