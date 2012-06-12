from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from products.models import Product, Category, Screenshot, ProductTag, AddProductForm, Video, Presentation, Tag, CategoryTag

def index(request):
    products_list= Product.objects.all().order_by('id')
    t = loader.get_template('products/index.html')
    c = Context ({
                  'product_list' : products_list,
                  })
    return HttpResponse(t.render(c))

def get_by_id(request, product_id):
    print product_id
    crumbs = ('Home', 'Products', product_id)
    product = Product.objects.filter(id=product_id)
    product = product[0]
    include_tag_list = ProductTag.objects.filter(product=product, include=True)
    exclude_tag_list = ProductTag.objects.filter(product=product, include=False)
    
    return render(request, 'products/product.html', {
        'crumbs': crumbs,
        'product':product,
        'include_tag_list':include_tag_list,
        'exclude_tag_list':exclude_tag_list,
    })

def get_by_name(request, product_slug):
    crumbs = ('Home', 'Products', product_slug)
    product = Product.objects.filter(slug=product_slug)[0]
    include_tag_list = ProductTag.objects.filter(product=product, include=True)
    exclude_tag_list = ProductTag.objects.filter(product=product, include=False)
    
    return render(request, 'products/product.html', {
        'crumbs': crumbs,
        'product':product,
        'include_tag_list':include_tag_list,
        'exclude_tag_list':exclude_tag_list,
    })

def add(request):
    crumbs = ('Home', 'Product', 'Add')
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if (form.is_valid()):
            n = form.cleaned_data['name']
            line = form.cleaned_data['tagline']
            d = form.cleaned_data['desc']
            l = form.cleaned_data['logo']
            s = form.cleaned_data['slug']
            u = form.cleaned_data['url']
            c = form.cleaned_data['category']
            cat = Category.objects.filter(id = c)[0]
            
            product = Product(name=n, desc=d, logo=l, url=u, slug=s, category=cat, tagline=line.strip())
            product.save()

            
            ss1 = form.cleaned_data['ss1']
            if (ss1 is not None):
                ps1 = Screenshot(product=product, url=ss1)
                ps1.save()
            ss2 = form.cleaned_data['ss2']
            if (ss2 is not None):
                ps2 = Screenshot(product=product, url=ss2)
                ps2.save()
            ss3 = form.cleaned_data['ss3']
            if (ss3 is not None):
                ps3 = Screenshot(product=product, url=ss3)
                ps3.save()
            ss4 = form.cleaned_data['ss4']
            if (ss4 is not None):
                ps4 = Screenshot(product=product, url=ss4)
                ps4.save()
            ss5 = form.cleaned_data['ss5']
            if (ss5 is not None):
                ps5 = Screenshot(product=product, url=ss5)
                ps5.save()
            
            v1 = form.cleaned_data['v1']
            if (v1 is not None):
                pv1 = Video(product=product, url=v1)
                pv1.save()
            v2 = form.cleaned_data['v2']
            if (v2 is not None):
                pv2 = Video(product=product, url=v2)
                pv2.save()
            v3 = form.cleaned_data['v3']
            if (v3 is not None):
                pv3 = Video(product=product, url=v3)
                pv3.save()
            
            p1 = form.cleaned_data['p1']
            if (p1 is not None):
                pp1 = Presentation(product=product, url=p1)
                pp1.save()
            p2 = form.cleaned_data['p2']
            if (p2 is not None):
                pp2 = Presentation(product=product, url=p2)
                pp2.save()
            p3 = form.cleaned_data['p3']
            if (p3 is not None):
                pp3 = Presentation(product=product, url=p3)
                pp3.save()
            
            t = form.cleaned_data['tags']
            tags = t.split(',')
            for tag in tags:
                temp_tag = Tag.objects.filter(name=tag.strip())
                if temp_tag.count() == 0:
                    temp_tag = Tag(name=tag, desc=tag)
                    temp_tag.save()
                    category_tag = CategoryTag(category=cat, tag=temp_tag, count=1)
                    category_tag.save()
                    product_tag = ProductTag(product=product, tag=temp_tag)
                    product_tag.save()
                else:
                    temp_tag = temp_tag[0]
                    category_tag = CategoryTag.objects.filter(category=cat, tag=temp_tag)[0]
                    if category_tag is None:
                        category_tag = CategoryTag(category=cat, tag=temp_tag, count=1)
                        category_tag.save()
                    else:
                        category_tag.count = category_tag.count + 1
                        category_tag.save()
                    
                    product_tag = ProductTag(product=product, tag=temp_tag)
                    product_tag.save()
            
            return HttpResponseRedirect("/products/")
    else:
        form = AddProductForm()
        
    return render(request, 'products/add.html', {
        'form': form,
        'crumbs': crumbs,
    })

def productdetail(request, product_id):
    return HttpResponse("product details page")


def categoryindex(request):
    return HttpResponse("Category index page")
