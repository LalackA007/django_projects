from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not username:
            raise ValueError('The Username field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)  # Username field with 50 char max
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Can be used to distinguish staff users

    # Required fields for user creation
    REQUIRED_FIELDS = []  # No additional required fields besides email and username

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Email serves as the unique identifier

    def __str__(self):
        return self.username
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)  # Adjusted username field
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Required fields for create_user
    REQUIRED_FIELDS = []  # No additional required fields

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Email is the unique identifier

    def __str__(self):
        return self.username
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)  # Add username field
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True) 

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Required fields for create_user
    REQUIRED_FIELDS = ['username']  # Specify other fields if necessary

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Email is the unique identifier

    def __str__(self):
        return self.username

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)  # Add username field
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    # Required fields for create_user
    REQUIRED_FIELDS = ['first_name', 'last_name']  # Add any additional required fields here

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Email is the unique identifier

    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', default='products/default.jpg', blank=True, null=True)

    def __str__(self):
        return self.name

class Accessories(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='accessories/', default='accessories/default.jpg', blank=True, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.status}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
