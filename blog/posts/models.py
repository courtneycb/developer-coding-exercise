from django.db import models

SMALL = 100

# Create your models here.
class Post(models.Model):
    """Model for blog post in databse."""

    slug = models.CharField(max_length=SMALL, unique=True)
    title = models.CharField(max_length=SMALL)
    author = models.CharField(max_length=SMALL)
    content = models.TextField()
    tags = models.CharField(max_length=SMALL, default='')
