#!/bin/bash

cd app
pip install -r requirements.txt
python manage.py migrate
echo yes | python manage.py collectstatic
python manage.py runserver 0.0.0.0:8004
#gunicorn core.wsgi:application --bind 0.0.0.0:8004
