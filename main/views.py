from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .models import Product

def index_page(request: HttpRequest):
    products = Product.objects.all()
    return HttpResponse( render(request, 'index.html', {'products': products}))
