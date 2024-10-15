from django.urls import path
from . import views

urlpatterns = [
    path('hello/<name>', views.hello, name='hello'),
    path('hello/', views.getuser, name='hello'),
    path('calc/<int:a>/<int:b>', views.calc),
    path('cookie/', views.cookie),
]