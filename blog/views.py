from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category
from django.utils import timezone


def index(request):
    template = 'blog/index.html'
    posts = Post.objects.select_related('category', 'author').filter(pub_date__lte=timezone.now(), is_published=True, category__is_published=True).order_by('-pub_date')[1:6]
    context = {
        'post_list': posts
    }
    return render(request, template, context)


def post_detail(request, pk):
    template = 'blog/post_detail.html'
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category, slug=category_slug, is_published=True)
    posts = Post.objects.all().filter(category=category, is_published=True).order_by('-pub_date')
    context = {'post_list': posts, 'category': category}
    return render(request, template, context)