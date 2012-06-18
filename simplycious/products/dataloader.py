from products.models import *
import random 

screenshots = ('http://freshdesk.com/images/screenshots/help-desk-social-support-tumb.png', 'http://freshdesk.com/images/screenshots/help-desk-ticket-dispatch-tumb.png', 'http://freshdesk.com/images/screenshots/help-desk-custom-properties-tumb.png','http://freshdesk.com/images/screenshots/help-desk-ticket-response-tumb.png','http://freshdesk.com/images/screenshots/help-desk-activity-stream-tumb.png')
category_logo = 'http://dl.dropbox.com/u/3350353/simplycious/'
product_logo = 'http://dl.dropbox.com/u/3350353/simplycious/logo/'
top_tags = ('SaaS', 'Open Source', 'Freemium', 'Subscription', 'Social', 'Free', 'Premium')
top_categories = ('Enterprise', 'Mobile', '', 'Finance', 'HR', 'Consumer', 'Productivity', 'Personal')
products = ('freshdesk', 'zendesk', 'supportbee', 'helpshift', 'webengage', 'yammer', 'sap', 'Orange HRM', 'pipedrive', 'highrise', 'zoho')

def populate_tags():
    for tag in top_tags:
        t = Tag(name=tag, desc=tag)
        t.save()
        print t.id
        
def populate_categories():
    
    for category in top_categories:
        logo = category_logo + str(top_categories.index(category) + 1) + '.jpg'
        cat = Category(name=category, desc=category, logo=logo, slug=category)
        cat.save()
        for tag in Tag.objects.all():
            category_tag = CategoryTag(category=cat, tag=tag)
            category_tag.save()
        print cat.id
        
def populate_products():
    for category in Category.objects.all():
        for p in products:
            logo = product_logo + str(products.index(p)+1) + '.png'
            product = Product(name=p, desc=p, logo=logo, category=category, slug=p +'_'+ str(random.randrange(1,10000)), url="http://facebook.com", tagline='Greatest product ever built!')
            product.save()
            for tag in top_tags:
                product_tag = ProductTag(product=product, tag=Tag.objects.filter(name=tag)[0])
                product_tag.save()
            for ss in screenshots:
                screenshot = Screenshot(product=product,url=ss)
                screenshot.save()
   
        
populate_tags()
populate_categories()
populate_products()
    
