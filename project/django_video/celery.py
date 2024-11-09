import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_video.settings")
app = Celery("django_video")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()