from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS,
                                         'Login successful, redirecting to home page...')
                    return redirect('/')

        else:
            form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
    else:
        messages.add_message(request, messages.ERROR,
                             "You are already logged in, redirecting to home page...")
        return redirect('/')


def logout_view(request):
    return render(request, 'accounts/logout.html')

def register_view(request):
    return render(request, 'accounts/register.html')