from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import *
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

@csrf_protect  # Декоратор, щоб переконатись, що CSRF перевіряється
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Логіка створення користувача (спрощено)
        return redirect('login')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def accessories(request):
    accessories = Accessories.objects.all()
    return render(request, 'accessories.html', {'accessories': accessories})

def cart(request):
    return render(request, 'cart.html')

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Переконайтеся, що користувач є автентифікованим
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to add products to your cart.")
        return redirect('login')

    # Отримання або створення замовлення
    order,  = Order.objects.get_or_create(user=request.user)

    # Додаємо продукт до замовлення (приклад, залежно від вашої моделі)
    order.products.add(product)
    messages.success(request, f'{product.name} was added to your cart.')

    return redirect('cart')
    # Ensure that the user is authenticated
    if not request.user.is_authenticated:
        return redirect('login')  # Replace 'login' with the name of your login route

    # Fetch or create an order for the authenticated user
    order, created = Order.objects.get_or_create(user=request.user)
    # Further processing of adding to the cart

    product = get_object_or_404(Product, id=product_id)
    order, created = Order.objects.get_or_create(user=request.user)

    
    item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if not created:
        order_item.quantity += 1
        order_item.save()

    return redirect('cart')

    product = get_object_or_404(Product, id=product_id)
    
    # Шукаємо активне замовлення (якщо потрібне)
    order, created = Order.objects.get_or_create(user=request.user, is_active=True)
    
    # Створюємо або оновлюємо товар у кошику
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    # Якщо товар вже був у кошику, збільшуємо кількість
    if not created:
        order_item.quantity += 1
        order_item.save()
    
    return redirect('cart')