from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    img = models.ImageField(upload_to='projects/images')
    url = models.URLField(max_length=200)
    