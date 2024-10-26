from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Accessories

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def accessories(request):
    accessories = Accessories.objects.all()
    return render(request, 'accessories.html', {'accessories': accessories})

def cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())
    success_message = None

    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        payment = request.POST.get("payment")

        if all([name, address, phone, email, payment]):
            # Clear the cart after successful order
            request.session['cart'] = {}
            request.session.modified = True
            success_message = "Ваше замовлення було успішно оформлено!"
        else:
            success_message = "Будь ласка, заповніть усі поля форми."

    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price, 'success_message': success_message})

def add_product_to_cart(request, product_id):
    # Attempt to find the product by ID
    item = Product.objects.filter(id=product_id).first()
    
    # If the product is not found, redirect to the home page
    if not item:
        return redirect('home')

    # Get the current cart from the session
    cart = request.session.get('cart', {})

    # Check if the product is already in the cart
    if str(product_id) in cart:
        # If it is, increment the quantity
        cart[str(product_id)]['quantity'] += 1
    else:
        # If it's not, add it to the cart
        cart[str(product_id)] = {
            'name': item.name,
            'price': str(item.price),
            'quantity': 1,
            'image_url': item.image.url,
        }

    # Update the session cart
    request.session['cart'] = cart
    request.session.modified = True

    # Redirect to the cart page
    return redirect('cart')

def add_accessory_to_cart(request, accessory_id):
    # Attempt to find the accessory by ID
    item = Accessories.objects.filter(id=accessory_id).first()

    # If the accessory is not found, redirect to the home page
    if not item:
        return redirect('home')

    # Get the current cart from the session
    cart = request.session.get('cart', {})

    # Check if the accessory is already in the cart
    if str(accessory_id) in cart:
        # If it is, increment the quantity
        cart[str(accessory_id)]['quantity'] += 1
    else:
        # If it's not, add it to the cart
        cart[str(accessory_id)] = {
            'name': item.name,
            'price': str(item.price),
            'quantity': 1,
            'image_url': item.image.url,
        }

    # Update the session cart
    request.session['cart'] = cart
    request.session.modified = True

    # Redirect to the cart page
    return redirect('cart')
