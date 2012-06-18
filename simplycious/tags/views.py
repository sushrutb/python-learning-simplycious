# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from products.models import AddTagForm, Tag


def index(request):
    return HttpResponse("Tag index page")

def add(request):
    crumbs = ('Home', 'Category', 'Add')
    if request.method == "POST":
        form = AddTagForm(request.POST)
        if (form.is_valid()):
            n = form.cleaned_data['name']
            d = form.cleaned_data['desc']
            p = form.cleaned_data['parent']
            r = form.cleaned_data['related']
            
            tag = Tag(name=n, desc=d, parent=Tag.objects.filter(id=p)[0], related=Tag.objects.filter(id=r)[0])
            tag.save()

            return HttpResponseRedirect("/")
    else:
        form = AddTagForm()
    
    return render(request, 'tags/add.html', {
        'form': form,
        'crumbs': crumbs,
    })
