'''
The backend app has no module yet that should be displayed
in the admin dashboard
'''
from django.contrib import admin
from .models import SiteConfig

admin.site.register(SiteConfig)