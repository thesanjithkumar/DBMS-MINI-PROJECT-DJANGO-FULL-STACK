from django.contrib.auth import login, logout
from django.views.generic import CreateView
from . import forms
from django.urls import reverse_lazy


# Create your views here.


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('user:login')
    template_name = "user/signup.html"
