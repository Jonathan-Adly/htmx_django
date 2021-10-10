from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blog-3", views.blog_3, name="blog_3"),
    path("blog-list", views.blog_list, name="blog_list"),
    path("blog/<slug:slug>", views.blog, name="blog"),
    path("validate-email", views.validate_email_view, name="validate_email"),
    path("blog/search/<str:tag>", views.tag_search, name="tag_search"),
    path("course-landing-page", views.course_landing_page, name="landing_page"),
]
