from django.urls import path
from .views import blog_view, blog_single, blog_category

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),
    path('category/<str:category_name>', blog_category, name='category'),
]