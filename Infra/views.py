from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('register')  # Redirect to register view
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('register')  # Redirect to register view
            else:
                User.objects.create_user(username=username, email=email, password=password1)
                messages.success(request, 'User created successfully')
                return redirect('login')  # Redirect to login view
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')  # Redirect to register view

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')  # Redirect to home view
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')  # Redirect to login view

    return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')
