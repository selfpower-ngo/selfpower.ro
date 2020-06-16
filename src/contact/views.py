'''
contact/views
'''
from __future__ import print_function
from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail
from django import forms
from .forms import contactForm


# Create your views here.
def contact(request):
    '''
    Contact web page.
    It contains the contact form.
    '''
    recaptchaKey = settings.GOOGLE_RECAPTCHA_SECRET_KEY

    confirmation = ''

    if request.method == 'POST':
        form = contactForm(data=request.POST, request=request)
        print('avem POST mesaj')

        if form.is_valid():

            print('formular valid')
            name = request.POST.get("name", "")
            emailUser = request.POST.get("email", "")
            phone = request.POST.get("phoneNo", "")
            body = "\nAcesta este un email trimis din formularul de contact.\n"
            body = body + "_______________________" + "\n"
            body = body + "Nume expeditor mesaj: " + name + "\n"
            body = body + "Email utilizator: " + emailUser + "\n"
            body = body + "Numar telefon: " + phone + "\n"
            body = body + "\n\n"
            body = body + request.POST.get("message", "") + "\n"
            body = body + "_______________________"

            confirmation = """
            Emailul a fost trimis catre echipa Selfpower!
            Veti primi un raspuns pe cat de repede cu putinta, multumim!
            """
            emailOffice = 'office@selfpower.ro'
            send_mail('Mesaj de la ' + name, body, emailOffice, [emailOffice], fail_silently=False)

    else:
        form = contactForm()

    if form.data.get('name') and confirmation == '':
        name = form.data.get('name')
    else:
        name = ''

    if form.data.get('email') and confirmation == '':
        email = form.data.get('email')
    else:
        email = ''

    if form.data.get('telefon') and confirmation == '':
        telefon = form.data.get('telefon')
    else:
        telefon = ''

    if form.data.get('message') and confirmation == '':
        message = form.data.get('message')
    else:
        message = ''

    context = {
        'form': form, 'name': name,
        'message': message, 'telefon': telefon,
        'email': email, 'recaptchaKey': recaptchaKey,
        'confirmation': confirmation
        }

    return render(request, 'contact.html', context)


def contact_email(request):
    print(request.POST)

    name = request.POST.get("name", "")
    email = request.POST.get("email", "")
    phone = request.POST.get("phoneNo", "")
    body = "\nAcesta este un email trimis din formularul de contact.\n"
    body = body + "_______________________" + "\n"
    body = body + "Nume expeditor mesaj: " + name + "\n"
    body = body + "Email utilizator: " + email + "\n"
    body = body + "Numar telefon: " + phone + "\n"
    body = body + "\n\n"
    body = body + request.POST.get("message", "") + "\n"
    body = body + "_______________________"

    confirmation = """
    Emailul a fost trimis catre echipa Selfpower! Veti primi un raspuns pe
    cat de repede cu putinta, multumim!
    """

    emailOffice = 'office@selfpower.ro'
    send_mail('Mesaj de la ' + name, body, emailOffice, [emailOffice], fail_silently=False)
    return render(request, 'contact.html', context={'confirmation': confirmation})
