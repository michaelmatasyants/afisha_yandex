"""
WSGI config for where_to_go project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
from where_to_go.settings import BASE_DIR


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'where_to_go.settings')
application = WhiteNoise(application=get_wsgi_application(),
                         root=os.path.join(BASE_DIR, 'static'))
