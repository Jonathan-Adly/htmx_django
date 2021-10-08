from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage

DEFAULT_FROM_EMAIL = '"Jonathan Adly" <hello@jonathanadly.com>'
REPLY_TO_EMAIL = "hello@jonathanadly.com"


def send_email(subject, message, to):

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
        to,  # to
        # BCC will go here
        reply_to=[REPLY_TO_EMAIL],
    )
    email.content_subtype = "html"
    try:
        email.send()
    except:
        pass
    return None
