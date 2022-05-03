from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self , phone_number, email , full_name ,password):
        """Creates and saves a new user"""

        if not phone_number:
            raise ValueError('Users must have an phone number')

        if not email:
            raise ValueError('Users must have an email address')

        if not full_name:
            raise ValueError('Users must have an full name')

        user = self.model(phone_number=phone_number, email=self.normalize_email(email), full_name=full_name)
        user.set_password(password)
        user.save(using=self._db) # use Active Database


        return user

    def create_superuser(self, phone_number, email, full_name, password):
        """Creates and saves a new superuser"""

        user = self.create_user(phone_number, email, full_name, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)

        return user