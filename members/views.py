from typing import Any

from django.contrib.auth.views import PasswordChangeView
from django.db import models
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .froms import SignUpForm, EditProfileForm, PasswordChaningForm
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChaningForm
    success_url = reverse_lazy("password_success")


class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"

    success_url = reverse_lazy("login")


class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        Profile()
        return self.request.user


def password_success(request):
    return render(request, "registration/password_success.html")