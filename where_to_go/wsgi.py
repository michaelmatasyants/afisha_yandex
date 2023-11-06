import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

from where_to_go.settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'where_to_go.settings')
application = WhiteNoise(application=get_wsgi_application(),
                         root=os.path.join(BASE_DIR, 'static'))
