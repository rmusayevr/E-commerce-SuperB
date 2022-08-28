import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SuperB.settings")
app = Celery("SuperB")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

#python -m celery -A SuperB worker 