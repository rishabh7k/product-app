from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm


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
