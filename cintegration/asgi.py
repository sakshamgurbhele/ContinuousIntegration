"""
ASGI config for cintegration project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

import get_asgi_application from django.core.asgi 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cintegration.settings')

application = get_asgi_application()
