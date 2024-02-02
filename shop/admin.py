from django.contrib import admin

# Register your models here.
from .models import Category , Subcategory , Product , ProductMedia , ProductVarients, \
     ProductPricing


admin.site.register(Category)
admin.site.register(Subcategory)


class ProductVarientsInline(admin.TabularInline):
    model = ProductVarients
    fk_name = 'product'
    max_num = 4 # ToHide +Add another and only  one obj creation
    fieldsets = [
        (
            None,
            {
                "fields": ["size","color"],
            },
        ),

    ]
    #template = 'shop/admin/varients_form.html' 
    

class ProductPricingInline(admin.TabularInline):
    model = ProductPricing
    fk_name = 'product'
    max_num = 1 # To Hide + Add another and only  one obj creation
    fields = ['regular_price', 'sale_price']
    #template = 'shop/admin/pricing_form.html' 
    
class ProductMediaInline(admin.StackedInline):
    model = ProductMedia
    max_num = 4

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ["product_no"]
    list_display = ('id',)
    inlines = [ProductPricingInline,ProductMediaInline,ProductVarientsInline]
   
