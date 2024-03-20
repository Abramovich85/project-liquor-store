from django.http import Http404, HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from .models import Product

def index_page(request: HttpRequest):
    products = Product.objects.filter(is_active=True)
    return HttpResponse( render(request, 'main.html', {'products': products}))

def products_view(request: HttpRequest):
    products = Product.objects.filter(is_active=True)
    products = products.order_by('-count')

    return HttpResponse(render(request, 'products.html', {
        'products': products
    }))


def product_view(request: HttpRequest, id: int):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404('Товар не найден')

    return HttpResponse(render(request, 'product.html', {
        'product': product
    }))

def add_to_basket_view(request: HttpRequest, id: int):
    request.session['basket'] = request.session.get('basket', []) + [
        {
            'product_id': id,
            'quantity': 1
        }
    ]
    print(request.session['basket'])
    return redirect('products')