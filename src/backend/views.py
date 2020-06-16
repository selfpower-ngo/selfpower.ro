'''
Module containing server listeners, error handling views, and SMTP clients
'''
from __future__ import print_function
import sys
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from paypal.standard.ipn.signals import valid_ipn_received
# pylint: disable=W0612,W0613
# for functions accepting kwargs

@csrf_exempt
def ipn(sender, **kwargs):
    '''
    Paypal IPN listener. It gets triggered after every each payment.
    '''
    msg = sender.POST.get('payer_email')

    print(msg)

    # CGI preamble
    print('content-type: text/plain')

    sys.stdin = sender

    return HttpResponse(msg)

valid_ipn_received.connect(ipn)


def send_email(request):
    '''
    Prototype of call to send_email() function
    '''
    email = 'alex.inntekt@gmail.com'
    send_mail('heyy', 'message', email, [email], fail_silently=False)


def error_404(request, *args, **kwargs):
    '''
    A 404 error handling view
    '''
    data = {}
    return render(request, '404.html', data)

def error_500(request, *args, **kwargs):
    '''
    A 500 error handling view
    '''
    data = {}
    return render(request, '500.html', data)
