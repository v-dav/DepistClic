#!/bin/sh

cd DepistClic
pipenv run python manage.py migrate --no-input
pipenv run python manage.py collectstatic --no-input
service nginx start
service nginx status
pipenv run gunicorn DepistClic.wsgi:application --bind 0.0.0.0:$PORT
