from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm

# Create your views here.

def blog_view(request, category_name=None, author_username=None, tag_name=None):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if category_name:
        posts = posts.filter(category__name=category_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
    if tag_name:
        posts = posts.filter(tag__name=tag_name)
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog-home.html', context)


def blog_single(request,pid):
    post = get_object_or_404(Post, id=pid, status=1, published_date__lte=timezone.now())
    post.counted_views += 1
    post.save()
    comment = Comment.objects.filter(post=post.id, approved=True).order_by('-created_date')
    other_posts = Post.objects.filter(published_date__lte=timezone.now(), status=1).exclude(id=pid)
    if request.method == 'POST':
        from django.contrib import messages
        form = CommentForm(request.POST)
        if form.is_valid():
            new_instance = form.save(commit=False)
            if new_instance.subject == '':
                new_instance.subject = 'No subject'
            new_instance.post = post
            new_instance.save()
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment has been submitted and is awaiting approval')
        elif form.errors:
            messages.add_message(request, messages.ERROR, 'Your comment didnt go through, check your input')
    form = CommentForm()
    context={
        'post': post,
        'next': other_posts.filter(id__gt=post.id).order_by('id').first(),
        'previous': other_posts.filter(id__lt=post.id).order_by('-id').first(),
        'comments': comment,
        'form': form,
    }
    return render(request, 'blog/blog-single.html', context)

def blog_search(request):
    query = request.GET.get('s')
    posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
    if query:
        posts = posts.filter(content__contains=query)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


# def blog_category(request, category_name):
#     posts = Post.objects.filter(published_date__lte=timezone.now(), status=1)
#     posts = posts.filter(category__name=category_name)
#     context = {'posts': posts}
#     return render(request, 'blog/blog-home.html', context)