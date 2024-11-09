from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm


@csrf_protect
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")  # Replace with your home view name
    else:
        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})


@csrf_protect
def signin(request):
    if request.method == "POST":
        form = CustomUserAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")  # Replace with your home view name
    else:
        form = CustomUserAuthenticationForm()
    return render(request, "users/login.html", {"form": form})
