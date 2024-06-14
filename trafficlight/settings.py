"""
Django settings for trafficlight project.

Generated by 'django-admin startproject' using Django 4.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
from .celery import app as celery_app
from celery.schedules import crontab

__all__ = ('celery_app')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s-1v_xlfcq7p-cq)(illmp0#_74s9cp_1lzs_eg(-ww@aui+h*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['159.203.82.246']

TIME_ZONE = 'Asia/Jakarta'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard',
    'task',
    'django_celery_beat',
    'django_celery_results'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'trafficlight.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'trafficlight.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'trafficlight', 
        'USER': 'postgres',
        'PASSWORD': 'efdxc123',
        'HOST': 'db', 
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# Celery settings
CELERY_BROKER_URL = 'redis://redis:6379/0'

CELERY_TIMEZONE = 'Asia/Jakarta' 

CELERY_RESULT_BACKEND = 'redis://redis:6379/0'


CELERY_BEAT_SCHEDULE = {
    'task1': {
        'task': 'task.tasks.object_detection1',
        'schedule': crontab(hour=7, minute=0),
    },
    'task2': {
        'task': 'task.tasks.object_detection2',
        'schedule': crontab(hour=7, minute=0),
    },
    'task3': {
        'task': 'task.tasks.object_detection3',
        'schedule': crontab(hour=7, minute=0),
    },
    'task4': {
        'task': 'task.tasks.object_detection4',
        'schedule': crontab(hour=12, minute=0),
    },
    'task5': {
        'task': 'task.tasks.object_detection5',
        'schedule': crontab(hour=12, minute=0),
    },
    'task6': {
        'task': 'task.tasks.object_detection6',
        'schedule': crontab(hour=12, minute=0),
    },
    'task7': {
        'task': 'task.tasks.object_detection7',
        'schedule': crontab(hour=18, minute=0),
    },
    'task8': {
        'task': 'task.tasks.object_detection8',
        'schedule': crontab(hour=18, minute=0),
    },
    'task9': {
        'task': 'task.tasks.object_detection9',
        'schedule': crontab(hour=18, minute=0),
    },
    'testing': {
        'task': 'task.tasks.testing',
        'schedule': crontab(hour=0, minute=20),
    },
}