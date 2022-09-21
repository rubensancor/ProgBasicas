#! /usr/bin/env bash

python app/manage.py collectstatic
gunicorn progbasicas.wsgi --bind 0.0.0.0:8000 --forwarded-allow-ips="*"