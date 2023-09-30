from pathlib import Path
import locale
import os
import dj_database_url
import psycopg2
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-uowdv@byvk7fyacx5f+x*8@940$m0awt6v%9$mdpv^#t^&bp4u'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # django admin interface
    'admin_interface',
    'colorfield',
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    # Third-party apps
    'star_ratings',
    'mptt',
    'ckeditor',
    'ckeditor_uploader',
    'django_jalali',
    'jdatetime',
    'fontawesomefree',
    'jalali_date',
    'mathfilters',
    # 'modeltranslation',
    # local apps
    'posts.apps.PostsConfig',
    'home.apps.HomeConfig',
    'accounts.apps.AccountsConfig',
    'pages.apps.PagesConfig'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'A.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # apps processors
                'home.context_processors.global_context',
                # django processors
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'A.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'blog',
        'USER': 'mehran',
        'PASSWORD': 'mehran',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
DJANGO_SETTINGS_MODULE = 'A.settings'

LANGUAGE_CODE = 'fa'

LANGUAGES = (
    ('fa', _('Farsi')),
    ('en', _('English')),
)

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale/'),)

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Ckeditor
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_ALLOW_NONIMAGE_FILES = True
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'extraPlugins': ','.join(
            [
                'html5video',
            ]),
    },
}

SITE_ID = 1

# settings
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'local')
if ENVIRONMENT == 'local':
    # from .local_settings import *
    pass
elif ENVIRONMENT == 'deploy':
    from .delpoy_settings import *
else:
    raise ValueError('Invalid environment value.')

# admin interface
X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

# rating
STAR_RATINGS_STAR_HEIGHT = 24
STAR_RATINGS_STAR_WIDTH = 24
template_name = "star_ratings/widget.html"

# zarinpal
MERCHANT = "00000000-0000-0000-0000-000000000000"
SANDBOX = True
