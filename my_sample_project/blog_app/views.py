from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import BlogPost
from .ownerviews import *
from django.shortcuts import get_object_or_404
from django.http import Http404

class BlogListView(ListView):
    model = BlogPost
    paginate_by = 6

class BlogDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk")
        year = self.kwargs.get("year")
        month = self.kwargs.get("month")
        day = self.kwargs.get("day")
        slug_id = self.kwargs.get("slug_id")

        if pk:
            return get_object_or_404(self.model, pk=pk)
        elif slug_id:
            return get_object_or_404(self.model, created_at__year=year, created_at__month=month, created_at__day=day, slug = slug_id)
        else:
            raise Http404("No object found matching the provided criteria.")

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
