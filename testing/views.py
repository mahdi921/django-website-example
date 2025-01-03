from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from testing.models import Contact
from testing.forms import ContactForm

def index_view(request):
    return render(request, 'testing/index.html')


def about_view(request):
    return render(request, 'testing/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
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