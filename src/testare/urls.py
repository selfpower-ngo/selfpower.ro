from django.conf.urls import include, url
from django.conf import settings
from .views import getPosts, apiInterface


if(settings.DEBUG):
	urlpatterns = [
	        # url(r'^$', getPosts, name='getPosts'),
	        # url(r'^patch/', apiInterface, name='patch'),
	]
else:
	urlpatterns = [
	]
 