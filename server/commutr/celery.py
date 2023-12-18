"""
Celery config file

This is the config for Celery, the library which offloads our intensive business tasks and runs
asynchronously in the background.
"""

import os
from celery import Celery

# Show the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
app = Celery("commutr")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks() # Do not delete this or the Celery jobs will not be loaded
