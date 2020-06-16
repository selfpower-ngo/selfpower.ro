'''
Tests module
'''
from django.test import TestCase, Client
from django.urls import resolve
from django.test.utils import override_settings

from .views import doilasuta, donatii, pdf_view

class TestDonations(TestCase):

    @classmethod
    def setUp(self):
       self.client = Client()

    def test_url_resolver(self):
        """
        Check if the paths match the views
        """
        doilasuta_url = resolve('/sustine/doilasuta/')
        self.assertEqual(doilasuta_url.func, doilasuta)

        donatii_url = resolve('/sustine/donatii/')
        self.assertEqual(donatii_url.func, donatii)

    def test_requests(self):
    	"""
    	Send requests to all the urls of the donations app
    	"""
    	response = self.client.get('/sustine/doilasuta/')
    	self.assertEqual(response.status_code, 200)

    	response = self.client.get('/sustine/donatii/')
    	self.assertEqual(response.status_code, 200)


    @override_settings(DEBUG=True)
    def test_in_debug(self):
        response = self.client.get('/sustine/pdf_view/')
        self.assertEqual(response.status_code, 200)

    def test_in_debug_not_found(self):
        response = self.client.get('/sustine/pdf_/')
        self.assertEqual(response.status_code, 404)
