# user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("signin/", views.signin, name="signin"),
]
