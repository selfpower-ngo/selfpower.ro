"""
Tests module for SelfpowerProject URLs
"""
from django.test import TestCase, Client
from django.urls import reverse


class SiteMenuLinksTestClass(TestCase):
    """
    Manages the tests for checking all main Menu URLS
        /SelfpowerProject/ urls.py
    """

    def setUp(self):
        """
        Initiate setup
        """
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    # Already in home/tests.py
    # def test_home_url(self):
    #     # Test if domain/sitemaps.xml can be accesed
    #     home_url = reverse('home',)
    #     print("Reverse URL check:", home_url)
    #     self.assertEqual(home_url, '/')
    #     response = self.client.get(reverse(''), follow=True)
    #     self.assertEquals(response.status_code, 200)

    def test_home(self):
        # Test if domain/sitemaps.xml can be accesed
        home_url = reverse('home',)
        print("Reverse URL check home /:", home_url)
        self.assertEqual(home_url, '/')
        response = self.client.get(reverse('home'), follow=True)
        self.assertEquals(response.status_code, 200)

    def test_requests(self):
        """
        Simulate requests to test SelfpowerProject/urls.py
        Consider failed test if the returned code is different than 200
        """
        url_tester = Client()
        print ("Main urls.py tester")
        response = url_tester.get('/administrare/', follow=True)
        self.assertEqual(response.status_code, 200)
        response = url_tester.get('/acasa/despre', follow=True)
        self.assertEqual(response.status_code, 200)
        response = url_tester.get('/politica-de-confidentialitate', follow=True)
        self.assertEqual(response.status_code, 200)
        response = url_tester.get('/blog', follow=True)
        self.assertEqual(response.status_code, 200)
        response = url_tester.get('/proiecte', follow=True)
        self.assertEqual(response.status_code, 200)
        response = url_tester.get('/sustine/doilasuta/', follow=True)
        self.assertEqual(response.status_code, 200)
        response = url_tester.get('/ipn', follow=True)
        self.assertEqual(response.status_code, 200)
        response = url_tester.get('/acasa/membri', follow=True)
        self.assertEqual(response.status_code, 200)
        response = url_tester.get('/contact', follow=True)
        self.assertEqual(response.status_code, 200)
        response = url_tester.get('/testarehtml', follow=True)
        self.assertEqual(response.status_code, 200)
        response = url_tester.get('/construction', follow=True)
        self.assertEqual(response.status_code, 200)
