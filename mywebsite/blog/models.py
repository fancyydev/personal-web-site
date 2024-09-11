from django.db import models
from category.models import Categories
from django_ckeditor_5.fields import CKEditor5Field
from django.core.exceptions import ValidationError
import datetime

# Create your models here.
# Modelo de Posts
class BasePostsContent(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    img = models.ImageField(upload_to='posts/images/', verbose_name="Image")
    description = models.TextField()
    date = models.DateField(default=datetime.date.today)

    class Meta:
        abstract = True

class Post(BasePostsContent):
    POST_TYPES = [
        ('escritos', 'Escritos'),
        ('recomendaciones', 'Recomendaciones')
    ]
    type = models.CharField(max_length=15, choices=POST_TYPES)
    categories = models.ManyToManyField(Categories, related_name="posts")
    content = CKEditor5Field('Text', config_name='extends')

    def clean(self):
        # Solo valida si el objeto ya está guardado (tiene un ID)
        if self.pk and self.categories.exists():
            for category in self.categories.all():
                if category.type != self.type:
                    raise ValidationError(f"La categoría '{category.name}' no coincide con el tipo de post '{self.type}'.")

class Art(BasePostsContent):
    tools = models.TextField()