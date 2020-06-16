'''
User-website interface. Contains the following webpages:
    -manual login form
    -magic link login trigger
    -sign up gate
    -profile  info page
'''
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import Membership, UserProfile
from .forms import SignUpForm, ProfileUpdate, ProfileUpdateForUserProfile
from .tokens import ACCOUNT_ACTIVATION_TOKEN


def profile(request):
    '''
    Profile page where the user information is displayed
        -the user can updates his/her user info
    '''
    if request.user.is_authenticated:
        abonament = Membership.objects.filter(user=request.user)

        if request.method == 'POST':
            form = ProfileUpdate(data=request.POST, instance=request.user)
            form2 = ProfileUpdateForUserProfile(data=request.POST, instance=request.user.userprofile)

            if form.is_valid() and form2.is_valid():
                its_user_profile = UserProfile.objects.filter(user=request.user).first()
                its_user_profile.phoneNo = form.data['phoneNo']
                its_user_profile.save()
                print('Valid form:  ', form.data['phoneNo'])

                update = form.save(commit=False)
                update.user = request.user
                update.save()
        else:
            form = ProfileUpdate(instance=request.user)
            form2 = ProfileUpdateForUserProfile(data=request.POST, instance=request.user.userprofile)


        return render(request, 'profile.html', {'abonament': abonament, 'form': form, 'form2': form2})
    return redirect('panou_logare')




def signup(request):
    '''
    Webpage for signup
    It contains a form that precedes the email verification
    '''
    logout(request)

    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST, request=request)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':(urlsafe_base64_encode(force_bytes(user.pk))),
                'token':ACCOUNT_ACTIVATION_TOKEN.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            message = 'Te rog confirma adresa de email pentru finalizarea inregistrarii.'
            template = 'registration/statusVerificare.html'
            return render(request, template, {'mesaj':message})

    else:
        form = SignUpForm()


    if form.data.get('username'):
        username = form.data.get('username')
    else:
        username = ''

    if form.data.get('first_name'):
        first_name = form.data.get('first_name')
    else:
        first_name = ''

    if form.data.get('last_name'):
        last_name = form.data.get('last_name')
    else:
        last_name = ''

    if form.data.get('email'):
        email = form.data.get('email')
    else:
        email = ''


    context = {
        'username': username,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,

        'confirmation': '',

        'form': form,
        'recaptchaKey': settings.GOOGLE_RECAPTCHA_SECRET_KEY
    }



    return render(request, 'signup.html', context)



def activate(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
    '''
    Defines the account activation process
    '''
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and ACCOUNT_ACTIVATION_TOKEN.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        message_succes = 'Confirmarea emailului a fost facuta. Acum poti intra in cont'
        message_failed = 'Linkul de activare este invalid!'
        template = 'registration/statusVerificare.html'
        return render(request, template, {'mesaj': message_succes})
    return render(request, template, {'mesaj': message_failed})
