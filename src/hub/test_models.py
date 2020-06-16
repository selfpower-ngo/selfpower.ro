'''
Tests module for the hub app model
'''
from django.test import TestCase
import factory

from hub.models import Proiect

# Create your tests here.
class ProjectsFactory(factory.django.DjangoModelFactory):
    """
    Create some test data
    """
    class Meta:
        model = Proiect
        django_get_or_create = (
            'title',
            'text',
            'slug',
            'publish',
        )
    title = 'My test proiect'
    text = 'This is my test proiect text'
    slug = 'my-test-proiect'
    publish = True

class ProjectTest(TestCase):
    def test_create_project_published(self):
      # Create the proiect
      project = ProjectsFactory()
      # Check if we can find it
      all_projects = Proiect.objects.all()
      self.assertEquals(len(all_projects), 1)
      only_project = all_projects[0]
      self.assertEquals(only_project, project)
      # Check attributes
      self.assertEquals(only_project.title, 'My test proiect')
      self.assertEquals(only_project.text, 'This is my test proiect text')
      self.assertEquals(only_project.slug, 'my-test-proiect')
      self.assertEquals(only_project.publish, True)

    def test_create_project_unpublished(self):
      # Create the proiect
      project = ProjectsFactory(publish=False)
      # Check if we can find it
      all_projects = Proiect.objects.all()
      self.assertEquals(len(all_projects), 1)
      only_project = all_projects[0]
      # Check attributes
      # Un-publish the project
      # only_project.publish = False
      self.assertEquals(only_project.title, 'My test proiect')
      self.assertEquals(only_project.text, 'This is my test proiect text')
      self.assertEquals(only_project.slug, 'my-test-proiect')
      self.assertEquals(only_project.publish, False)
