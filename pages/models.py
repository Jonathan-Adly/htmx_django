from django.db import models
from django.urls import reverse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from config.utils import send_email

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
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    main_img = models.ImageField(upload_to="blogimages/", blank=True)
    tag = models.CharField(max_length=50, default="django-htmx")
    blog_views = models.IntegerField(default=0)
    draft = models.BooleanField(default=True)
    course = models.BooleanField(default=False)

    class Meta:
        ordering = ["-timestamp", "-updated"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog", kwargs={"slug": self.slug})

    def send(self, request):
        subscribers = Subscriber.objects.all()
        to = []
        message = (
            "<p> Hi there, </p> <p> I just published a new article:"
            f"<a href='https://htmx-django.com{self.get_absolute_url()}'> {self.title} </a>."
            " Check it out and as always, I am happy to hear your feedback. Just respond to this email</p>"
            "<p> Thanks! </p>"
            "<p> Jonathan Adly </p>"
        )
        for sub in subscribers:
            to.append(sub.email)

        send_email(self.title, message, to)


class SubscriberMessage(models.Model):
    subject = models.CharField(max_length=150)
    content = RichTextUploadingField()

    def __str__(self):
        return self.subject

    def send(self, request):
        subscribers = Subscriber.objects.all()
        to = []
        for sub in subscribers:
            to.append(sub.email)

        send_email(self.subject, self.content, to)
