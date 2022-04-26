from django.shortcuts import render
from django.views import View
from .forms import UserRegisterationForm
# Create your views here.



class SignupView(View):

    form_class = UserRegisterationForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        pass