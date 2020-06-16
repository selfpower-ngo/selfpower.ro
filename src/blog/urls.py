'''
blog/urls
'''
from django.urls import include, path
from blog.views import BlogIndex, BlogDetail

urlpatterns = [
    path(r'', BlogIndex.as_view(), name='blog_index'),  # Blog Index
    path(r'<slug>', BlogDetail.as_view(), name="entry_detail"),  # Blog Detail
]
