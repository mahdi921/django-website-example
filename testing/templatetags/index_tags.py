from django.utils import timezone
from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('testing/index-recent-posts.html')
def index_posts():
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).order_by('-published_date')[:6]
    print(posts)
    return {'posts': posts}