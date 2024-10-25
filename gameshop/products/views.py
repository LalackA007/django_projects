from django.shortcuts import render, redirect, get_object_or_404
from .models import *

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def accessories(request):
    accessories = Accessories.objects.all()
    return render(request, 'accessories.html', {'accessories': accessories})

def cart(request):
    return render(request, 'cart.html')

def add_to_cart(request, product_id):
    return render(request, 'cart.html')