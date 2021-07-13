from django.core.mail import send_mail
from django.conf import settings
from common.models import Email
from django.shortcuts import redirect


def email(subject, message, recipient_list):
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject, message, email_from, recipient_list)


