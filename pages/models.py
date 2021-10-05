from django.db import models

from django.urls import reverse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribe = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class Blog(models.Model):

    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    content = RichTextUploadingField()
    notes = RichTextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    main_img = models.ImageField(upload_to="blogimages/", blank=True)
    tag = models.CharField(max_length=50, default="blogging")
    blog_views = models.IntegerField(default=0)

    class Meta:
        ordering = ["-timestamp", "-updated"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog", kwargs={"slug": self.slug})

    def send(self, request):
        subscribers = Subscriber.objects.all()
        email_list = []
        html_template = "email/email_base.html"
        html_message = render_to_string(
            html_template,
            {
                "context": self.content,
            },
        )
        for sub in subscribers:
            email_list.append(sub.email)

        email = EmailMessage(
            self.title,
            html_message,
            "gadly0123@gmail.com",
            ["gadly0123@gmail.com"],
            email_list,
        )
        email.content_subtype = "html"
        email.send()
