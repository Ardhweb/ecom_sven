from django.urls import path
from. import views

app_name = 'shop' #C112
urlpatterns = [
    
    path('product/<int:id>/',views.product_detail,name="product-detail"), #C112
]

