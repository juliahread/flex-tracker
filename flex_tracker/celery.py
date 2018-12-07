# flex_backend/celery.py

import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flex_tracker.settings')

app = Celery('flex_tracker')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# periodic stuff
app.conf.beat_schedule = {
    'update_database_every_ten_min': {
        'task': 'flex_backend.tasks.updateFlexDatabase',
        'schedule': 600,
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
        'schedule': crontab(),
    },
}
