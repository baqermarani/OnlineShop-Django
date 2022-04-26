from django import forms
from .models import User, otpCode
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    """Form for creating a new user in Admin panel."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone_number', 'email', 'full_name')

    # """ Validator For Password """
    def clean_password2(self):
        clean_data = self.cleaned_data

        if clean_data['password1'] and clean_data['password2'] and clean_data['password1'] != clean_data['password2']:
            raise ValidationError('Passwords do not match')
        return clean_data['password2']
    # Save User
    def save(self , commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    """Form for updating a user in Admin panel."""
    password =ReadOnlyPasswordHashField(
        help_text="""Raw passwords are not stored,
         so there is no way to see this user's password, but you can change the password using <a href=\"../password/\">this form</a>.""")

    class Meta:
        model = User
        fields = ('phone_number', 'email', 'full_name' , 'password' , 'last_login')




class UserRegisterationForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(label='Full Name')
    phone = forms.CharField(label='Phone Number' , max_length=11)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email Already Exists')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if User.objects.filter(phone_number=phone).exists():
            raise ValidationError('Phone Number Already Exists')
        otpCode.objects.filter(phone_number=phone).delete()
        return phone





class VerifyCodeForm(forms.Form):
    code = forms.IntegerField(label='Verification Code')
