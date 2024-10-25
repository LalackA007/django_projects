from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accessories/', views.accessories, name='accessories'),
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
 