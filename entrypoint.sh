#!/bin/sh

cd DepistClic

pwd
ls -la uploads/images
ls -la uploads/ordonnances

mkdir static
pipenv run python manage.py migrate --no-input
pipenv run python manage.py collectstatic --no-input

envsubst < /etc/nginx/sites-available/depistclic > /etc/nginx/sites-available/depistclic

ln -s /etc/nginx/sites-available/depistclic /etc/nginx/sites-enabled	
nginx -t	

pipenv run gunicorn DepistClic.wsgi:application --bind 0.0.0.0:$PORT --access-logfile -
service nginx start	
service nginx status
