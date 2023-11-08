#!/bin/sh

ls -la
cd uploads
ls -la
cd ..
cd DepistClic
ls -la
mkdir static
pipenv run python manage.py migrate --no-input
pipenv run python manage.py collectstatic --no-input
pipenv run gunicorn DepistClic.wsgi:application --bind 0.0.0.0:$PORT --access-logfile -
