from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages
# Create your views here.


class Login(LoginView):
    def get_success_url(self):
        url = self.get_redirect_url()
        messages.success(self.request,"Hey, Buddy..! Welcome to STCS dashboard.")
        return reverse_lazy('home')


class Logout(LogoutView):
    def get_success_url(self):
        messages.success(self.request,"Hi, Buddy..! You have been successfully logged out! Come back soon!")
    next_page = reverse_lazy('login')