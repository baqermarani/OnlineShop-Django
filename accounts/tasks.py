import datetime

from celery import shared_task
from accounts.models import otpCode
from datetime import datetime, timedelta
from pytz import timezone

from utils import send_otp


@shared_task
def send_otp_task(phone, code):
    send_otp(phone_number=phone , code=code)

@shared_task
def remove_otp_task():
    expire_time = datetime.now(tz=timezone('Asia/Tehran')) - timedelta(minutes=2)
    otpCode.objects.filter(created_at__lte=expire_time).delete()