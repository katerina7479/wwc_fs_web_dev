FROM python:3.9

ENV PTYHONBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir /project
WORKDIR /project
COPY . /project/
