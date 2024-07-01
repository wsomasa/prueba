"""
WSGI config for App_Emma project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
import os
import sys


sys.path.append('/home/obe/prueba')
sys.path.append('/home/obe/prueba/App_Emma')
#/home/obe/prueba
#if path not in sys.path:
#    sys.path.append(path)
#
os.environ['DJANGO_SETTINGS_MODULE'] = 'App_Emma.settings'
#
## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
