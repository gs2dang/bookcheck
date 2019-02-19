import requests
import sentry_sdk
from .base import *
from sentry_sdk.integrations.django import DjangoIntegration

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SECRETS = json.load(open(os.path.join(SECRET_DIR, 'prod.json')))

ALLOWED_HOSTS = SECRETS['ALLOWED_HOSTS']

WSGI_APPLICATION = 'config.wsgi.prod.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = SECRETS['DATABASES']


# AWS
AWS_ACCESS_KEY_ID = SECRETS['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = SECRETS['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = SECRETS['AWS_STORAGE_BUCKET_NAME']
AWS_DEFAULT_ACL = None
AWS_S3_REGION_NAME = 'ap-northeast-2'

# S3 Storage
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Health Check
try:
    EC2_IP = requests.get('http://169.254.169.254/latest/meta-data/local-ipv4').text
    ALLOWED_HOSTS.append(EC2_IP)
except requests.exceptions.RequestException:
    pass

# Sentry
sentry_sdk.init(
    dsn=SECRETS['SENTRY_DSN'],
    integrations=[DjangoIntegration()]
)