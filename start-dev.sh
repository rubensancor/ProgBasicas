#! /usr/bin/env bash

python manage.py createsuperuser --no-input
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata initial_data.json

python manage.py runserver 0.0.0.0:8000 --settings=progbasicas.settings.dev
