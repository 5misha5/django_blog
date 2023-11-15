from typing import Any

from django.contrib.auth.views import PasswordChangeView
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
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


class ProfilePageView(DetailView):
    model = Profile
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs: Any) -> dict[str, Any]:
        users = Profile.objects.all()
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])
        context["page_user"] = page_user

        return context


class EditProfilePageView(UpdateView):
    model = Profile
    template_name = "registration/edit_profile_page.html"

    fields = ["bio", "profile_pic", "website_url", "facebook_url", "twitter_url", "instagram_url", "pinterest_url"]

    success_url = "home"


def password_success(request):
    return render(request, "registration/password_success.html")
