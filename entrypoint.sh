#!/bin/sh

cd DepistClic
mkdir static
pipenv run python manage.py migrate --no-input
pipenv run python manage.py collectstatic --no-input
pipenv run gunicorn -w 4 DepistClic.wsgi:application --bind 0.0.0.0:$PORT --access-logfile - 
