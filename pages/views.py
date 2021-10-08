from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.views.decorators.http import require_http_methods

from .models import Blog, Subscriber
from config.utils import send_email
import random


def home(request):
    blogs = Blog.objects.all()[:3]
    if request.method == "POST":
        email = request.POST["email"].lower()
        sub = Subscriber(email=email)
        sub.save()
        subject = "Thanks for subscribing!"
        message = "<p> Thank you for signing up! You will start receiving updates shortly with no further action. </p> Jonathan Adly </p> <p> P.S. If you need to get in touch with me, just respond to this email. </p>"
        send_email(subject, message, [email])
        return render(request, "components/success.html")

    return render(request, "pages/home.html", {"blogs": blogs})


def validate_email_view(request):
    errors = None
    email = None
    if request.method == "POST":
        email = request.POST["email"]
        try:
            validate_email(email)
        except ValidationError as e:
            errors = e
        if Subscriber.objects.filter(email__iexact=email).exists():
            errors = ["Email already exists"]

    return render(
        request, "components/subscribe_box.html", {"errors": errors, "email": email}
    )


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
