from .base_settings import * # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv("CALENDLO_DATABASE_NAME", "NAME"),
        'USER': os.getenv("CALENDLO_DATABASE_USER", "USER"),
        'PASSWORD': os.getenv("CALENDLO_DATABASE_PASSWORD", "PASSWORD"),
        'HOST': os.getenv("CALENDLO_DATABASE_HOST", "HOST"),
        'PORT': os.getenv("CALENDLO_DATABASE_PORT", "PORT"),
    }
}
