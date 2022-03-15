FROM python:3.10-alpine3.15
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
#RUN python -m pip install --upgrade pip
RUN pip install --upgrade pip wheel\
    && pip install -r requirements.txt
