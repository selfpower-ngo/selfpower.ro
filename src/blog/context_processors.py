'''
A context processor for the disqus  feature (comments section)
'''
from django.conf import settings


def disqus(context):
    '''
    return settings.DISQUS
    '''
    return {'DISQUS': settings.DISQUS}
