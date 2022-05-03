from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser , PermissionsMixin):
    email = models.EmailField(max_length=255 , unique=True)
    phone_number = models.CharField(max_length=11 , unique=True)
    full_name = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email' , 'full_name']

    def __str__(self):
        return self.email


    @property
    def is_staff(self):
        return self.is_admin




class otpCode(models.Model):
    '''throwaway code for Registration'''

    phone_number = models.CharField(max_length=11 , unique=True)
    code = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.phone_number} - {self.code} - {self.created_at}'