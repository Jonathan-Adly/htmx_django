from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # new
from django.conf.urls.static import static

urlpatterns = [
    path("theojoy/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("", include("pages.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
