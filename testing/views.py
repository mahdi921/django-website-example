from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from testing.forms import ContactForm, NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'testing/index.html')


def about_view(request):
    return render(request, 'testing/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            new_instance = form.save(commit=False)
            new_instance.name = 'Anonymous'
            new_instance.save()
            form.save()
            human = True
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent')
        elif form.errors:
            messages.add_message(request, messages.ERROR, 'Your message has not been sent, check your input')
    form = ContactForm()
    return render(request, 'testing/contact.html', {'form':form})


def form_test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Form submitted successfully')
        else:
            return HttpResponse('Form is not valid')
    else:
        form = ContactForm()
    return render(request, 'testing/form-test.html', {'form':form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')