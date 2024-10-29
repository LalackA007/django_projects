from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "Користувач з таким ім'ям або електронною поштою вже існує.")
            return redirect('register')
        
        user = User.objects.create(username=username, password=password, email=email)
        request.session['user_id'] = user.id
        messages.success(request, "Реєстрація пройшла успішно!")
        return redirect('home')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)
            request.session['user_id'] = user.id
            messages.success(request, "Авторизація пройшла успішно!")
            return redirect('home')
        except User.DoesNotExist:
            messages.error(request, "Неправильне ім'я користувача або пароль.")
            return redirect('login')

    return render(request, 'login.html')

def logout(request):
    request.session.flush()
    messages.success(request, "Вихід успішний!")
    return redirect('home')

def home(request):
    products = Product.objects.all()
    cart = request.session.get('cart', {})
    for product in products:
        item_key = f'product_{product.id}'
        product.in_cart = item_key in cart
    return render(request, 'home.html', {'products': products})

def accessories(request):
    accessories = Accessories.objects.all()
    cart = request.session.get('cart', {})
    for accessory in accessories:
        item_key = f'accessory_{accessory.id}'
        accessory.in_cart = item_key in cart
    return render(request, 'accessories.html', {'accessories': accessories})

def cart(request):
    if 'user_id' not in request.session:
        messages.error(request, "Будь ласка, зареєструйтеся або авторизуйтеся для оформлення замовлення.")
        return redirect('register')

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
        action = request.POST.get('action')
        if action == 'update':
            quantity = int(request.POST.get('quantity', 1))
            if item_id in cart:
                if quantity > 0:
                    cart[item_id]['quantity'] = quantity
                    messages.success(request, f"Кількість товару '{cart[item_id]['name']}' оновлено.")
                else:
                    del cart[item_id]
                    messages.success(request, "Товар видалено з кошика.")
            else:
                messages.error(request, "Товар не знайдено в кошику.")
        elif action == 'remove':
            if item_id in cart:
                del cart[item_id]
                messages.success(request, "Товар видалено з кошика.")

    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart')

def clear_cart(request):
    request.session['cart'] = {}
    request.session.modified = True
    messages.success(request, "Кошик очищено.")
    return redirect('cart')
