# adapted from https://docs.docker.com/compose/django/

FROM python:3.9.1-buster
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r --no-cache-dir requirements.txt
COPY . /code/
