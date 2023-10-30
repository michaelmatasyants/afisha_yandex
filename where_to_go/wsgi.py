import os
from django.core.wsgi import get_wsgi_application

from whitenoise import WhiteNoise

from manage import DEBUG

if DEBUG:
    from where_to_go.settings.development import BASE_DIR
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'where_to_go.settings.development')
else:
    from where_to_go.settings.production import BASE_DIR
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'where_to_go.settings.production')
application = WhiteNoise(application=get_wsgi_application(),
                         root=os.path.join(BASE_DIR, 'static'))
