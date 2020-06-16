'''
Tests module
'''

from django.test import TestCase

from django.test import Client

class ExamplelPostTest(TestCase):

    @classmethod
    def setUpTestData(self):
       # creating instance of a client.
       self.client = Client()

    def test_postContactFormNoRecaptcha(self):
        """
        Test for Internal Server Error when g-recaptcha-response is missing
        from the POST request. Issue #122
        """
       # Issue a POST request.
        print("Test: send POST without g-recaptcha-response field")
        response = self.client.post('/contact/',{'name':'name','telefon':'pass',
        'message':'message',"email":"mail@mail.com"})
        print("Response: ", response)
       # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_postContactFormInvRecaptcha(self):
        """
        Test for when g-recaptcha-response field is in POST request
        but is invalid. Issue #122
        """
       # Issue a POST request.
        print("Test: send POST with invalid g-recaptcha-response field")
        response = self.client.post('/contact/',{'name':'name','telefon':'pass',
        'message':'message',"email":"mail@mail.com", "g-recaptcha-response":"blabla"})
        print("Response: ", response)
       # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
