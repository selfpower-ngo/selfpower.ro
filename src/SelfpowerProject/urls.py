from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
# for serving images from server
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from blog.views import BlogIndex, BlogDetail  # feed
from backend.views import ipn
from home.views import home
from backend.views import send_email
from home.views import home
# for sitemaps
from .sitemaps import StaticViewSitemap, BlogPostSitemap, ProiecteIndexSitemap


sitemaps = {
    'static': StaticViewSitemap,
    'post': BlogPostSitemap,
    'proiecte': ProiecteIndexSitemap,
}

urlpatterns = [
    # default
    path(r'', home, name='home'),

    path(r'acasa/', include('home.urls')),

    path(r'administrare/', admin.site.urls),

    # external apps' urls
    path(r'markdown/', include('django_markdown.urls')),

    path(r'politica-de-confidentialitate/', TemplateView.as_view(
            template_name='politica-de-confidentialitate.html'), name='confidentialitate'),

    # blog section
    path(r'blog/', include('blog.urls')),

    # donations
    path(r'sustine/', include('donations.urls')),

    # contact
    path(r'contact/', include('contact.urls')),

    # Hub Proiecte Resurse
    path('proiecte/', include('hub.urls')),

    # ipn end-point listener for paypal transactions:
    path(r'ipn/', ipn, name='ipn'),

    # backend view for sending emails
    path(r'send_email/', send_email, name='send_email'),

    # user control
    path(r'autentificare/', include('login.urls')),

    # other
    path(r'testare/', include('testare.urls'), name='testare'),

    path(r'construction/', TemplateView.as_view(
            template_name='construction.html'), name='construction'),

    path(r'testarehtml/', TemplateView.as_view(
            template_name='testare.html'), name='testare'),

    path(r'sitemap.xml', sitemap, {'sitemaps': sitemaps},
            name='django.contrib.sitemaps.views.sitemap'),

]

# If running DEBUG we need this in order to serve static files
# we are mapping the URL to the Paths specified in settings.py

# in order to serve static
# disable in PROD

if settings.DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

if settings.DEBUG and not settings.STAGING:
    import pprint
    #urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    print("urls.py report: urlpatterns is")  # this is to get the final list in console output
    pprint.pprint(urlpatterns)
