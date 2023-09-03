#!/bin/bash

cd app
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8004
