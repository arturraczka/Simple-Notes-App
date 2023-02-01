from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import home, CreateAccountView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import (
    PasswordChangeDoneView,
    PasswordChangeView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)

class TestUrls(SimpleTestCase):

    token = 'testtoken'
    uidb64 = 'testuidb'

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_create_account_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, CreateAccountView)

    def test_user_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_user_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_password_change_done_url_resolves(self):
        url = reverse('password_change_done')
        self.assertEquals(resolve(url).func.view_class, PasswordChangeDoneView)

    def test_password_change_request_url_resolves(self):
        url = reverse('password_change_request')
        self.assertEquals(resolve(url).func.view_class, PasswordChangeView)

    def test_password_change_complete_url_resolves(self):
        url = reverse('password_reset_complete')
        self.assertEquals(resolve(url).func.view_class, PasswordResetCompleteView)

    def test_password_reset_done_url_resolves(self):
        url = reverse('password_reset_done')
        self.assertEquals(resolve(url).func.view_class, PasswordResetDoneView)

    def test_password_reset_request_url_resolves(self):
        url = reverse('password_reset_request')
        self.assertEquals(resolve(url).func.view_class, PasswordResetView)

    def test_password_reset_confirm_url_resolves(self):
        url = reverse('password_reset_confirm', kwargs = {'token': self.token, 'uidb64': self.uidb64})
        self.assertEquals(resolve(url).func.view_class, PasswordResetConfirmView)
