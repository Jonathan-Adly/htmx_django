from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage

DEFAULT_FROM_EMAIL = '"Jonathan From HTMX/Django" <hello@htmx-django.com>'
REPLY_TO_EMAIL = "hello@htmx-django.com"


def send_email(subject, message, to):
    for i in range(0, len(to), 50):
        chunk = to[i : i + 50]
        html_template = "email/email_base.html"
        html_message = render_to_string(
            html_template,
            {
                "context": message,
            },
        )
        email = EmailMessage(
            subject,
            html_message,
            DEFAULT_FROM_EMAIL,  # from
            [REPLY_TO_EMAIL],  # to
            chunk,  # BCC will go here
            reply_to=[REPLY_TO_EMAIL],
        )
        email.content_subtype = "html"
        email.send()

    return None
