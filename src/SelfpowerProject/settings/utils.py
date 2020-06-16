'''
Helpful functions used in the entire project
'''
import hashlib

from django.conf import settings
from django.contrib.staticfiles.finders import find
from django.templatetags.static import static


def prepare_you_tube_url(prime_url):
    '''
    Convert one youtube format to another
    '''
    refined_url = prime_url.replace(
                'https://youtu.be/',
                'https://www.youtube.com/watch?v='
                )
    return refined_url


def convert_text_to_md5(its_input):
    '''
    Convert text to MD5 format
        so that it can be prepared for processing
    '''
    md5_version = hashlib.md5()
    md5_version.update(its_input.encode('utf-8'))
    result = md5_version.hexdigest()
    return result


def get_static(path):
    """
    Get the path of static files
    """
    if settings.DEBUG:
        return find(path)
    else:
        return static(path)
