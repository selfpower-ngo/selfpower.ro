'''
Models of the blog section
-Blog posts
-Tags
'''
from __future__ import unicode_literals
from django.db import models
from django_markdown.models import MarkdownField  # to fix markdown
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Tag(models.Model):
    '''
    Tag. A class that is assigned to one ore more blog posts to classifiy it.
    A blog post can have more tags.
    A tag is defined by one single slug.
    '''
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name_plural = "Tag-uri"

    def __str__(self):
        return self.slug


class EntryQuerySet(models.QuerySet):
    '''
    A query set model.
    '''
    def published(self):
        '''
        Return blog posts that are published
        '''
        return self.filter(publish=True)


def get_sentinel_user():
    '''
    Get a default user 'sters' in case a post has no user.
    '''
    return get_user_model().objects.get_or_create(username='sters')[0]


class Entry(models.Model):
    '''
    Blog post.
    '''
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=400)
    body = MarkdownField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user), default=0)
    created = models.DateTimeField()
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)
    objects = EntryQuerySet.as_manager()
    image = models.ImageField(upload_to='postImage', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        '''
        Get absolute url of object blog entry (post)
        '''
        return reverse("entry_detail", kwargs={"slug": self.slug})

    class Meta:
        '''
        Romanian titles.
        '''
        verbose_name = "Postare din Blog"
        verbose_name_plural = "Postari din Blog"
        ordering = ["-created"]
