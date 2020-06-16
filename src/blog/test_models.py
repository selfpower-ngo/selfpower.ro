'''
Tests module for the blog app model
'''
from django.test import TestCase
import factory

from datetime import datetime
from django.utils import timezone

from django.contrib.auth.models import User, Permission # Required to assign User to a Blog Post
from django.contrib.auth.hashers import make_password

from blog.models import Tag, Entry

# Create your tests here.

class UserFactory(factory.django.DjangoModelFactory):
    # Generate a valid django user
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('email')
    password = factory.LazyFunction(lambda: make_password('pi3.1415'))
    is_staff = True
    is_superuser = True

class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag
        django_get_or_create = (
            'slug',
        )
    # slug = 'test-tag'
    slug = factory.Sequence(lambda n: "test-slug-%s" % n)

class BlogPostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Entry
        django_get_or_create = (
            'title',
            'subtitle',
            'body',
            'slug',
            'created',
        )
    title = 'My test post'
    subtitle = 'My subtitle'
    body = 'This is my test blog post'
    slug = 'my-test-post'
    created = timezone.now()
    author = factory.SubFactory(UserFactory)

class BlogPostTest(TestCase):
    def test_create_user(self):
      # Create the tag
      user = UserFactory()
      # Check if we can find it
      all_users = User.objects.all()
      self.assertEquals(len(all_users), 1)
      only_user = all_users[0]
      self.assertEquals(only_user, user)

    def test_create_post(self):
      # Create the tag
      user = UserFactory()
      # Create the tag
      tag = TagFactory()
      # Create the post
      post = BlogPostFactory()
      # Add the tag only after creating post
      post.tags.add(tag)
      # Check if we can find it
      all_posts = Entry.objects.all()
      self.assertEquals(len(all_posts), 1)
      only_post = all_posts[0]
      self.assertEquals(only_post, post)
      # Check attributes
      self.assertEquals(only_post.title, 'My test post')
      self.assertEquals(only_post.body, 'This is my test blog post')
      self.assertEquals(only_post.slug, 'my-test-post')
      self.assertEquals(only_post.created.day, post.created.day)
      self.assertEquals(only_post.created.month, post.created.month)
      self.assertEquals(only_post.created.year, post.created.year)
      self.assertEquals(only_post.created.hour, post.created.hour)
      self.assertEquals(only_post.created.minute, post.created.minute)
      self.assertEquals(only_post.created.second, post.created.second)
      # Check tags
      post_tags = only_post.tags.all()
      self.assertEquals(len(post_tags), 1)
      only_post_tag = post_tags[0]
      self.assertEquals(only_post_tag, tag)
      self.assertEquals(only_post_tag.slug, 'test-slug-0')

class TagModelTestClass(TestCase):
    def test_create_tag(self):
      # Create the tag
      tag = TagFactory()
      # Check if we can find it
      all_tags = Tag.objects.all()
      self.assertEquals(len(all_tags), 1)
      only_tag = all_tags[0]
      self.assertEquals(only_tag, tag)
      # Check attributes
      self.assertEquals(only_tag.slug, 'test-slug-1')
