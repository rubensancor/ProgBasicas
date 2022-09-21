#! /usr/bin/env bash

cd app

# Set database
python manage.py migrate
python manage.py loaddata initial_data.json
# Create admin if not created
python manage.py createsuperuser --no-input
# Collect statics
python manage.py collectstatic --noinput

gunicorn progbasicas.wsgi --bind 0.0.0.0:8000 --forwarded-allow-ips="*"