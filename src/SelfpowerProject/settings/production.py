'''
Settings file used for production
'''
import os
from .base import *

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
LIVE = True
DISQUS = True
ALLOWED_HOSTS = ['selfpower.ro', 'www.selfpower.ro', 'staging.selfpower.ro']

# Setup Database
from .database_production import DATABASES
DATABASES = DATABASES

# Send exceptions to admins
ADMINS = (
    ('Razvan Ionescu', 'ionescu77@gmail.com'),
    ('Alexandru Manolescu', 'alexandru.manolescu@selfpower.ro')
)

LANGUAGE_CODE = 'ro'

TIME_ZONE = 'Europe/Berlin'

STATIC_URL = '/static/'     # static is served by apache see .conf
MEDIA_URL = '/media/'       # static is served by apache see .conf

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_dirs"),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")

# This is for the flatpages app (check if still used)
SITE_ID = 1


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'blog',
    'contact',
    'home',
    'django_markdown',
    'django.contrib.sitemaps',
    'donations',
    'testare',
    'hub',
    'login',
    'backend',
    'requests',

)

# This is for the flatpages app (check if still used)
SITE_ID = 1
# STATIC_ROOT = "/var/www/myProjects/www.selfpower.ro/static/"
SECRET_KEY = os.environ['SECRET_KEY']
GOOGLE_RECAPTCHA_SECRET_KEY = os.environ['GOOGLE_RECAPTCHA_SECRET_KEY']
GOOGLE_RECAPTCHA_SECRET_SERVER_KEY = os.environ['GOOGLE_RECAPTCHA_SECRET_SERVER_KEY']
MAILCHIMP_API = os.environ['MAILCHIMP_API']
MAILCHIMP_LIST_ID = os.environ['MAILCHIMP_LIST_ID']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
