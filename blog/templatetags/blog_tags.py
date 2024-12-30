from django.utils import timezone
from django import template
from blog.models import Post, Category

register = template.Library()


@register.simple_tag
def views_count():
    pass

@register.inclusion_tag('blog/blog-popular-widget.html')
def popular_posts(arg=4):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).order_by('-counted_views')[:arg]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-category-widget.html')
def categories_widget():
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    category = Category.objects.all()
    category_dict = {}
    for name in category:
        category_dict[name] = posts.filter(category=name).count()
    return {'categories': category_dict}