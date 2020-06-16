from django.urls import path
from .views import contact, contact_email

urlpatterns = [
	path(r'', contact, name='contact'),
	path(r'contact_email/', contact_email, name='contact_email'),
]