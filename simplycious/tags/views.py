# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from products.models import Product
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("Tag index page")

def add(request):
    return HttpResponse("Add tags")
