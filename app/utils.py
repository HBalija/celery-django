from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def send_contact_email(context):

    rendered = render_to_string('email/contact.html', context)
    send_mail(
        subject=settings.CONTACT_SUBJECT,
        message=rendered,
        from_email=context['contact_email'],
        recipient_list=[settings.DEFAULT_FROM_EMAIL],
        fail_silently=False,
        html_message=rendered)
