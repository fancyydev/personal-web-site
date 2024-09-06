from django.db import models

# Create your models here.
class Categories(models.Model):
    CATEGORIES_TYPES = [
        ('escritos', 'Escritos'),
        ('recomendaciones', 'Recomendaciones')
    ]
    name = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    type = models.CharField(max_length=15, choices=CATEGORIES_TYPES)
    
    def __str__(self):
        return self.name + "-" + self.type
    