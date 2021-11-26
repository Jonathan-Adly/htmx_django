import random

from datetime import datetime

from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.cache import never_cache

from .models import Blog, Subscriber
from config.utils import send_email


def home(request):
    blogs = Blog.objects.filter(draft=False)[:3]
    if request.method == "POST":
        if "email" in request.POST:
            email = request.POST["email"].lower()
            sub = Subscriber(email=email)
            sub.save()
            subject = "Thanks for subscribing!"
            message = "<p> Thank you for signing up! You will start receiving updates shortly with no further action. </p> Jonathan Adly </p> <p> P.S. If you need to get in touch with me, just respond to this email. </p>"
            send_email(subject, message, [email])
            return render(request, "components/success.html", {"success": True})
        else:
            return render(request, "components/success.html", {"success": False})

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
    all_blogs = list(Blog.objects.filter(draft=False))
    blogs = random.sample(all_blogs, 3)
    return render(request, "pages/blog_list_3.html", {"blogs": blogs})


def blog_list(request):
    all_blogs = Blog.objects.filter(draft=False, course=False)
    paginator = Paginator(all_blogs, 10)

    page_number = request.GET.get("page")
    blogs = paginator.get_page(page_number)
    return render(request, "pages/blog_list.html", {"blogs": blogs})


@never_cache
def blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if not blog.draft:
        blog.blog_views += 1
        blog.save()
    return render(request, "pages/blog.html", {"blog": blog, "tldr": False})


def tag_search(request, tag):
    all_blogs = Blog.objects.filter(draft=False, tag=tag)
    paginator = Paginator(all_blogs, 10)

    page_number = request.GET.get("page")
    blogs = paginator.get_page(page_number)
    return render(request, "pages/blog_list.html", {"blogs": blogs})


def course_landing_page(request):
    projects = Blog.objects.filter(draft=False, course=True).order_by("timestamp")
    return render(request, "pages/course_landing_page.html", {"projects": projects})


def time_difference(request):
    delta = datetime(2022, 12, 1, tzinfo=timezone.utc) - timezone.now()
    return render(
        request,
        "components/time_difference.html",
        {
            "days": delta.days,
            "seconds": delta.seconds % 60,
            "minutes": (delta.seconds // 60) % 60,
            "hours": delta.seconds // 3600,
        },
    )


def draft_list(request):
    drafts = Blog.objects.filter(draft=True)
    paginator = Paginator(drafts, 10)

    page_number = request.GET.get("page")
    blogs = paginator.get_page(page_number)
    return render(request, "pages/blog_list.html", {"blogs": blogs})
