"""Defines URL patterns for users"""

from django.urls import path, include
from . import views

app_name = "users"

urlpatterns = [
    # Include default auth urls.
    path("", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("change_password/", views.change_password, name="change_password"),
    path("password_success/", views.password_success, name="password_success"),
]
