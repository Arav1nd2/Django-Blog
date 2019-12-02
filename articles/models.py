from django.db import models

from django.contrib import admin
from django.contrib.auth.models import User


class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    # Add thumbnail and author later

    def snippet(self):
        return self.body[0:50]+"..."


admin.site.register(Articles)
