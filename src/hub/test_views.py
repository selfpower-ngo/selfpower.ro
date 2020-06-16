'''
Tests module for hub app views
'''
from django.test import TestCase, Client

import factory

from django.urls import resolve, reverse

from .views import ProiecteIndex
from .models import Proiect

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
    slug = 'published-proiect-slug'
    publish = True


class TestHub(TestCase):
    """
    Testing manager for the hub app.
        Subclass of TestCase
    """
    @classmethod
    def setUp(self):
        """
        Static method for general setup
        """
        self.Client = Client()

    def test_resolve_views(self):
        """
        Validates the urls and their views
          (Check if the urls match the views)
        """
        proiecte_index = resolve('/proiecte/')
        self.assertEqual(proiecte_index.func.view_class, ProiecteIndex)

    def test_requests(self):
        """
        Simulate requests to the endpoints/views
          Consider status code 200 as passed test.
        """
        response = self.client.get('/proiecte/')
        self.assertEqual(response.status_code, 200)

    def test_reverse_urls(self):
        """
        Validates the urls and their names
          (Check if the urls match the names)
        """
        proiecte_index = reverse('proiecte_index')
        print("Reverse URL check home /:", proiecte_index)
        self.assertEqual(proiecte_index, '/proiecte/')
        response = self.client.get(reverse('proiecte_index'), follow=True)
        self.assertContains( response, '<strong>Proiecte', status_code=200 )

        proiecte_detail = reverse('proiecte_detail', args=['test'])
        print("Reverse URL check home /:", proiecte_detail)
        self.assertEqual(proiecte_detail, '/proiecte/test')

    def test_model_creation(self):
        """
        This methos covers the instantiation of the model classes.
            !!! Please keep in mind that the process uses a different database for testing,
            so any saved instance won't be found in the real database. The instance is
            destroyed when the test returns.
        """
        instance = Proiect()
        instance.title = "Title of instance"
        instance.text = "This is the text of the title"
        instance.slug = "test-instance"
        instance.save()

    def test_projects_published(self):
        """
        Validates the urls and their names
          (Check if the urls match the names)
        """
        test_project = ProjectsFactory()
        test_project_unpublished = ProjectsFactory(slug = 'unpublished-proiect-slug', publish=False)
        # Check for the published project in Project List template
        response = self.client.get(reverse('proiecte_index'), follow=True)
        self.assertContains(response, 'proiect-slug', status_code=200 )
        self.assertContains( response, '<strong>Proiecte', status_code=200 )
        # Check on page if link for published exists, and not published not:
        self.assertContains( response, '<a href="/proiecte/published-proiect-slug')
        self.assertNotContains( response, '<a href="/proiecte/unpublished-proiect-slug')
        # Check if published project details is accesible
        proiecte_detail = reverse('proiecte_detail', args=['published-proiect-slug'])
        self.assertEqual(proiecte_detail, '/proiecte/published-proiect-slug')
        # Check if un-published project details is accesible
        proiecte_detail = reverse('proiecte_detail', args=['unpublished-proiect-slug'])
        self.assertEqual(proiecte_detail, '/proiecte/unpublished-proiect-slug')
        # to be implemented later
        # response = self.client.get(reverse('proiecte_detail', args=['test']), follow=True)
        # self.assertEquals(response.status_code, 200)
