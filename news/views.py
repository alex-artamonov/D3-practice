from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.

class NewsList(ListView):
    # model = Post
    queryset = Post.objects.order_by('-created_dtm')
    template_name = 'news.html'
    context_object_name = 'news'

class NewsDetail(DetailView):
    model = Post
    template_name = 'news_detail.html'
    context_object_name = 'post'
