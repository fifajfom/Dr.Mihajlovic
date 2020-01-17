#/bin/bash

sleep 10

cd /var/django_p/OM/


gunicorn --daemon --workers 1 --bind unix:/var/django_p/OM/OM.sock OM.wsgi
