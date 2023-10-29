import os
import sys

from environs import Env

env = Env()
env.read_env()
DEBUG = env.bool('DEBUG', default=False)


def main():
    """Run administrative tasks."""
    if DEBUG:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'where_to_go.settings.development')
    else:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'where_to_go.settings.production')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
