'''
hub/urls
'''
from django.urls import path
from .views import ProiecteIndex, ProiecteDetail

urlpatterns = [
    path(r'', ProiecteIndex.as_view(), name='proiecte_index'),
    path(r'<slug>', ProiecteDetail.as_view(), name="proiecte_detail"),
    # path(r'resurse/<slug>', ResurseDetail.as_view(), name="resurse_detail"),
    # path(r'resurse/', ResurseIndex.as_view(), name='resurse_index'),

    # membership, feature not offered yet. No link to this page.
    # path(r'membership/', membership, name='membership'),
]
