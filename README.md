# Celery django

Simple implementation of celery shared task with django framework. Every step
of celery implementation (from a functional mail sending via django)
is shown in "Implement celery" commit.

### Quickstart

Before starting, make sure you have Redis server installed.

Create Python3 virtual environment:

    mkvirtualenv --python=/usr/bin/python3 celery

Get the source from GitHub:

    git clone git@github.com:HBalija/celery-django.git

Navigate to the project directory:

    cd celery-django

Instal requirements:

    pip install -r requirements.txt

Run development server:

    python manage.py runserver

Run celery (in separate environment):

    celery -A cellery_django worker -l info

Point your browser to:

    127.0.0.1:8000
