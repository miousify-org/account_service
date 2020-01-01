#!/bin/sh

python manage.py makemigrations store; python manage.py migrate

echo "run migrations"

python manage.py runserver 0.0.0.0:80