'''
Add models in the admin dashboard
'''
from django.contrib import admin
from .models import Membership, UserProfile

admin.site.register(Membership)
admin.site.register(UserProfile)
