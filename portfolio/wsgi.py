"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
<<<<<<< HEAD
# app = application
=======
>>>>>>> 1a729ec33828544cc42c545173254032db3c72c3

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application()
<<<<<<< HEAD
app = application
=======
app = application
>>>>>>> 1a729ec33828544cc42c545173254032db3c72c3
