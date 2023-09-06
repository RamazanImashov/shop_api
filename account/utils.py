from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_activation_code(email, activation_code):
    context = {
        'text_detail': 'Thank for registretion',
        'email': email,
        'domain': 'http://127.0.0.1:8000/',
        'activation_code': activation_code
    }
    message_html = render_to_string('email.html', context)
    message = strip_tags(message_html)
    send_mail('Activation account',
              message,
              'admin@gmail.com',
              [email],
              html_message=message_html,
              fail_silently=False
              )
