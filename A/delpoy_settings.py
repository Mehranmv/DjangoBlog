import os
from .settings import *
import dj_database_url

# export ENVIRONMENT=deploy

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}