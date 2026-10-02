from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.


class SignUpForm(CreateView):
    form_class = RegisterForm
    model = User
    fields = ['username', 'first_name', 'last_name']
    template_name = 'registration/signup.html'