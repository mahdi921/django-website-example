from django.urls import path
from .views import index_view, about_view, contact_view

app_name = 'testing'

urlpatterns = [
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact')
]