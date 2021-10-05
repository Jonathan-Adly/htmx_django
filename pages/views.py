from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404

from .models import Blog
import random


def home(request):
    blogs = Blog.objects.all()[:3]
    return render(request, "pages/home.html", {"blogs": blogs})


def blog_3(request):
    all_blogs = list(Blog.objects.all())
    blogs = random.sample(all_blogs, 3)
    return render(request, "pages/blog_list_3.html", {"blogs": blogs})


def blog_list(request):
    all_blogs = Blog.objects.all()
    paginator = Paginator(all_blogs, 10)

    page_number = request.GET.get("page")
    blogs = paginator.get_page(page_number)
    return render(request, "pages/blog_list.html", {"blogs": blogs})


def blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    blog.blog_views += 1
    blog.save()
    return render(request, "pages/blog.html", {"blog": blog})


def tag_search(request, tag):
    all_blogs = Blog.objects.filter(tag=tag)
    paginator = Paginator(all_blogs, 10)

    page_number = request.GET.get("page")
    blogs = paginator.get_page(page_number)
    return render(request, "pages/blog_list.html", {"blogs": blogs})
