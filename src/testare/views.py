import requests, json
from django.shortcuts import render
from .models import Post, PostImage
from SelfpowerProject.settings.utils import convert_text_to_md5
# Create your views here.

def getPosts(request):

	# Get all blog posts
	posts = Post.objects.all().order_by('-pub_date')

	# Get all images
	images = PostImage.objects.all()

	# Display all the posts
	return render(request, 'testare.html', {'posts': posts, 'images': images}) 



def sendRequest(subscriber_hash):
    """ Makes use of Send API:
        https://developers.facebook.com/docs/messenger-platform/send-api-reference
    """
    headers = {
        'Authorization': 'Basic YWxleDplZjZiNzBjMDAzYTk3ZmVkZDJiYWI1OTE2ODcwZDZiMi11czEw',
    }
    
    payload = {
        'recipient': {
            'id': 'user_id',
        },
        'message': "messageee",
    }
    url = 'https://us10.api.mailchimp.com/3.0/lists/281deb4d67/members/'+subscriber_hash
    response = requests.get(url, headers=headers,
                             data=json.dumps(payload))
    response.raise_for_status()
    return response.json() 


def isSubscribed(subscriber_email):

	cond=True

	subscriber_hash=convert_text_to_md5(subscriber_email)
	headers = {
	'Authorization': 'Basic YWxleDplZjZiNzBjMDAzYTk3ZmVkZDJiYWI1OTE2ODcwZDZiMi11czEw',
	}
	url = 'https://us10.api.mailchimp.com/3.0/lists/281deb4d67/members/'+subscriber_hash
	response = requests.patch(url, headers=headers)

		#print(response.raise_for_status())
		#return True


	if response.json()['status']=='subscribed':
		cond=True 
	else:
		cond=False

	return cond


def update(subscriber_email, subscribeOrUnsubscribe):

	subscriber_hash=convertTextToMD5(subscriber_email)

	headers = {
		'Authorization': 'Basic YWxleDplZjZiNzBjMDAzYTk3ZmVkZDJiYWI1OTE2ODcwZDZiMi11czEw',
	}
    
	payload = {
		"status": subscribeOrUnsubscribe
	}
	url = 'https://us10.api.mailchimp.com/3.0/lists/281deb4d67/members/'+subscriber_hash
	response = requests.patch(url, headers=headers,
                             data=json.dumps(payload))
	response.raise_for_status()
	return response.json() 


def apiInterface(request):

	update('email@example.com','unsubscribed')

	#print( isSubscribed('email@example.com') )

	return render(request, 'parteneri.html')

	
