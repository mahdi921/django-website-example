from django.urls import path
from .views import blog_view, blog_single, blog_search #,blog_category

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),
    path('author/<author_username>', blog_view, name='author'),
    path('search/', blog_search, name='search'),
    path('tag/<str:tag_name>', blog_view, name='tag'),
    path('category/<str:category_name>', blog_view, name='category'),
]