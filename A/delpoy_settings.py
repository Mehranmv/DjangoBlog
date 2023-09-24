from .settings import *
import dj_database_url
from dotenv import load_dotenv
# ENVIRONMENT=deploy
load_dotenv()

DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}

# gettext = lambda s: s
# LANGUAGES = (
#     ('en', gettext('English')),
#     ('fa', gettext('Farsi')),
# )

# storages
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'
# # STORAGES = {
# #     "default": {
# #         "BACKEND": "storages.backends.s3.S3Storage",
# #     },
# # }
# AWS_S3_ENDPOINT_URL = os.getenv("LIARA_ENDPOINT")
# AWS_S3_ACCESS_KEY_ID = os.getenv("LIARA_ACCESS_KEY")
# AWS_S3_SECRET_ACCESS_KEY = os.getenv("LIARA_SECRET_KEY")
# AWS_STORAGE_BUCKET_NAME = os.getenv("LIARA_BUCKET_NAME")
