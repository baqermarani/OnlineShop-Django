from django.core.management.base import BaseCommand
from accounts.models import otpCode
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Remove expired OTP codes'

    def handle(self, *args, **options):
        expire_time = datetime.now() - timedelta(minutes=2)
        # Get all OTP codes that are expired and Delete them
        otpCode.objects.filter(created_at__lte=expire_time).delete()
        self.stdout.write(self.style.SUCCESS('Successfully removed expired OTP codes'))
