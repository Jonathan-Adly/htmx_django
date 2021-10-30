from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.core import mail


DEFAULT_FROM_EMAIL = '"Jonathan From HTMX/Django" <hello@htmx-django.com>'
REPLY_TO_EMAIL = "hello@htmx-django.com"


def send_email(subject, message, to):
    connection = mail.get_connection()
    connection.open()
    for email in to:
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
            [email],  # to
            connection=connection,
        )
        email.content_subtype = "html"
        email.send()
    connection.close()
    return None
