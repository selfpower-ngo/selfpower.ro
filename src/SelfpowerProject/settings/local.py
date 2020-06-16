'''
Settings file for locat developement and testing
'''
import os
from .base import *

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = True
DEBUG_TOOLBAR = True
STAGING = False

ALLOWED_HOSTS = ['127.0.0.1']

# This is for debug_toolbar:
# we sant to be able to activate on staging too
if DEBUG_TOOLBAR:
    INSTALLED_APPS += (
        'debug_toolbar',  # for debug_toolbar
    )

    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ] + MIDDLEWARE  # for debug_toolbar

    INTERNAL_IPS = ['127.0.0.1']  # for debug_toolbar

# Moved here from base.py, because they would nod read DEBUG in time
# on STAGING & LIVE static root and media root are served by apache
if DEBUG:
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")
    print("Debug is TRUE and :",
            "\nSTATIC_ROOT: ", STATIC_ROOT,
            "\nMEDIA_ROOT: ", MEDIA_ROOT)

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static_dirs"),
    )

# For local.py this variables will need to be set in bin/activate
#

GOOGLE_RECAPTCHA_SECRET_KEY = os.environ['GOOGLE_RECAPTCHA_SECRET_KEY']
GOOGLE_RECAPTCHA_SECRET_SERVER_KEY = os.environ['GOOGLE_RECAPTCHA_SECRET_SERVER_KEY']
MAILCHIMP_API = os.environ['MAILCHIMP_API']
MAILCHIMP_LIST_ID = os.environ['MAILCHIMP_LIST_ID']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
