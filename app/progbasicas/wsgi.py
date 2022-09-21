"""
WSGI config for progbasicas project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
import os
from dotenv import load_dotenv

from whitenoise import WhiteNoise

load_dotenv()

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    os.getenv('DJANGO_SETTINGS_MODULE'))

application = get_wsgi_application()
application = WhiteNoise(application, root="/django-sites/progbasicas/static")
