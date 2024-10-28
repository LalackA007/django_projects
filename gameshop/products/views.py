from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            if user.password == password:
                request.session['user_id'] = user.id
                messages.success(request, 'Ви успішно увійшли!')
                return redirect('home')
            else:
                messages.error(request, 'Невірний пароль.')
        except User.DoesNotExist:
            messages.error(request, 'Користувача не знайдено.')

    return render(request, 'registration/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Користувач з таким ім\'ям вже існує.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Цей email вже зареєстровано.')
        else:
            User.objects.create(username=username, password=password, email=email)
            messages.success(request, 'Реєстрація успішна! Тепер ви можете увійти.')
            return redirect('login')

    return render(request, 'registration/signup.html')

def checkout(request):
    if 'user_id' not in request.session:
        messages.error(request, 'Вам потрібно увійти, щоб оформити замовлення.')
        return redirect('login')

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        payment = request.POST.get('payment')

        if all([name, address, phone, email, payment]):
            request.session['cart'] = {}
            request.session.modified = True
            messages.success(request, 'Ваше замовлення успішно оформлено!')
            return redirect('home')
        else:
            messages.error(request, 'Будь ласка, заповніть усі поля форми.')

    return render(request, 'checkout.html')

def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        messages.success(request, 'Ви успішно вийшли.')
    return redirect('home')


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def accessories(request):
    accessories = Accessories.objects.all()
    return render(request, 'accessories.html', {'accessories': accessories})

def cart(request):
    cart = request.session.get('cart', {})
    total_price = round(sum(float(item['price']) * item['quantity'] for item in cart.values()), 2)

    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        payment = request.POST.get("payment")

        if all([name, address, phone, email, payment]):
            request.session['cart'] = {}
            request.session.modified = True
            messages.success(request, "Ваше замовлення було успішно оформлено!")
        else:
            messages.error(request, "Будь ласка, заповніть усі поля форми.")

        return redirect('cart')

    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})

def add_product_to_cart(request, product_id):
    item = Product.objects.filter(id=product_id).first()
    if not item:
        messages.error(request, "Цей товар не знайдено.")
        return redirect('home')

    cart = request.session.get('cart', {})
    item_key = f'product_{product_id}'

    if item_key in cart:
        cart[item_key]['quantity'] += 1
    else:
        cart[item_key] = {
            'name': item.name,
            'price': str(item.price),
            'quantity': 1,
            'image_url': item.image.url,
            'type': 'product'
        }

    request.session['cart'] = cart
    request.session.modified = True

    messages.success(request, f"Товар '{item.name}' додано до кошика!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def add_accessory_to_cart(request, accessory_id):
    item = Accessories.objects.filter(id=accessory_id).first()
    if not item:
        messages.error(request, "Цей аксесуар не знайдено.")
        return redirect('home')

    cart = request.session.get('cart', {})
    item_key = f'accessory_{accessory_id}'

    if item_key in cart:
        cart[item_key]['quantity'] += 1
    else:
        cart[item_key] = {
            'name': item.name,
            'price': str(item.price),
            'quantity': 1,
            'image_url': item.image.url,
            'type': 'accessory'
        }

    request.session['cart'] = cart
    request.session.modified = True

    messages.success(request, f"Аксесуар '{item.name}' додано до кошика!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def update_cart(request, item_id):
    cart = request.session.get('cart', {})

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart[str(item_id)]['quantity'] = quantity
        else:
            del cart[str(item_id)]

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart')
