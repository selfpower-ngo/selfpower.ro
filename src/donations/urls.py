from django.urls import path
from .views import doilasuta, donatii, pdf_view

urlpatterns = [
    path(r'doilasuta/', doilasuta, name='doilasuta'),
    path(r'donatii/', donatii, name='donatii'),
    path(r'pdf_view/', pdf_view, name='pdf_view'),
]
