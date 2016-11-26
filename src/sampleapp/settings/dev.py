import os

from sampleapp.settings.base import *  # NOQA (ignore all errors on this line)


DEBUG = True

PAGE_CACHE_SECONDS = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite'),  # NOQA (ignore all errors on this line)
    }
}

REST_FRAMEWORK['EXCEPTION_HANDLER'] = 'django_rest_logger.handlers.rest_exception_handler'  # NOQA (ignore all errors on this line)

