from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import BlogPost
from .ownerviews import *

class BlogListView(ListView):
    model = BlogPost
    paginate_by = 2

class BlogDetailView(DetailView):
    model = BlogPost

class BlogDeleteView(OwnerDeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog_app:posts")

class BlogUpdateView(OwnerUpdateView):
    model = BlogPost
    fields = ['title', 'text']
    success_url = reverse_lazy("blog_app:posts")

class BlogCreateView(OwnerCreateView):
    model = BlogPost
    fields = ['title', 'text']
    success_url = reverse_lazy("blog_app:posts")
