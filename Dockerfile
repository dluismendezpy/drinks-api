FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /drinks
COPY requirements.txt /drinks/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /drinks/
