from django.http import Http404, HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import Product

def get_basket_quantity(request: HttpRequest):
    items = request.session.get('basket', [])

    quantities = sum([item['quantity'] for item in items])

    return quantities
def index_page(request: HttpRequest):
    products = Product.objects.filter(is_active=True)
    products = products.order_by('-count')

    return HttpResponse( render(request, 'main.html', {'products': products, 'quantities': get_basket_quantity(request),
    }))

def get_product_for_view(id: int):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404('Товар не найден')

    if not product.is_active:
        raise Http404('Товар не доступен')

    return product


def product_view(request: HttpRequest, id: int):
    # items = request.session.get('basket', [])

    # quantities = sum([item['quantity'] for item in items])

    return HttpResponse(render(request, 'product.html', {
        'product': get_product_for_view(id=id),
        'quantities': get_basket_quantity(request),
    }))


def add_to_basket_view(request: HttpRequest, id: int):
    product = get_product_for_view(id=id)

    if product.count < 1:
        return redirect('product', id=id)

    basket: list = request.session.get('basket', [])

    found_item = next(
        (item for item in basket if item['product_id'] == id),
        None,
    )

    if found_item is not None:
        found_item['quantity'] = found_item['quantity'] + 1
    else:
        basket.append({
            'product_id': id,
            'quantity': 1
    })

    request.session['basket'] = basket

    return redirect('home')


def basket_view(request: HttpRequest):
    items = request.session.get('basket', [])

    for item in items:
        item['product'] = Product.objects.get(id=item['product_id'])
    
    total_price = sum(item['product'].price * item['quantity']
                      for item in items)

    return HttpResponse(render(request, 'basket.html', {
        'items': items,
        'total_price': total_price,
        'quantities': get_basket_quantity(request),
    }))

def basket_clear_view(request: HttpRequest):
    request.session.update({'basket': []})

    return redirect('basket')