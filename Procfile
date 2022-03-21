release: python manage.py migrate

web: gunicorn main.wsgi --preload --log-file -

worker: python manage.py rqworker default