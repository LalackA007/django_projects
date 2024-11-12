from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=125)
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique_for_date = True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} | by {self.owner}'

    def get_absolute_url(self):
        return reverse(
            'blog_app:post_by_slug',
            args=[
                self.created_at.year,
                self.created_at.month,
                self.created_at.day,
                self.slug,
            ]
        )