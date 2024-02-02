from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Product, ProductMedia

def product_detail(request,id): #C112
    product_item = get_object_or_404(Product,id=id)
    product_media = ProductMedia.objects.filter(product=product_item)
    context = {'product_item':product_item,
               'product_media':product_media}
    image_urls = []  # Initialize an empty list to store image URLs
    thumb_url = product_item.product_image.url  # Retrieve thumbnail URL
    image_urls.append(thumb_url)  # Add thumbnail URL to the list
    
    for media in product_media:  # Iterate over product media objects
        image_url = media.image.url  # Retrieve image URL from each object
        image_urls.append(image_url)  # Add unique image URL to the list
    # print(image_urls) 
    context.update({'image_urls':image_urls})   
   
    return render(request, "shop/product/product_detail.html",context)