from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from blog_main import settings
from blogs.models import Blog, Category


def posts_by_category(request, category_id):

    posts = Blog.objects.filter(status='Published', category=category_id)
    if settings.DEBUG:
        try:
            category = Category.objects.get(pk=category_id)
        except Category.DoesNotExist:
            return render(request, '404.html')
    else:
        category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)

def blogs(request, slug):
    if settings.DEBUG:
        try:
            single_blog = Blog.objects.get(slug=slug)
        except:
            return render(request, '404.html')
    else:
        single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context ={
        'single_blog': single_blog,
    }
    return render(request, 'blogs.html', context)
