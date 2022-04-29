from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render , redirect
from django.utils import timezone
from django.views import View
from .forms import UserRegisterationForm, VerifyCodeForm, UserLoginForm
import random
from utils import send_otp
from .models import otpCode , User
from django.contrib import messages
from . import tasks
# Create your views here.



class SignupView(View):

    form_class = UserRegisterationForm
    template_name = 'accounts/signup.html'

    def get(self, request):

        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000, 9999)
            tasks.send_otp_task.delay(form.cleaned_data['phone'], random_code)
            otpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_code)
            expire_time = timezone.now()
            request.session['user_registration_info'] = {
               'phone_number' : form.cleaned_data['phone'] ,
               'password' : form.cleaned_data['password'],
               'email' : form.cleaned_data['email'],
               'full_name' : form.cleaned_data['full_name'],
               'expire_time' : str(expire_time)
            }
            messages.success(request, 'code sent to your phone number' , 'alert alert-success')
            return redirect('accounts:verify_code')
        return render(request, self.template_name, {'form': form})

class SignUpVerifyCodeView(View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'accounts/verify_code.html', {'form': form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = otpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            if form.cleaned_data['code'] == code_instance.code:
                User.objects.create_user(user_session['phone_number'], user_session['email'],
                                         user_session['full_name'], user_session['password'], )
                code_instance.delete()
                messages.success(request, 'your account has been created successfully' , 'alert alert-success')
                return redirect('home:home')
            else:
                messages.error(request, 'invalid code' , 'alert alert-danger')
                return redirect('accounts:verify_code')

        return redirect('home:home')

class LoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['phone'], password=form.cleaned_data['password'])
            if user is not None:
                user.last_login = timezone.now()
                user.save()
                login(request, user)
                return redirect('home:home')
            else:
                messages.error(request, 'invalid phone number' , 'alert alert-danger')
                return redirect('accounts:login')
        return render(request, self.template_name, {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home:home')