# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from products.models import Category, Tag, AddCategoryForm, CategoryTag


def index(request):
    crumbs = ('Home', 'Category', 'index')
    category_list = Category.objects.all() 
    t = loader.get_template('category/list.html')
    
    c = Context ({
                  'category_list' : category_list,
                  'crumbs': crumbs,
                })
    return HttpResponse(t.render(c))

def categorydetail(request, cat_slug):
    return HttpResponse("category details page")


def add(request):
    crumbs = ('Home', 'Category', 'Add')
    if request.method == "POST":
        form = AddCategoryForm(request.POST)
        if (form.is_valid()):
            n = form.cleaned_data['name']
            d = form.cleaned_data['desc']
            l = form.cleaned_data['logo']
            s = form.cleaned_data['slug']
            c = Category(name=n, slug=s, desc=d, logo=l)
            c.save()
            t = form.cleaned_data['tags']
            tags = t.split(',')
            for tag in tags:
                tag = tag.strip()
                temp_tag = Tag.objects.filter(name=tag)
                if temp_tag.count() == 0:
                    temp_tag = Tag(name=tag, desc=tag)
                    temp_tag.save()
                    categoryTag = CategoryTag(category=c, tag=temp_tag)
                    categoryTag.save()
                else:
                    temp_tag = temp_tag[0]
                    categoryTag = CategoryTag(category=c, tag=temp_tag)
                    categoryTag.save()
            
            return HttpResponseRedirect("/category/thanks/")
    else:
        form = AddCategoryForm()
    
    return render(request, 'category/add.html', {
        'form': form,
        'crumbs': crumbs,
    })


def save(request):
    return HttpResponse("Category saved!")