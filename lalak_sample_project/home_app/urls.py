from django.urls import path, include
from . import views

app_name = "home_app"

urlpatterns = [
    path('', views.home, name="home"),
    path('index', views.home, name="home"),
    path('register/', views.register, name='register'),
    path('open_page', views.open_page, name="open_page"),    
<<<<<<< HEAD
    path('account/edit', views.edit, name='edit'),   
=======
>>>>>>> 00c691414f1328b5762828267d913cdb8ad70007
    path('closed_page', views.closed_page, name="closed_page"),
    path('blog', include('blog_app.urls')),
]