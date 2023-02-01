from django.urls import path, include
from .views import home, CreateAccountView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import (
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)

urlpatterns = [
    path('' , home , name = 'home') ,
    path('register/', CreateAccountView.as_view(), name='register'),
    path('login/' , LoginView.as_view(template_name = 'users/login.html', next_page = 'home') , name = 'login') ,
    path('logout/' , LogoutView.as_view(template_name = 'users/logout.html') , name = 'logout') ,
    path('password-change/done/' ,
         PasswordChangeDoneView.as_view(template_name = 'users/password-reset-complete.html') , name = 'password_change_done') ,
    path('password-change/request/' ,
         PasswordChangeView.as_view(template_name = 'users/password-reset-confirm.html') , name = 'password_change_request') ,
    path('password-reset/complete/' ,
         PasswordResetCompleteView.as_view(template_name = 'users/password-reset-complete.html') , name = 'password_reset_complete') ,
    path('password-reset/confirm/<uidb64>/<token>/' ,
         PasswordResetConfirmView.as_view(template_name = 'users/password-reset-confirm.html') , name = 'password_reset_confirm') ,
    path('password-reset/done/' ,
         PasswordResetDoneView.as_view(template_name = 'users/password-reset-done.html') , name = 'password_reset_done') ,
    path('password-reset/request/' ,
         PasswordResetView.as_view(template_name = 'users/password-reset-request.html') , name = 'password_reset_request') ,
]
