'''
login/forms
'''
import os
import requests
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from backend.aider import get_client_ip


class SignUpForm(UserCreationForm):
    '''
    SignUpForm
    The sign up form
    '''
    attribs = {'size': '40%'}
    username = forms.CharField(widget=forms.TextInput(attrs=attribs), required=True)
    first_name = forms.CharField(widget=forms.TextInput(attrs=attribs), max_length=90, required=False, help_text='Optional.')
    last_name = forms.CharField(widget=forms.TextInput(attrs=attribs), max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(widget=forms.TextInput(attrs=attribs), max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = (
            'username', 'first_name',
            'last_name', 'email',
            'password1', 'password2',
            )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SignUpForm, self).__init__(*args, **kwargs)

    def clean(self):
        '''
        In the fields verification process we also process
            the reCaptcha verification


        duplicate_users:
            check if chosen username is already taken or not
        '''
        ca_response = self.request.POST["g-recaptcha-response"]
        url = "https://www.google.com/recaptcha/api/siteverify"
        params = {
            'secret': os.environ['GOOGLE_RECAPTCHA_SECRET_SERVER_KEY'],
            'response': ca_response,
            'remoteip': get_client_ip(self.request)
        }
        verify_rs = requests.get(url, params=params, verify=True)
        verify_rs = verify_rs.json()

        duplicate_users = User.objects.filter(username=self.cleaned_data['username'])
        if duplicate_users.exists():
            self.add_error('username', "Acest nume de utilizator este deja folosit!")
        print('verify_rs: ', verify_rs)
        print('key: ', os.environ['GOOGLE_RECAPTCHA_SECRET_KEY'])

        status = verify_rs.get("success", False)
        if not status:
            raise forms.ValidationError(
                    ('Validarea Captcha nu a fost efectuata.'),
                    code='invalid',
                    )


class ProfileUpdateForUserProfile(forms.ModelForm):
    '''
    Form for updating UserProfile objects' data
    '''
    class Meta:
        model = UserProfile
        fields = ['phoneNo']


class ProfileUpdate(forms.ModelForm):
    '''
    This form is for updating the user data
    '''
    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email']

        def clean_email(self):
            '''
            Check email field
            '''
            cleaned_data = self.clean()
            url = cleaned_data.get('email')
            if not is_valid_url(url):  # You create this function
                self.add_error('email', "The field is not valid")
            return url
