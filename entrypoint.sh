#!/bin/sh

cd DepistClic

pwd
ls -la uploads/images
ls -la uploads/ordonnances

mkdir static
pipenv run python manage.py migrate --no-input
pipenv run python manage.py collectstatic --no-input

chmod -R 755 /app/DepistClic/uploads

envsubst < /etc/nginx/sites-available/depistclic > /etc/nginx/sites-available/depistclic
cat /etc/nginx/sites-available/depistclic
cat /etc/nginx/nginx.conf

ln -s /etc/nginx/sites-available/depistclic /etc/nginx/sites-enabled
cat /etc/nginx/nginx.conf	
nginx -t
service nginx start	
service nginx status
cat /var/log/nginx/error.log

pipenv run gunicorn DepistClic.wsgi:application --bind 0.0.0.0:$PORT --access-logfile -
