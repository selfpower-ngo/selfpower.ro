'''
Tests module
-Please use pass 'enforce_csrf_checks=True' as argument to the Client()
if you want to enable the csrf validation!
'''
from django.test import TestCase, Client
from django.urls import resolve

from .views import home, MembersView

class TestPrime(TestCase):
    """
    A TestCase class responsible for the home app tests
    """

    def test_url_resolver(self):
        """
        Check if the paths match the views
        """
        despre_url = resolve('/acasa/despre/')
        self.assertEqual(despre_url.func, home)

        membri_url = resolve('/acasa/membri/')
        self.assertEqual(membri_url.func.view_class, MembersView)

    def test_requests(self):
        """
        Simulate requests to the home app's views.
        Consider failed test if the returned code is different than 200
        """
        home_tester = Client()
        response = home_tester.get('/acasa/despre/')
        self.assertEqual(response.status_code, 200)

        response = home_tester.get('/acasa/membri/')
        self.assertEqual(response.status_code, 200)
