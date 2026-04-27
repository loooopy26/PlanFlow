#!/bin/sh
sleep 10
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn --bind 0.0.0.0:8000 board_project.wsgi:application
