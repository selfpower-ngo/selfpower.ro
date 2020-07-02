'''
blog/urls
'''
from django.urls import include, path
from blog.views import BlogIndex, BlogDetail, ListPostsByTag

urlpatterns = [
    path(r'', BlogIndex.as_view(), name='blog_index'),  # Blog Index
    path(r'<slug>', BlogDetail.as_view(), name="entry_detail"),  # Blog Detail
    path(r'posts_by/<str:tag>', ListPostsByTag.as_view(),name='list_by_tag'),
]
