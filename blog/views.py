from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

# Create your views here.

def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog-home.html', context)


def blog_single(request,pid):
    post = get_object_or_404(Post, id=pid, status=1, published_date__lte=timezone.now())
    post.counted_views += 1
    post.save()
    other_posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).exclude(id=pid)
    
    context={
        'post': post,
        'next': other_posts.filter(id__gt=post.id).order_by('id').first(),
        'previous': other_posts.filter(id__lt=post.id).order_by('-id').first()
    }
    return render(request, 'blog/blog-single.html', context)


def blog_category(request, category_name):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    posts = posts.filter(category__name=category_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)