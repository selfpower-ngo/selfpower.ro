"""
Tests module for the sitemap.xml
"""
import xml.dom.minidom  # print pretty xml
from django.test import TestCase, Client
from django.urls import reverse


class SitemapTestClass(TestCase):
    """
    Manages the tests responsible for the static
        /sitemap.xml
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

    def test_sitemap_url(self):
        # Test if domain/sitemaps.xml can be accesed
        sitemap_url = reverse('django.contrib.sitemaps.views.sitemap',)
        print("Reverse URL check:", sitemap_url)
        self.assertEqual(sitemap_url, '/sitemap.xml')
        response = self.client.get(reverse('django.contrib.sitemaps.views.sitemap'), follow=True)
        # Check response OK
        self.assertEquals(response.status_code, 200)
        # Print response content in pretty xml
        # response_content = xml.dom.minidom.parseString(response.content)
        # xml_pretty = response_content.toprettyxml()
        # print("Sitemap content, xml_pretty:", xml_pretty)
        self.assertContains(response,"acasa", 2)
        self.assertContains(response,"doilasuta")
        self.assertContains(response,"contact")
        self.assertContains(response,"despre")
