#!/bin/sh

gunicorn --bind 0.0.0.0:8888 -w 2 --threads 2 wsgi:app