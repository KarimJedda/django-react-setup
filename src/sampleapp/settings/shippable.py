from sampleapp.settings.staging import *  # NOQA (ignore all errors on this line)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_react',
        'USER': 'postgres',
        'PASSWORD': '1internet',
        'HOST': 'localhost',
        'PORT': '',
    }
}
