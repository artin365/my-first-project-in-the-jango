# core/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('list/', views.product_list, name='product_list'),
    path('list/detail/', views.product_detail, name='product_detail'),
]