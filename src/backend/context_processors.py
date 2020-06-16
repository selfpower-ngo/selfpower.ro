'''
A module for context processors in the  project
'''
from django.conf import settings
from .models import SiteConfig

def live(request):
    '''
    Return True if LIVE or False otherwise
    '''
    return {
        'LIVE': settings.LIVE
    }

def config(request):
	return {'config':SiteConfig.load()}
