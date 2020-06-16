'''
hub/admin
'''
from django.contrib import admin
from django_markdown.admin import MarkdownModelAdmin
from django_markdown.widgets import AdminMarkdownWidget
from django.db.models import TextField
from . import models


class PostImageAdmin(admin.ModelAdmin):
    '''
    Empty
    '''


class PostImageInline(admin.StackedInline):
    '''
    InLine  admin
    '''
    model = models.Image
    max_num = 15
    extra = 0


class PostUrlInLine(admin.StackedInline):
    '''
    For Book Url
    '''
    model = models.BookUrl
    max_num = 20
    extra = 0


class PostAdmin(MarkdownModelAdmin):
    '''
    Admin table for 'blog' posts
    '''
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PostImageInline]
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}


class ResourceAdmin(MarkdownModelAdmin):
    '''
    Admin table for 'resource' items
    '''
    prepopulated_fields = {"slug": ("title",)}
    #  this automatically creates a slug
    inlines = [PostUrlInLine]
    formfield_overrides = {TextField: {'widget': AdminMarkdownWidget}}


admin.site.register(models.Proiect, PostAdmin)
# admin.site.register(models.Resursa, ResourceAdmin)
# commented out beacause this is not used by client anymore
