from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import requests


# Create your views here.
def test(request):
    return HttpResponse("yo")


def get_products(request):
    """
    Fetches product data from the Faker API and returns the response.
    """
    url = "https://fakerapi.it/api/v2/products?_quantity=10&_taxes=12&_categories_type=uuid"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return JsonResponse(data)  # Return the JSON data if successful
    except requests.exceptions.RequestException as e:
        # Handle errors gracefully, e.g., log the error and return a user-friendly message
        return {"error": f"An error occurred: {str(e)}"}
