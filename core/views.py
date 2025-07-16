from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# این صفحه ی هوم است 
def home_view(request):
    return render(request , "home.html")


# این صفحه ی لیست محصولات است 
def product_list(request):
    return render(request , "product_list.html")


# این صفحه ی جزیات هر یک از محصولات است 
def product_detail(request):
    return render(request , "product_detail.html")


