from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index_view(request):
    return HttpResponse('<h1>hello this is index page</h1>')


def about_view(request):
    return HttpResponse('<h2>this is about page</h2>')


def contact_view(request):
    return HttpResponse('<h3>this is contact us page</h3>')