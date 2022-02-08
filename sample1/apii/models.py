from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)
    
class Article(models.Model):
    slug=models.SlugField()
    title=models.CharField(max_length=256)
    description=models.TextField()
