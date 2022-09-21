#! /usr/bin/env bash

python app/manage.py createsuperuser --no-input
python app/manage.py makemigrations
python app/manage.py migrate
python app/manage.py loaddata initial_data.json
python app/manage.py collectstatic

python app/manage.py runserver 0.0.0.0:8000 --settings=progbasicas.settings.dev
