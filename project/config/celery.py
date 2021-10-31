import os
from celery import Celery

path = os.getenv('DJANGO_SETTINGS_MODULE')

os.environ.setdefault('DJANGO_SETTINGS_MODULE',str(path))

app = Celery('config')

app.config_from_object('django.conf:settings',namespace='CELERY')

app.autodiscover_tasks()