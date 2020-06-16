'''
blog/admin
'''
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget     # for Python 2.7
from django.db.models import TextField                      # for Python 2.7
from django.contrib import admin
from . import models
# Register your models here.

class EntryAdmin(MarkdownModelAdmin):
    '''
    Blog posts.
    Automatically add slug field
    '''
    list_display = ("title", "created")
    prepopulated_fields = {"slug": ("title",)}
    # Next line is a workaround for Python 2.x
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}

admin.site.register(models.Entry, EntryAdmin)
admin.site.register(models.Tag)
