from .base import *

DEBUG = False

# ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# request allowed from any hosts - Danger!!!
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': '5432',
    }
}
