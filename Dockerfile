FROM python:3.9

ENV PTYHONBUFFERED 1

RUN mkdir /src
WORKDIR /src
COPY requirements.txt /src/
RUN pip install -r requirements.txt
COPY . /src/

