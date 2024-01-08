"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from server.tasks import setup_rss_job

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

# App Startup Code
setup_rss_job()

from django.apps import apps

for app in apps.get_app_configs():
    print(app)

application = get_wsgi_application()


