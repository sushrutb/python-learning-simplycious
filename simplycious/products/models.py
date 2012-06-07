from django.db import models
from django.db.models.sql.constants import NULLABLE


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=256)
    desc = models.TextField()
    last_modified = models.DateTimeField(auto_now = True)
    
class Category(models.Model):
    name = models.CharField(max_length=1024)
    desc = models.TextField()
    parent = models.ForeignKey('self', null=True)
    slug = models.SlugField()
    logo = models.URLField()
    tags = models.ManyToManyField(Tag, through='CategoryTag')
    last_modified = models.DateTimeField(auto_now = True)
    
class Product(models.Model):
    name = models.CharField(max_length=256)
    desc = models.TextField()
    slug = models.SlugField(max_length=64, unique=True)
    url = models.CharField(max_length=1024)
    logo = models.CharField(max_length = 1024)
    
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, through='ProductTag')
    
    last_modified = models.DateTimeField(auto_now = True)
    
class Vote(models.Model):
    product = models.ForeignKey(Product)
    rating = models.IntegerField()
    last_modified = models.DateTimeField(auto_now = True)
    
class ProductTag(models.Model):
    product = models.ForeignKey(Product)
    tag = models.ForeignKey(Tag)
    include = models.BooleanField()
    last_modified = models.DateTimeField(auto_now = True)
    
class ProductCollaterals(models.Model):
    COLLATERAL_CHOICES = (('V' , 'Video'),
                          ('P' , 'Slideshow'),
                          ('S', 'Screenshots')
                          )
    product = models.ForeignKey(Product)
    type = models.CharField(max_length=1, choices=COLLATERAL_CHOICES)
    
class CategoryTag(models.Model):
    category = models.ForeignKey(Category)
    tag = models.ForeignKey(Tag)
    last_modified = models.DateTimeField(auto_now = True)
  
    
