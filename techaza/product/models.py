from pyexpat import model
from unicodedata import category
from django.db import models


category_choices = (
    (1,"mobile"),
    (2,"electric"),
    (3,"household")
)

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=250)
    price = models.PositiveIntegerField()    
    category = models.IntegerField(choices=category_choices)
    image = models.ImageField(upload_to='productImg', height_field=None, width_field=None, max_length=None, blank=True, null=True)