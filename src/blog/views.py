'''
Blog/views
'''
from django.views import generic
from django.views.generic import TemplateView
from blog.models import Entry


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
