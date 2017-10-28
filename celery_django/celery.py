from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings # noqa

# flake8: noqa
# used for loading .env file variables if separate .env file used
# import project.settings.env


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_django.settings')

app = Celery('tasks')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
