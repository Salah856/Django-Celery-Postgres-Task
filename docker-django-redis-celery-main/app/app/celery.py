import os
from celery import Celery
from celery.schedules import crontab
from app.core.views import getPrices


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # run every hour (60 minutes) to fetch prices from alpha vantage api
    sender.add_periodic_task(
        crontab(minute='*/60'),
        test.s(),
    )


@app.task
def test():
    getPrices()
