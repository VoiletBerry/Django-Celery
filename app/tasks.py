from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from root import settings

@shared_task(bind=True)
def test_func(self):
    # Operations
    for i in range(10):
        print(i)
    return 'Done Task'

@shared_task(bind=True)
def send_reminder_mail(self):
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Celery Testing"
        message = " You leacture is scheduled 24 hours from now. Its a reminder"
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True
        )
    return "Remined Mail Sent"