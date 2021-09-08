FROM python:3.9.5

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY /requirements/production.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8000
