from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import CreateAccountForm


def home(request):
    return render(request = request, template_name = 'users/home.html')


class CreateAccountView(SuccessMessageMixin, CreateView):
    template_name = 'users/register.html'
    form_class = CreateAccountForm
    success_message = "Your account has been created. You can log in now."
    success_url = reverse_lazy('login')
