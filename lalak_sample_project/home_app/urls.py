from django.urls import path, include
from . import views

app_name = "home_app"

urlpatterns = [
    path('', views.home, name="home"),
    path('index', views.home, name="home"),
    path('register/', views.register, name='register'),
    path('open_page', views.open_page, name="open_page"),    
    path('closed_page', views.closed_page, name="closed_page"),
]