import os

from django.core.asgi import get_asgi_application
from manage import DEBUG


if DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'where_to_go.settings.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'where_to_go.settings.production')

application = get_asgi_application()
