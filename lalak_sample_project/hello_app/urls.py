from django.urls import path
from . import views

urlpatterns = [
    path('hello/<str:name>', views.hello),
    path('hello/', views.getuser, name='hello'),
    path('calc/<int:a>/<int:b>', views.calc),
    path('cookie/', views.cookie),
]