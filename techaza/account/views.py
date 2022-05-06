from msilib.schema import ListView
from operator import mod
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView
from .forms import UserCreateForm
from django.contrib.auth.models import User

# Create your views here.


class Login(LoginView):
    template_name = "registration/login.html"

    def get_success_url(self):
        messages.success(self.request,"Hey, "+self.request.user.username+"..! Welcome to Techaza...!")
        return reverse_lazy('home')

class Signup(CreateView):
    model = User
    template_name = "registration/signup.html"
    form_class = UserCreateForm
    success_url = reverse_lazy('home')

class Logout(LogoutView):
    next_page = reverse_lazy('login')

    def get_success_url(self):
        messages.success(self.request,"Hi, Buddy..! You have been successfully logged out! Come back soon!")