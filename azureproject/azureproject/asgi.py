"""
ASGI config for azureproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Check for the WEBSITE_HOSTNAME environment variable to see if we are running in Azure App Service
# If so, then load the settings from production.py

settings_module = 'azureproject.production' if 'WEBSITE_HOSTNAME' in os.environ else 'azureproject.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_asgi_application()
