# Author: K. Dushyant Reddy
# StudID: STU614f75ed0b64d1632597485
# Social: https://www.linkedin.com/in/kdushyantreddy, https://github.com/Dushyant029 

"""
WSGI config for duchatapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'duchatapp.settings')

application = get_wsgi_application()
