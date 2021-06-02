FROM ubuntu:20.04
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev git \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

EXPOSE 8000

ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

COPY . /code/
