from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'config.wsgi.dev.application'

SECRETS = json.load(open(os.path.join(SECRET_DIR, 'dev.json')))
