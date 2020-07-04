"""
Tests module for the authentication app
"""
from django.test import TestCase, Client
from django.urls import resolve, reverse
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views

from .views import signup, profile
from .models import UserProfile, Membership



class TestAuth(TestCase):
    """
    Manages the tests responsible for the authentication system
        /login app.
    """

    @classmethod
    def setUp(self):
        """
        Initiate setup
        """
        self.Client = Client()

    def test_reverse_urls(self):
        """
        Validates the urls and their names
        (Matching urls and names)
        """

        signup_url = reverse('signup')
        print("Reverse URL check:", signup_url)
        self.assertEqual(signup_url, '/autentificare/signup/')
        response = self.client.get(reverse('signup'), follow=True)
        self.assertEquals(response.status_code, 200)

        profile_url = reverse('profile')
        print("Reverse URL check:", profile_url)
        self.assertEqual(profile_url, '/autentificare/profile/')
        response = self.client.get(reverse('profile'), follow=True)
        self.assertEquals(response.status_code, 200)

        classical_login_url = reverse('panou_logare')
        print("Reverse URL check:", classical_login_url)
        self.assertEqual(classical_login_url, '/autentificare/panou_logare/')
        response = self.client.get(reverse('panou_logare'), follow=True)
        self.assertEquals(response.status_code, 200)


        panou_logare_url = reverse('panou_logare')
        print("Reverse URL check:", panou_logare_url)
#        self.assertEqual(panou_logare_url, '/panou_logare/') # this works while authenticated
        self.assertEqual(panou_logare_url, '/autentificare/panou_logare/')
        response = self.client.get(reverse('panou_logare'), follow=True)
        self.assertEquals(response.status_code, 200)

        instant_logout_url = reverse('instant_logout')
        print("Reverse URL check:", instant_logout_url)
#        self.assertEqual(instant_logout_url, '/logout/')
        self.assertEqual(instant_logout_url, '/autentificare/logout/')
        response = self.client.get(reverse('instant_logout'), follow=True)
        self.assertEquals(response.status_code, 200)

        password_reset_form_url = reverse('password_reset_form')
        print("Reverse URL check:", password_reset_form_url)
        self.assertEqual(password_reset_form_url, '/autentificare/password_reset/')
        response = self.client.get(reverse('password_reset_form'), follow=True)
        self.assertEquals(response.status_code, 200)

# This needs to be looked at:
        password_reset_done_url = reverse('password_reset_done')
        print("Reverse URL check:", password_reset_done_url)
        self.assertEqual(password_reset_done_url, '/autentificare/password_reset_done/')
        response = self.client.get(reverse('password_reset_done'), follow=True)
        self.assertEquals(response.status_code, 200)

        # ----- This needs extra care because of token
        # ---   reset/<uidb64>/<token>
        # password_reset_confirm_url = reverse('password_reset_confirm')
        # print("Reverse URL check:", password_reset_confirm_url)
        # self.assertEqual(password_reset_confirm_url, '/password_reset_confirm/')
        # response = self.client.get(reverse('password_reset_confirm'), follow=True)
        # self.assertEquals(response.status_code, 200)

# This needs to be looked at:
        password_reset_complete_url = reverse('password_reset_complete')
        print("Reverse URL check:", password_reset_complete_url)
        self.assertEqual(password_reset_complete_url, '/autentificare/password_reset_complete/')
        response = self.client.get(reverse('password_reset_complete'), follow=True)
        self.assertEquals(response.status_code, 200)

        # nopassword_url = reverse('nopassword')
        # print("Reverse URL check:", nopassword_url)
        # self.assertEqual(nopassword_url, '/accounts/')
        # response = self.client.get(reverse('nopassword'), follow=True)
        # self.assertEquals(response.status_code, 200)

        login_url = reverse('login')
        print("Reverse URL check:", login_url)
        self.assertEqual(login_url, '/autentificare/login/')
        response = self.client.get(reverse('login'), follow=True)
        self.assertEquals(response.status_code, 200)

        # ----- This needs extra care because of token
        # ---   reset/<uidb64>/<token>
        # activate_url = reverse('activate')
        # print("Reverse URL check:", activate_url)
        # self.assertEqual(activate_url, '/activate/<uidb64>/<token>/')
        # response = self.client.get(reverse('activate'), follow=True)
        # self.assertEquals(response.status_code, 200)




    def test_resolve_views(self):
        """
        Validates the urls and their views
            Match the urls with their specific views
        """

        signup_view = resolve('/autentificare/signup/')
        self.assertEqual(signup_view.func, signup)

        profile_view = resolve('/autentificare/profile/')
        self.assertEqual(profile_view.func, profile)

        classical_login_view = resolve('/autentificare/panou_logare/')
        self.assertEqual(classical_login_view.func.view_class, auth_views.LoginView)

    def test_create_user(self):
        """
        Creates an user inside the parallel DB.
            It gets autodestroyed after the tests
            -iterate an user creation
            -check if the user matches with its own  membership
            -check if the user matches with its own user profile
        """
        #check instantiation of an User object
        user = User()
        user.username = "test_user"
        user.email = "example@email.com"
        user.save()
        #check existence of id and userprofile
        #the userprofile is created automatically for any new user
        its_id = user.id
        its_profile = user.userprofile
        its_membership = user.membership

        #check own membership
        memb = Membership.objects.filter(user=user).first()
        self.assertEqual(memb, its_membership)

        #check own profile
        profil = UserProfile.objects.filter(user=user).first()
        self.assertEqual(profil, its_profile)
