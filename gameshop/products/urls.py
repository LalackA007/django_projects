from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accessories/', views.accessories, name='accessories'),
    path('cart/', views.cart, name='cart'),
    path('add_product_to_cart/<int:product_id>/', views.add_product_to_cart, name='add_product_to_cart'),
    path('add_accessory_to_cart/<int:accessory_id>/', views.add_accessory_to_cart, name='add_accessory_to_cart'),
    path('update_cart/<int:item_id>/', views.update_cart, name='update_cart'),
]
 