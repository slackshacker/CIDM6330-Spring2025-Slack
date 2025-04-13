import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cidm6330.settings')

app = Celery('cidm6330')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
