'''
Some helpful functions that can be reused.
Module created for a DRY flow in the project.
'''
# pylint: disable=invalid-name


def get_client_ip(request):
    '''
    Takes input a request and returns the IP from the quest
    '''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
