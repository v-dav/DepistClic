#!/bin/sh

cd DepistClic
ls -la uploads/images
ls -la upload/ordonnances
mkdir static
pipenv run python manage.py migrate --no-input
pipenv run python manage.py collectstatic --no-input
pipenv run gunicorn DepistClic.wsgi:application --bind 0.0.0.0:$PORT --access-logfile -
