'''
Settings file used for staging
'''
import os
from .base import *

SECRET_KEY = "some)&mx2e#kxcji$#@%#@i1-wk#m47sd9crs4!bstnk)*8u@"

DEBUG = True
LIVE = False
STAGING = False

DEBUG_TOOLBAR = False


ALLOWED_HOSTS = []


# Setup Database
from .database_circleci import DATABASES
DATABASES = DATABASES

# This is for debug_toolbar:
# we sant to be able to activate on staging too
if DEBUG_TOOLBAR:
    INSTALLED_APPS += (
        'debug_toolbar', # for debug_toolbar
    )

    MIDDLEWARE = [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ] + MIDDLEWARE # for debug_toolbar
    # for local 127.0.0.1 works, but on spaceport, you need your ip here
    # this is  you web-browser (your outside, public IP addres) the one from your ISP
    INTERNAL_IPS = ['127.0.0.1',]

LANGUAGE_CODE = 'ro'

TIME_ZONE = 'Europe/Berlin'

MEDIA_URL = '/media/'


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

# This is only to get circleci moving
GOOGLE_RECAPTCHA_SECRET_KEY = "something"
GOOGLE_RECAPTCHA_SECRET_SERVER_KEY = "something"
MAILCHIMP_API = "something"
MAILCHIMP_LIST_ID = "something"
