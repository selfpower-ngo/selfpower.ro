'''
Configurations for the database used in production
'''
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DATABASE_NAME'],
        'USER': os.environ['DATABASE_USER'],
        'PASSWORD': os.environ['PRODUCTION_DATABASE_PASSWORD'],
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
