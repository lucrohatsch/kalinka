FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
#RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
