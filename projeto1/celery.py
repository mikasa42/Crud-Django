import os
from celery import Celery
from time import sleep

os.environ.setdefault('DJANGO_SETTINGS_MODULE','projeto1.settings')

app = Celery('projeto1')

app.autodiscover_tasks()

app.config_from_object('django.conf:settings', namespace='CELERY')

