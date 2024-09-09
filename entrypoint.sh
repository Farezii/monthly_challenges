#!/usr/bin/env bash

python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn 'monthly_challenges.wsgi' --bind=0.0.0.0:8089