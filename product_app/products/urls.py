from django.urls import path
from . import views

urlpatterns = [
    path("test", views.test, name="test"),
    path("get", views.get_products, name="get_products"),
]
