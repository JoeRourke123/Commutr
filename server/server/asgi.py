"""
ASGI config for server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/

----
from @Joe Rourke:
The Asynchronous Server Gateway Interface is a calling convention for web servers to forward requests to asynchronous-capable Python programming language frameworks, and applications. It is built as a successor to the Web Server Gateway Interface.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_asgi_application()
