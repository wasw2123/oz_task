from django.core.mail import EmailMessage


def send_email(subject: str, message: str, to_email: str | list[str]):
    email = EmailMessage(subject, message, to=to_email)
    email.content_subtype = 'html'
    return email.send()
