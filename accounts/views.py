from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def login_view(request):
    msg = ''
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS,
                                 'Login successful, redirecting to home page...')
            return redirect('/')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Login failed, check your username and password')
    return render(request, 'accounts/login.html')

def logout_view(request):
    return render(request, 'accounts/logout.html')

def register_view(request):
    return render(request, 'accounts/register.html')