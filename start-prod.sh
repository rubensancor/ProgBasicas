#! /usr/bin/env bash

cd app

# Create admin if not created
python manage.py createsuperuser --no-input
# Set database
python manage.py migrate
python manage.py loaddata initial_data.json
# Collect statics
python manage.py collectstatic --noinput

gunicorn progbasicas.wsgi --bind 0.0.0.0:8000 --forwarded-allow-ips="*"