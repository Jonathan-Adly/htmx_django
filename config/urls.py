from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import TemplateView
from pages.models import Blog


urlpatterns = [
    path("theojoy/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path("", include("pages.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
