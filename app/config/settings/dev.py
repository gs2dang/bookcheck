from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

WSGI_APPLICATION = 'config.wsgi.dev.application'

SECRETS = json.load(open(os.path.join(SECRET_DIR, 'dev.json')))

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = SECRETS['DATABASES']

# AWS
AWS_ACCESS_KEY_ID = SECRETS['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = SECRETS['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = SECRETS['AWS_STORAGE_BUCKET_NAME']
AWS_S3_REGION_NAME = 'ap-northeast-2'

# S3 Storage
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'