from django.contrib import admin
from django.conf import settings
from . import models

class PostImageAdmin(admin.ModelAdmin):
	pass

class PostImageInline(admin.StackedInline):
	model = models.PostImage
	max_num = 10
	extra = 0

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	inlines = [PostImageInline]
	list_display = ["__unicode__", "pub_date"]



if(settings.DEBUG):
        admin.site.register(models.PostImage, PostImageAdmin)
        admin.site.register(models.Post, PostAdmin)












