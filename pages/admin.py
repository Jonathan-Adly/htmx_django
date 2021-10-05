from django.contrib import admin
from .models import Subscriber, Blog


def send_email_update(modeladmin, request, queryset):
    for email_update in queryset:
        email_update.send(request)


send_email_update.short_description = "Send selected Newsletters to all subscribers"


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "timestamp",
    )
    prepopulated_fields = {"slug": ("title",)}
    actions = [send_email_update]


admin.site.register(Subscriber)
admin.site.register(Blog, BlogAdmin)
