from django.urls import path
from .views import \
    UserRegisterView, \
    UserEditView, \
    PasswordsChangeView, \
    password_success, \
    ProfilePageView, \
    EditProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register", UserRegisterView.as_view(), name="register"),
    path("edit_user", UserEditView.as_view(), name="edit_user"),
    path("password", PasswordsChangeView.as_view(template_name="registration/change-password.html")),
    path("password_success", password_success, name="password_success"),
    path("<int:pk>", ProfilePageView.as_view(), name="profile_page"),
    path("<int:pk>/edit_profile", EditProfilePageView.as_view(), name="edit_profile_page"),
]
