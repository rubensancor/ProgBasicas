#! /usr/bin/env bash

cd app
python manage.py collectstatic --noinput
gunicorn progbasicas.wsgi --bind 0.0.0.0:8000 --forwarded-allow-ips="*"