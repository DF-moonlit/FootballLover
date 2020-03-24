# <<<<<<< HEAD
"""
Django settings for FNSProject project.

Generated by 'django-admin startproject' using Django 2.1.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import json
from django.core.exceptions import ImproperlyConfigured
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'cg#p$g+j9tax!#a3cup@1$8obt2_+&k3q+pmu)5%asj6yjpkag')
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = bool( os.environ.get('DJANGO_DEBUG', True) )
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    
    'account.apps.AccountConfig',
    'match.apps.MatchConfig',
    'team.apps.TeamConfig',
    'result.apps.ResultConfig',
    'decidedMatch.apps.DecidedmatchConfig',
    'rank.apps.RankConfig',
    'notification.apps.NotificationConfig',
    'customerService.apps.CustomerserviceConfig',
    'reservation.apps.ReservationConfig',
    'match2',
    

    'rest_framework',
    'bootstrap4',
    'bootstrap_datepicker_plus',
    'storages',
]

# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'FNSProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['FNSProject/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'FNSProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

# USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
# ROOT_DIR = os.path.dirname(BASE_DIR)

CONFIG_SECRET_DIR = os.path.join(BASE_DIR, 'config_secret')
CONFIG_SETTINGS_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR, 'settings_common.json')
config_secret = json.loads(open(CONFIG_SETTINGS_COMMON_FILE).read())



DEFAULT_FILE_STORAGE = 'FNSProject.storages.MediaStorage'
STATICFILES_STORAGE = 'FNSProject.storages.StaticStorage'
MEDIAFILES_LOCATION = 'media'
STATICFILES_LOCATION = 'static'
AWS_ACCESS_KEY_ID = config_secret['aws']['access_key_id']
# AWS_ACCESS_KEY_ID = os.environ.get('access_key_id')
AWS_SECRET_ACCESS_KEY = config_secret['aws']['secret_access_key']
# AWS_SECRET_ACCESS_KEY = os.environ.get('secret_access_key')
AWS_STORAGE_BUCKET_NAME = config_secret['aws']['s3_bucket_name']
# AWS_STORAGE_BUCKET_NAME = os.environ.get('s3_bucket_name')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_DIR = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    STATIC_DIR,
]
AWS_LOCATION = 'ap-northeast-2'
STATIC_URL = 'https://%s/%s/static/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATICFILES_DIR = [
#     os.path.join(BASE_DIR, 'FNSProject', 'static'),
#     os.path.join(BASE_DIR, 'account', 'static'),
# ]# static 파일들이 현재 어디에 있는지를 쓰는 곳
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# # static 파일들이 어디로 모일 것인지를 쓰는 곳

MEDIA_URL = 'https://%s/%s/media/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Heroku: Update database configuration from $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

