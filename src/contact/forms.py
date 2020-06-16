'''
contact/forms
Contains one contact form. Send the massage to the Selfpower team by email.
See SMTP configuration for the implementation
'''
from django.conf import settings
import requests
from django import forms
from backend.aider import get_client_ip


class contactForm(forms.Form):
    '''
    Contact form. Uses SMTP and the Google accounts
    '''
    name = forms.CharField(label='name', max_length=100)
    email = forms.CharField(label='email', max_length=100)
    telefon = forms.CharField(label='telefon', max_length=100)
    message = forms.CharField(label='message', max_length=100)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(contactForm, self).__init__(*args, **kwargs)

    def clean(self):
        '''
        Verify fields after POST sending.
        Check for error and problems.

        Most of this method consists in the Google reCaptcha verification
        the anti-bot point.
        For details see Google docs.
        '''
        try:
            Ca = self.request.POST["g-recaptcha-response"]
            url = "https://www.google.com/recaptcha/api/siteverify"
            params = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_SERVER_KEY,
                'response': Ca,
                'remoteip': get_client_ip(self.request)
            }
            verify_rs = requests.get(url, params=params, verify=True)
            verify_rs = verify_rs.json()

            print('verify_rs: ', verify_rs)
            print('key: ', settings.GOOGLE_RECAPTCHA_SECRET_SERVER_KEY)

            status = verify_rs.get("success", False)
            if not status:
                raise forms.ValidationError(
                    ('Validarea Captcha nu a fost efectuata.'),
                    code='invalid',
                )
        except Exception as exception:
            print("One exception spotted during the processing of the form. Exception source: ", exception)
            raise forms.ValidationError(
                    ('O exceptie s-a produs in timpul procesarii. Sursa: ', exception),
                    code='invalid',
                )

        
