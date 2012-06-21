from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from products.models import Product, Category, Screenshot, ProductTag, AddProductForm, Video, Presentation, Tag, CategoryTag, CompareProductForm

def index(request):
    category_list = Category.objects.all()

    product_list = [[product for product in Product.objects.filter(category=category)] for category in category_list]
    t = loader.get_template('products/index.html')
    c = Context ({
                  'category_list' : category_list,
                  'product_list': product_list,
                  })
    return HttpResponse(t.render(c))

def get_by_id(request, product_id):
    product = Product.objects.filter(id=product_id)
    product = product[0]
    include_tag_list = ProductTag.objects.filter(product=product, include=True)
    exclude_tag_list = ProductTag.objects.filter(product=product, include=False)

    crumbs = [('Home', '/'), ('Products','/products'), (product.name, '/products/' + product.slug)]
    
    return render(request, 'products/product.html', {
        'crumbs': crumbs,
        'product':product,
        'include_tag_list':include_tag_list,
        'exclude_tag_list':exclude_tag_list,
        'screenshot_list' : Screenshot.objects.filter(product=product)
    })

def get_by_name(request, product_slug):
    product = Product.objects.filter(slug=product_slug)[0]
    include_tag_list = ProductTag.objects.filter(product=product, include=True)
    exclude_tag_list = ProductTag.objects.filter(product=product, include=False)
    
    crumbs = [('Home', '/'), ('Products','/products'), (product.name, '/products/' + product.slug)]
    return render(request, 'products/product.html', {
        'crumbs': crumbs,
        'product':product,
        'include_tag_list':include_tag_list,
        'exclude_tag_list':exclude_tag_list,
        'screenshot_list' : Screenshot.objects.filter(product=product)
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
                tag = tag.strip()
                temp_tag = Tag.objects.filter(name=tag)
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
    
def compare(request, product1_slug, product2_slug):
    crumbs = [('Home', '/'), ('Products', '/products/'), ('Compare', '/products/compare/')]
    
    if request.method == "POST":
        form = CompareProductForm(request.POST)
        if (form.is_valid()):
            product1 = form.cleaned_data['product1']
            product2 = form.cleaned_data['product2']
            product1 = Product.objects.filter(name=product1)[0]
            product2 = Product.objects.filter(name=product2)[0]
            return HttpResponseRedirect("/products/compare/" + product1.slug + "/" + product2.slug + "/")

    if product1_slug is not None and len(product1_slug) > 0:
        product1 = Product.objects.get(slug=product1_slug)
        product2 = Product.objects.get(slug=product2_slug)
        active_crumb = product1.name + ' V ' + product2.name
        crumbs.append((active_crumb, ''))
        category = product1.category
        category_tags = category.tags.all()
        product1_tags = [tag.name for tag in product1.tags.all()]
        product2_tags = [tag.name for tag in product2.tags.all()]
        tuples = dict([ (tag.name, ( tag.name in product1_tags, tag.name in product2_tags)) for tag in category_tags ])
    
        return render(request, 'products/compare.html', {
            'crumbs': crumbs,
            'tuples':tuples,
            'product1':product1,
            'product2':product2,
            'form':CompareProductForm(),
        })
    else:
        return render(request, 'products/compare.html', {
            'crumbs': crumbs,
            'tuples':None,
            'product1':None,
            'product2':None,
            'form':CompareProductForm(),
        })
        
        
    

