from django.db import models
from django import forms
from django.forms.widgets import Textarea

class AddCategoryForm(forms.Form):
    name = forms.CharField()
    desc = forms.CharField(widget=forms.Textarea)
    slug = forms.SlugField()
    logo = forms.URLField()
    tags = forms.CharField(widget=forms.Textarea)

class AddProductForm(forms.Form):
    name = forms.CharField()
    desc = forms.CharField(widget=forms.Textarea)
    slug = forms.SlugField()
    url = forms.URLField()
    logo = forms.URLField()
    category = forms.ChoiceField(choices = (), widget=forms.Select)
    
    # screenshots, videos and presentations.
    ss1 = forms.URLField()
    ss2 = forms.URLField()
    ss3 = forms.URLField()
    ss4 = forms.URLField()
    ss5 = forms.URLField()
    v1 = forms.URLField()
    v2 = forms.URLField()
    v3 = forms.URLField()
    p1 = forms.URLField()
    p2 = forms.URLField()
    p3 = forms.URLField()
    
    tags = forms.CharField(widget=Textarea)
    
    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields['category'] = forms.ChoiceField(
            choices=[('', '----------')]+ [(category.id, category.name) for category in Category.objects.all()])

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
    def __unicode__(self):
        return self.name
    
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
    include = models.BooleanField(default = True)
    last_modified = models.DateTimeField(auto_now = True)
    
class Screenshot(models.Model):
    product = models.ForeignKey(Product)
    url = models.URLField()
    order_id = models.IntegerField(default = 0)
    home = models.BooleanField(default = False)
    
class Video(models.Model):
    product = models.ForeignKey(Product)
    url = models.URLField()
    order_id = models.IntegerField(default = 0)
    home = models.BooleanField(default = False)

class Presentation(models.Model):    
    product = models.ForeignKey(Product)
    url = models.URLField()
    order_id = models.IntegerField(default = 0)
    home = models.BooleanField(default = False)
        
class CategoryTag(models.Model):
    category = models.ForeignKey(Category)
    tag = models.ForeignKey(Tag)
    count = models.IntegerField(default = 0)
    imp = models.BooleanField(default = True)
    last_modified = models.DateTimeField(auto_now = True)  
    
