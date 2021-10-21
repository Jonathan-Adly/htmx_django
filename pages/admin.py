from django.contrib import admin
from .models import Subscriber, Blog, SubscriberMessage, Project, Chapter, Section


def send_email_update(modeladmin, request, queryset):
    for email_update in queryset:
        email_update.send(request)


send_email_update.short_description = "Announce selected Newsletters to all subscribers"


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "blog_views",
    )
    prepopulated_fields = {"slug": ("title",)}
    actions = [send_email_update]


class SubscriberMessageAdmin(admin.ModelAdmin):
    actions = [send_email_update]


admin.site.register(Subscriber)
admin.site.register(Blog, BlogAdmin)
admin.site.register(SubscriberMessage, SubscriberMessageAdmin)
admin.site.register(Project)
admin.site.register(Chapter)
admin.site.register(Section)
