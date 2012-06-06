from django.http import HttpResponse
from django.template import Context, loader
from products.models import Product
from django.contrib.auth.decorators import login_required

def index(request):
    products_list= Product.objects.all().order_by('id')
    t = loader.get_template('products/index.html')
    c = Context ({
                  'product_list' : products_list,
                  })
    return HttpResponse(t.render(c))

def productdetail(request, product_id):
    return HttpResponse("product details page")


def categoryindex(request):
    return HttpResponse("Category index page")
