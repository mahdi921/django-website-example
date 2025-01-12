from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required

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
                messages.add_message(request, messages.ERROR,
                                     'Check your input and try again')
        else:
            form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
    else:
        messages.add_message(request, messages.ERROR,
                             "You are already logged in, redirecting to home page...")
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS,
                        "You have been logged out, redirecting to home page...")
    return redirect('/')

def register_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,
                                     "Registration successful, redirecting to login page...")
                return redirect('/accounts/login')
            else:
                messages.add_message(request, messages.ERROR,
                                     "Check your input and try again")
        form = UserCreationForm()
        context = {
            'form' : form
        }
        return render(request, 'accounts/register.html', context)
    else:
        redirect('/')