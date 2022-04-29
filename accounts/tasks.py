from celery import shared_task
from utils import send_otp


@shared_task
def send_otp_task(phone, code):
    send_otp(phone_number=phone , code=code)