from django.db import models
from django.db.models.sql.constants import NULLABLE

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=256)
    desc = models.CharField(max_length=1024)
    
class Category(models.Model):
    name = models.CharField(max_length=1024)
    desc = models.CharField(max_length=1024)
    parent = models.ForeignKey('self')
    
class Product(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    
class Vote(models.Model):
    product = models.ForeignKey(Product)
    rating = models.IntegerField()
    
    