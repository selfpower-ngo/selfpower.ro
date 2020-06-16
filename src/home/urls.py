from django.urls import path
from django.views.generic import TemplateView

from .views import home, MembersView

urlpatterns = [
    path(r'despre/', home, name='about'),

    path(r'membri/', MembersView.as_view(), name='membri'),

    path(r'parteneri/', TemplateView.as_view(template_name='parteneri.html'), name='parteneri'),
]
