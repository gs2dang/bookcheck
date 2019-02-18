from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'config.wsgi.dev.application'

SECRETS = json.load(open(os.path.join(SECRET_DIR, 'dev.json')))

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# PostgreSQL
# DATABASES = SECRETS['DATABASES']

# SQLite3
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}