from django.db import models

# Create your models here.
class BlogSetting(models.Model):
    brand_name = models.CharField(max_length=255)
    author_name = models.CharField(max_length=255)
    bio = models.TextField()
    github = models.URLField(null=True, blank=True)

class Maqola(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    body = models.TextField()

class Resume(models.Model):
    body = models.TextField()
    is_active = models.BooleanField(default=True)