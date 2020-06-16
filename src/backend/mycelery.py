'''
A Celery module that controls the overall activity of Celery
'''
from __future__ import absolute_import
import os
from django.conf import settings
from celery import Celery

# set the default Django settings module for the 'celery' program.
### Razvansky: this is error prone, you are setting and ENV variable from an application
# why 20190415
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SelfpowerProject.settings')
APP = Celery('SelfpowerProject')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
APP.config_from_object('django.conf:settings')
APP.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@APP.task(bind=True)
def debug_task(self):
    '''
    debug_task(self)
    '''
    print('Request: {0!r}'.format(self.request))
