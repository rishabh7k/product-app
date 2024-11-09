from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import (
    CustomUserCreationForm,
    CustomUserAuthenticationForm,
    PasswordResetForm,
)
from .models import CustomUser


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect("login")
        else:
            messages.error(
                request, "Registration failed. Please correct the errors below."
            )
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CustomUserAuthenticationForm


def login_view(request):
    if request.method == "POST":
        form = CustomUserAuthenticationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("product_list")
            else:
                messages.error(request, "Invalid username or password.")
    else:
        form = CustomUserAuthenticationForm()
    return render(request, "users/common_logic.html", {"form": form})


def forgot_password(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            new_password = form.cleaned_data["new_password"]
            try:
                user = CustomUser.objects.get(username=username)
                if user.check_password(new_password):
                    messages.error(
                        request, "New password cannot be the same as the old password."
                    )
                else:
                    user.set_password(new_password)
                    user.save()
                    messages.success(request, "Password updated successfully.")
                    return redirect("login")
            except CustomUser.DoesNotExist:
                messages.error(request, "Username does not exist.")
    else:
        form = PasswordResetForm()
    return render(request, "users/forgot_password.html", {"form": form})


from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, redirect


@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        logout(request)
        messages.success(request, "Your account has been deleted.")
        return redirect("home")
    return render(request, "users/delete_account.html")
