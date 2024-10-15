from django.urls import path
from . import views

urlpatterns = [
    path('showgame/', views.showgame),
    path('', views.home),
]
