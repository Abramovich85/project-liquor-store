from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Product

def index_page(request: HttpRequest):
    products = Product.objects.filter(is_active=True)
    return HttpResponse( render(request, 'main.html', {'products': products}))
