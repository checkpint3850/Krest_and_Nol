from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Author, Category, Post, PostCategory, Comment

# Create your views here.


class PostsList(ListView):
    #  model = Post
    #  ordering = 'heading'
    queryset = Post.objects.order_by('-datetime_in')
    template_name = 'news.html'
    context_object_name = 'post'


class PostDetail(DetailView):
    model = Post
    template_name = 'one_news.html'
    context_object_name = "post"
