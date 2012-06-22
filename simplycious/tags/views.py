# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from products.models import AddTagForm, Tag


def index(request):
    return HttpResponse("Tag index page")

def add(request):
    crumbs = [('Home', '/'), ('Tags', '/tags/'), ('Add', '')]
    if request.method == "POST":
        form = AddTagForm(request.POST)
        if (form.is_valid()):
            n = form.cleaned_data['name']
            d = form.cleaned_data['desc']
            p = form.cleaned_data['parent']
            r = form.cleaned_data['related']
            
            
            tag = Tag(name=n, desc=d)
            tag.parent = Tag.objects.get(id=int(p)) if p else None
            tag.related = Tag.objects.get(id=int(p)) if r else None
            tag.save()

            return HttpResponseRedirect("/tags/add/")
    else:
        form = AddTagForm()
    
    return render(request, 'tags/add.html', {
        'form': form,
        'crumbs': crumbs,
    })
