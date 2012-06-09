# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from products.models import Category, AddCategoryForm
from django.contrib.auth.decorators import login_required

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
            return HttpResponseRedirect("/thanks/")
    else:
        form = AddCategoryForm()
    
    return render(request, 'category/add.html', {
        'form': form,
        'crumbs': crumbs,
    })


def save(request):
    return HttpResponse("Category saved!")
