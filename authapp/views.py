from django.shortcuts import render

# این صفحه ی لاگ این هست 
def login_view(request):
    return render(request , "log_in.html")
# این صفحه ی ساین این است 
def register_view(request):
    return render(request , "register.html")
