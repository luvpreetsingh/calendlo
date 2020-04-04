from .base_settings import * # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("CALENDLO_DATABASE_NAME", "NAME"),
        'USER': os.getenv("CALENDLO_DATABASE_USER", "USER"),
        'PASSWORD': os.getenv("CALENDLO_DATABASE_PASSWORD", "PASSWORD"),
        'HOST': os.getenv("CALENDLO_DATABASE_HOST", "HOST"),
        'PORT': int(os.getenv("CALENDLO_DATABASE_PORT", "PORT")),
    }
}

NO_OF_WEEKS_TO_SCHEDULE = int(os.getenv("CALENDLO_WEEKS_TO_SCHEDULE", 4))
