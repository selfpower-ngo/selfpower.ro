'''
home/views
Web views: home
Tasks:
-update() which updates the status of a navigator
-isSubscribed() check the status of a navigator
encoding: utf-8
'''
import json
import requests

from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from django.views.generic import TemplateView

from mailchimp3 import MailChimp

from SelfpowerProject.settings.utils import convert_text_to_md5
from .forms import SignUpForm
from blog.models import Tag

API_KEY = settings.MAILCHIMP_API
LIST_ID = settings.MAILCHIMP_LIST_ID


def update(subscriber_email, subscribeOrUnsubscribe):
    '''
    Update the status of subscriber to
    -subscribed
    -unsubscribed
    '''
    try:
        subscriber_hash = convert_text_to_md5(subscriber_email)

        authorization = 'Basic YWxleDplZjZiNzBjMDAzYTk3ZmVkZDJiYWI1OTE2ODcwZDZiMi11czEw'

        headers = {
            'Authorization': authorization,
        }

        payload = {
            "status": subscribeOrUnsubscribe
        }
        url = 'https://us10.api.mailchimp.com/3.0/lists/281deb4d67/members/'+subscriber_hash
        response = requests.patch(
                        url, headers=headers,
                        data=json.dumps(payload)
                        )
        response.raise_for_status()
        return 1  # reabonarea s-a facut cu succes prin API
    except Exception as e:
        return 0  # reabonarea nu s-a putut face prin API si userul trebuie
        # sa se reaboneze singur prin emailul primit de la mailchimp


def isSubscribed(subscriber_email):
    '''
    verify if the navigator is already subscribed in the newsletter list
    '''
    cond = True
    authorization = 'Basic YWxleDplZjZiNzBjMDAzYTk3ZmVkZDJiYWI1OTE2ODcwZDZiMi11czEw'
    subscriber_hash = convert_text_to_md5(subscriber_email)
    headers = {
                'Authorization': authorization
                }
    url = 'https://us10.api.mailchimp.com/3.0/lists/281deb4d67/members/'+subscriber_hash
    response = requests.patch(url, headers=headers)

    if response.json()['status'] == 'subscribed':
        cond = True
    else:
        cond = False

    return cond




def home(request):
    '''
    Web view
    Contains MailChimp form
    '''
    # print(client.lists.members.all(LIST_ID, get_all=False))

    if request.method == 'POST':

        try:
        
            client = MailChimp(mc_api=API_KEY, mc_user='office')

            Nform = SignUpForm(data=request.POST, request=request)
            if Nform.is_valid():
                new_email_address = Nform.cleaned_data['adresa_email']
                try:
                    client.lists.members.create(
                        LIST_ID, {
                            'email_address': new_email_address,
                            'status': 'subscribed',
                            'double_option': True,
                            'update_existing': False,
                            'send_welcome': True,
                            })
                    messages.success(request, 'Mulțumim pentru înregistrare')
                    return render(request, 'about.html', {'form': Nform, 'anchor': 'inregistrare'})

                except Exception as e:
                    # print(e.args[0]['title'])
                    if(e.args[0]['title'] == "Member Exists"):
                        if(isSubscribed(new_email_address)):
                            messages.error(request, "Membrul exisă deja și este abonat!")
                        else:
                            response = update(new_email_address, 'subscribed')
                            if response == 1:
                                messages.success(request, "Membrul deja existent a fost reabonat!")
                            else:
                                messages.error(request, "Se pare ca acest email a fost dezabonat. Pentru reabonare, folositi emailul primit dupa dezabonare si urmariti linkul.")
                    else:
                        messages.error(request,  e.args[0]['title'])

            else:
                messages.error(request, 'Formular incorect, vă rugăm să verificați din nou')
                return render(request, 'about.html', {'form': Nform, 'anchor': 'inregistrare'})

        except Exception as exception:
            print(exception)
            messages.error(request, exception)
            return render(request, 'about.html')
    else:
        Nform = SignUpForm()
        tags = Tag.objects.all()
    return render(request, 'about.html', {'form': Nform,'tags':tags})


class MembersView(TemplateView):
    """
    Display members of the team
    """
    template_name = "membri.html"
