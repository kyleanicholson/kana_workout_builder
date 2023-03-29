from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import EditProfileForm, PasswordChangingForm


# Create your views here.

def change_password(request):
    """Change user password."""
    if request.method != "POST":
        # Display a blank registration form
        form = PasswordChangingForm(request.user)
    else:
        # Process completed form.
        form = PasswordChangingForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("users:password_success")

    context = {"form": form}
    return render(request, "registration/change_password.html", context)

def password_success(request):
    return render(request, "registration/password_success.html", {})

def register(request):
    """Register a new user."""
    if request.method != "POST":
        # Display a blank registration form
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page

            login(request, new_user)
            return redirect("kana_workout_builder_app:index")
    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "registration/register.html", context)

def edit_profile(request):
    """Edit user profile."""

    if request.method != "POST":
        # Display profile edit form
        form = EditProfileForm(instance=request.user)
    else:
        # Process completed form.
        form = EditProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("kana_workout_builder_app:index")
    context = {"form": form}
    return render(request, "registration/edit_profile.html", context)
