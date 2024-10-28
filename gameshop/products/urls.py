from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accessories/', views.accessories, name='accessories'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_product_to_cart/<int:product_id>/', views.add_product_to_cart, name='add_product_to_cart'),
    path('add_accessory_to_cart/<int:accessory_id>/', views.add_accessory_to_cart, name='add_accessory_to_cart'),
    path('update_cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
]
