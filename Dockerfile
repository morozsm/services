FROM python:3.10-alpine

COPY requirements.txt /
RUN pip install -r requirements.txt

RUN mkdir /app

COPY ./src/ /app
WORKDIR /app
EXPOSE 8888
ENTRYPOINT /app/gunicorn.sh