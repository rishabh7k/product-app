from django.urls import path
from . import views

# urlpatterns = [
#     path("register/", views.register, name="register"),
#     path("login/", views.login_view, name="login"),
# ]

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("forgot_password/", views.forgot_password, name="forgot_password"),
    path("delete_account/", views.delete_account, name="delete_account"),
]
