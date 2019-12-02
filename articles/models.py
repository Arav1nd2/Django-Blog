from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Add thumbnail and author later
