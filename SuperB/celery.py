import os
from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SuperB.settings")
app = Celery("SuperB")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


#python -m celery -A SuperB worker 
#celery -A SuperB.celery beat --scheduler django --loglevel=info 