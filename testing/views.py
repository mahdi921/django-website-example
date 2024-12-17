from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index_view(request):
    return render(request, 'testing/index.html')


def about_view(request):
    return render(request, 'testing/about.html')


def contact_view(request):
    return render(request, 'testing/contact.html')