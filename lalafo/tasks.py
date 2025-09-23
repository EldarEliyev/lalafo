from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_created_elan_email(elan_title):
    send_mail(
        subject="New Created the Elan",
        message=f"New Added the Elan: {elan_title}",
        from_email="eldar6251@gmail.com",
        recipient_list=["liyev7773@gmail.com"],
        fail_silently=False
    )