from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as authlogin, logout as authlogout
from django.urls import reverse

# Create your views here.
def signin(request):
    user = None
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
        except Exception as e:
            error_message = str(e)

    return render(request, 'signin.html', {"user": user, "error_message": error_message})

def user_login(request):  # Renamed to avoid conflict with imported login
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            authlogin(request, user)
            return redirect('Product_list')  # Corrected redirect usage
        else:
            error_message = 'Invalid credentials'
    return render(request, 'login.html', {'error_message': error_message})

def user_logout(request):  # Renamed to avoid conflict with imported logout
    authlogout(request)
    return redirect('login')
