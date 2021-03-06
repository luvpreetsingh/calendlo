from .base_settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("CALENDLO_DATABASE_NAME"),
        'USER': os.getenv("CALENDLO_DATABASE_USER"),
        'PASSWORD': os.getenv("CALENDLO_DATABASE_PASSWORD"),
        'HOST': os.getenv("CALENDLO_DATABASE_HOST", "localhost"),
        'PORT': int(os.getenv("CALENDLO_DATABASE_PORT", "5432")),
    }
}

NO_OF_WEEKS_TO_SCHEDULE = int(os.getenv("CALENDLO_WEEKS_TO_SCHEDULE", 4))

SECRET_KEY = os.getenv("CALENDLO_SECRET_KEY")

DEBUG = bool(int(os.getenv("CALENDLO_DEBUG", "0")))
ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

import django_heroku
django_heroku.settings(locals())
