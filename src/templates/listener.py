
#!/usr/bin/python

'''This module processes PayPal Instant Payment Notification messages (IPNs).'''

from __future__ import print_function
from django.http import HttpResponseRedirect

import sys
import urllib.parse
import requests
import logging



VERIFY_URL_PROD = 'https://ipnpb.paypal.com/cgi-bin/webscr'
VERIFY_URL_TEST = 'https://ipnpb.sandbox.paypal.com/cgi-bin/webscr'

# Switch as appropriate 
VERIFY_URL = VERIFY_URL_TEST

# CGI preamble
print ('content-type: text/plain')
print ()

# Read and parse query string
param_str = sys.stdin.readline().strip()
params = urllib.parse.parse_qsl(param_str)

# Add '_notify-validate' parameter
params.append(('cmd', '_notify-validate'))

# Post back to PayPal for validation

headers = {'content-type': 'application/x-www-form-urlencoded',
           'user-agent': 'Python-IPN-Verification-Script'}
r = requests.post(VERIFY_URL, params=params, headers=headers, verify=True)
r.raise_for_status()

# Check return message and take action as needed
if r.text == 'VERIFIED':
    print('\n IPN received. CFinder: 39fgg2h92h0 \n', file=sys.stderr)
    print('\n r.receiver_email \n', file=sys.stdout))
    #logging.basicConfig(level=logging.DEBUG)
    okragon = r.receiver_email





elif r.text == 'INVALID':
    pass
else:
    pass



