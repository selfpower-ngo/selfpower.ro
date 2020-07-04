"""
Authentication system and users manager.

a) signup
-signup form
-activation link

b)login
-classical login, using username and password
-rapid login using magic link send by email

c)profile
-user data update throug profile page
-membership  (currently inactive feature)
-handles paid and free user-memberships
"""
from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import profile, signup, activate

urlpatterns = [
    path(r'panou_logare/', auth_views.LoginView.as_view(template_name='classical_login.html'), name='panou_logare'),

    path(r'logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='instant_logout'),

    path(r'profile/', profile, name='profile'),

    path(r'signup/', signup, name='signup'),

    # password reset
    path(r'password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset_form'),

    path(r'password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),

    path(r'reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),

    path(r'password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    # activation of account after signup:
    path(r'activate/<uidb64>/<token>', activate, name='activate'),

]
