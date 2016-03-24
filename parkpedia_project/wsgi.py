"""
WSGI config for parkpedia_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parkpedia_project.settings")

import django
django.setup()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
