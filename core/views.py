from django.shortcuts import render,get_object_or_404
# Create your views here.
from shop.models import Product, ProductMedia

def home_main(request):
    product_items = Product.objects.all()
    context = {'product_item':product_items}
    return render(request, "core/core_hme.html", context)