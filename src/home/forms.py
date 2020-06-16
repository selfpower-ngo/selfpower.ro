'''
home/forms
'''
from django import forms


class SignUpForm(forms.Form):
    '''
    Sign up form . First step in the sign up process
    It precedes an activation link sent by email to the new user.
    '''
    adresa_email = forms.EmailField()
    checkbox_agreement = forms.BooleanField()

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(SignUpForm, self).__init__(*args, **kwargs)

    def clean(self):

        message = 'Pentru utilizarea serviciului de newsletter este necesară confirmarea acordului dvs.'

        if not "checkbox_agreement" in self.request.POST:
            raise forms.ValidationError(
                        (message)
                    )
            
        checkbox_agreement = self.cleaned_data['checkbox_agreement']

        if checkbox_agreement==False:
            raise forms.ValidationError(
                        (message)
                    )