import os

from sampleapp.settings.base import *  # NOQA (ignore all errors on this line)


DEBUG = False
TEMPLATE_DEBUG = DEBUG

PAGE_CACHE_SECONDS = 60

# TODO: n a real production server this should have a proper url
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite'),  # NOQA (ignore all errors on this line)
    }
}

REST_FRAMEWORK['EXCEPTION_HANDLER'] = 'django_rest_logger.handlers.rest_exception_handler'  # NOQA (ignore all errors on this line)

# ########### Sentry configuration

# Change this to proper sentry url.
RAVEN_CONFIG = {
    'dsn': '',
}

INSTALLED_APPS = INSTALLED_APPS + (  # NOQA (ignore all errors on this line)
    'raven.contrib.django.raven_compat',
)

# ####### Logging