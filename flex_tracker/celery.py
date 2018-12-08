# flex_backend/celery.py
# to Run celery tasks, start up a worker: celery -A flex_tracker worker -B -E

from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from celery.schedules import crontab
from flex_tracker.settings import TIME_ZONE

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flex_tracker.settings')

app = Celery('flex_tracker')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.update({'worker_hijack_root_logger': False})

app.conf.timezone = TIME_ZONE

# periodic stuff
app.conf.beat_schedule = {
    'update_database_every_ten_min': {
        'task': 'flex_backend.tasks.updateFlexDatabase',
        'schedule': 600.0,
    },
    # emails and texts sent at 8pm every friday
    'send_emails': {
        'task': 'flex_backend.tasks.sendEmails',
        'schedule': crontab(hour=20, minute=0, day_of_week=6),
    },
    'send_texts': {
        'task': 'flex_backend.tasks.sendTexts',
        'schedule': crontab(hour=20, minute=0, day_of_week=6),
    },
    'spam_david_test': {
        'task': 'flex_backend.tasks.test',
        'schedule': crontab(hour=17, minute=0),
    },
}
