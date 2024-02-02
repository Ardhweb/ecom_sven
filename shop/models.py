from django.db import models
from django.urls import reverse #C112
# Create your models here.
from .generate_code import code_request

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.category_name

class Subcategory(models.Model):
    sub_category_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.sub_category_name


class Product(models.Model):
    product_no = models.CharField(max_length=255,default=code_request.get_code('hex',8),editable=False)
    product_image = models.ImageField(upload_to='uploads/',default="True" )
    product_title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, max_length=455)
    category_and_subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    in_stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_title
     
    def get_absolute_url(self):
       return reverse('shop:product-detail',args=[self.id, ]) #C112




class ProductVarients(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=50,)
    color = models.CharField(max_length=50,choices=COLOR_LIST, default='none')


class ProductPricing(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    regular_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2,blank=True)




class ProductMedia(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/products/images/')
    