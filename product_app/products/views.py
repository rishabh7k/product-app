from django.shortcuts import render, HttpResponse
import requests
from django.views.generic import DetailView

from django.contrib.auth.decorators import login_required

import logging
from django.shortcuts import render
import requests

logger = logging.getLogger(__name__)


def test(request):
    return HttpResponse("yo")


@login_required
def get_products(request):
    """Fetches products and renders them in the template"""
    template = request.GET.get("template", "grid")
    # Check if products are already in session
    products = request.session.get("products")

    if not products:
        # Fetch data from the API
        url = "https://fakerapi.it/api/v2/products?_quantity=10"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            products = data["data"]
            # Store products in session
            request.session["products"] = products
            error = None
        except requests.exceptions.RequestException as e:
            logger.error("API request failed: %s", e)
            products = []
            error = f"An error occurred: {str(e)}"
    else:
        error = None

    context = {"products": products, "template": template, "error": error}
    return render(request, "products/product_list.html", context)


def product_detail(request, product_id):
    """Display detailed product information"""
    url = f"https://fakerapi.it/api/v2/products?_quantity=1"  # In real app, you'd fetch specific product
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        product = data["data"][0]  # For demo, taking first product
        context = {"product": product, "error": None}
    except requests.exceptions.RequestException as e:
        context = {"product": None, "error": f"An error occurred: {str(e)}"}

    return render(request, "products/product_detail.html", context)
