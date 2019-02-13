from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

SECRETS = json.load(open(os.path.join(SECRET_DIR, 'prod.json')))