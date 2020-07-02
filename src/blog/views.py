'''
Blog/views
'''
from django.views import generic
from django.views.generic import TemplateView
from blog.models import Entry, Tag
from django.shortcuts import render, redirect


class BlogIndex(generic.ListView):
    '''
    ListView to display blog posts with pagination
    '''
    template_name = "blog_index_element.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        '''
        Get blog posts that are published
        Customized query set
        '''
        context = super(BlogIndex, self).get_context_data(**kwargs)
        context['Entry'] = Entry.objects.published()
        context['tags'] = Tag.objects.all()
        return context

    def get_queryset(self):
        return Entry.objects.published().select_related('author')



class BlogDetail(generic.DetailView):
    '''
    BlogDetail(generic.DetailView)
    '''
    model = Entry
    template_name = "blog_post.html"



class AddPost(TemplateView):
    '''
    AddPost(TemplateView)
    '''
    template_name = "addPost.html"

class ListPostsByTag(TemplateView):

    template_name = 'blog_search_tag.html'

    def get(self, request, *args, **kwargs):
        tag_url = kwargs['tag']
        posts = Entry.objects.filter(tags__slug=tag_url)
        tags = Tag.objects.all()
        print(posts)
        return render(request, self.template_name, {'posts':posts,'query':tag_url,'tags':tags})

def search(request):
    query = request.GET.get('q')
    object_list = Entry.objects.filter(Q(tags__slug=query))
    print(object_list)
    return render(request,'blog_search_tag.html',{'object_list':object_list,'query':query})