from django.urls import path
from . import views

# urlpatterns = [
#     path("test", views.test, name="test"),
#     path("products", views.get_products, name="product_list"),
#     path("products/<int:product_id>/", views.product_detail, name="product_detail"),
# ]

urlpatterns = [
    path("", views.get_products, name="product_list"),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
]
