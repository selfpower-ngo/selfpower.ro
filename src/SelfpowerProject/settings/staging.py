'''
Settings file used for staging
'''
import os
from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True
LIVE = False
STAGING = True
DEBUG_TOOLBAR = True


ALLOWED_HOSTS = [
        '.avproiect.com',
        '.selfpower.ro',
    ]


# Setup Database
from .database_staging import DATABASES
DATABASES = DATABASES

# Send exceptions to admins
ADMINS = (
    ('Razvan Ionescu', 'ionescu77@gmail.com'),
    ('Alexandru Manolescu', 'alexandru.manolescu@selfpower.ro')
)

# This is for debug_toolbar:
# we sant to be able to activate on staging too (make sure we not LIVE)
if DEBUG_TOOLBAR and STAGING and not LIVE:
    INSTALLED_APPS += (
        'debug_toolbar', # for debug_toolbar
    )

    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ] + MIDDLEWARE # for debug_toolbar
    # for local 127.0.0.1 works, but on spaceport, you need your ip in INTERNAL_IPS
    # this is  you web-browser (your outside, public IP addres) the one from your ISP
    # INTERNAL_IPS = ['127.0.0.1','192.168.1.9','95.91.223.88',]
    INTERNAL_IPS = os.environ['INTERNAL_IPS']

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

# This is for the flatpages app and django sitemap framework
SITE_ID = 1


SECRET_KEY = os.environ['SECRET_KEY']
GOOGLE_RECAPTCHA_SECRET_KEY = os.environ['GOOGLE_RECAPTCHA_SECRET_KEY']
GOOGLE_RECAPTCHA_SECRET_SERVER_KEY = os.environ['GOOGLE_RECAPTCHA_SECRET_SERVER_KEY']
MAILCHIMP_API = os.environ['MAILCHIMP_API']
MAILCHIMP_LIST_ID = os.environ['MAILCHIMP_LIST_ID']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
