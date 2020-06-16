'''
donations/views

'''
import os
import sys

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings

from SelfpowerProject.settings.utils import get_static

def doilasuta(request):
    '''
    Simple web view
    '''
    return render(request, 'doilasuta.html')


def donatii(request):
    '''
    Web page inviting navigators to make donations.
    Contains link to Paypal processor
    '''
    return render(request, 'donatii.html')


def pdf_view(request):
    '''
    Returns a pdf, the form with the redirecting of 2% out of salary

    Use this for debugging, to find out what is your MEDIA_ROOT path:
        print(settings.MEDIA_ROOT)    #use this for debugging
    '''

    pathToPDF = get_static('documents/Formular_donatie.pdf')
    print(pathToPDF)
    if pathToPDF:
        with open(pathToPDF, 'rb') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=some_file.pdf'
            return response
        pdf.closed
    else:
        raise Http404
        #return HttpResponseNotFound("PDF not found")
