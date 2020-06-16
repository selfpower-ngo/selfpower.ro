'''
hub/views
'''
from django.shortcuts import render
from django.views import generic
from hub.models import Proiect, Image, Resursa, BookUrl

from backend.procceses import isSFA

from django.conf import settings # for debug
from django import template

# Create your views here.
register = template.Library()


class ProiecteIndex(generic.ListView):
    '''
    ListView for proiecte model
    '''
    template_name = "proiecte_index.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        '''
        Get list of proiecte that are published
        Customized query set for sitemaps.py
        '''
        context = super(ProiecteIndex, self).get_context_data(**kwargs)
        context['Proiect'] = Proiect.objects.published()
        return context

    def get_queryset(self):
        queryset = Proiect.objects.get_queryset().order_by('id').prefetch_related('images').published()
        return queryset
 


class ProiecteDetail(generic.DetailView):
    '''
    DetailView for proiecte model
    '''
    model = Proiect
    template_name = "proiecte_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProiecteDetail, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']

        images_urls = list()

        for instance in Image.objects.filter(proiect__in=Proiect.objects.filter(slug=slug)):
            images_urls.append(instance.image.url)

        if settings.DEBUG:
            for obj in images_urls:
                print("hub.ProiecteDetail.images_urls.obj: ", obj)

        context['images'] = images_urls

        if settings.DEBUG:
            context_messafe = str(context).encode('utf-8')
            print(context_messafe)

        # And so on for more models
        return context



class ResurseIndex(generic.ListView):
    '''
    Listview for Resursa model
    '''
    model = Resursa
    template_name = "resurse_index.html"
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super(ResurseIndex, self).get_context_data(**kwargs)

        context['resurse'] = Resursa.objects.all()

        # And so on for more models
        return context




class ResurseDetail(generic.DetailView):
    '''
    DetailView for Resursa model
    '''
    model = Resursa
    template_name = "resurse_detail.html"

    def get_context_data(self, **kwargs):
        context = super(ResurseDetail, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']

        context['books'] = BookUrl.objects.filter(resursa=Resursa.objects.filter(slug=slug))
        context['videoUrl'] = embed_url(Resursa.objects.filter(slug=slug).first().videoUrl)

        return context


def embed_url(video_url):
    '''
    Transform an clickable youtube url into an embeded one for a frame
    '''
    new_adress = video_url.replace("watch?v=", "embed/")
    print(new_adress)
    return new_adress


def membership(request):
    '''
    Webview
    '''
    return render(request, 'membership.html', {'isSFA':isSFA})
