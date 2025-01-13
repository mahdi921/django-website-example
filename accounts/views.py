from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetCompleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import RegisterForm
from django.urls import reverse_lazy


# Create your views here.

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('accounts:login')

# class ResetDone(PasswordResetCompleteView):
#     template_name = 'accounts/password_reset_complete.html'
#     success_url = reverse_lazy('accounts:login')

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            userinput = request.POST['username']
            try:
                username = User.objects.get(email=userinput).username
            except User.DoesNotExist:
                username = request.POST['username']
            password = request.POST['password']
            data = {'username': username, 'password': password}
            form = AuthenticationForm(request=request, data=data)
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
            data={
                'username' : request.POST.get('username'),
                'email' : request.POST.get('email'),
                'password1' : request.POST.get('password1'),
                'password2' : request.POST.get('password2')
            }
            form = RegisterForm(data=data)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS,
                                     "Registration successful, redirecting to login page...")
                return redirect('/accounts/login')
            else:
                messages.add_message(request, messages.ERROR,
                                     "Check your input and try again")
        form = RegisterForm()
        context = {
            'form' : form
        }
        return render(request, 'accounts/register.html', context)
    else:
        redirect('/')