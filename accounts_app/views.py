from django.shortcuts import render
from django.views.generic import CreateView
from .forms import Creation_user,Update_user
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your views here.



class SignUpForm(CreateView):
    form_class = Creation_user
    model = User
    template_name = "registration/signup.html"
    success_url = reverse_lazy('login')