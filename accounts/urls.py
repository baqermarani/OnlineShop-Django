from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='user_signup'),
    path('verify/', views.SignUpVerifyCodeView.as_view(), name='verify_code'),
    path('login/', views.LoginView.as_view(), name='user_login'),
]