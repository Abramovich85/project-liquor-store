from django.core.paginator import Paginator
from django.http import Http404, HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import Product, Categories

def get_basket_quantity(request: HttpRequest):
    items = request.session.get('basket', [])

    quantities = sum([item['quantity'] for item in items])

    return quantities
def index_page(request: HttpRequest,category_slug='all', page=1):

    title_text = Categories.objects.get(slug=category_slug).name

    if category_slug == 'all':
        products = Product.objects.filter(is_active=True)
        products = products.order_by('-count')
    else:
        products = Product.objects.filter(category__slug=category_slug, is_active=True)
        products = products.order_by('-count')

    paginator = Paginator(products, 8)
    current_page = paginator.page(page)

    context = {
        'products': current_page,
        'quantities': get_basket_quantity(request),
        'title_text': title_text,
        'slug_url': category_slug
    }

    return HttpResponse( render(request, 'main.html', context))

def get_product_for_view(id: int):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404('Товар не найден')

    if not product.is_active:
        raise Http404('Товар не доступен')

    return product


def product_view(request: HttpRequest, id=False, product_slug=False):

    if id:
        product = get_product_for_view(id=id)
    else:
        product = Product.objects.get(slug=product_slug)

    if not product.is_active:
        raise Http404('Товар не доступен')
    return HttpResponse(render(request, 'product.html', {
        'product': product,
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


def basket_view(request: HttpRequest,):
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

def order_view(request: HttpRequest):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            login_page = redirect('login')
            login_page['Location'] += '?next=/order'
            return login_page

        basket_items = request.session.get('basket', [])

        if len(basket_items) < 1:
            return redirect('basket')

        basket_products_ids = [item['product_id'] for item in basket_items]
        basket_products = Product.objects.filter(id__in=basket_products_ids)

        for item in basket_items:
            item['product'] = basket_products.get(id=item['product_id'])

        basket_sum = sum(item['product'].price * item['quantity']
                         for item in basket_items)

        return HttpResponse(render(request, 'order.html', {
            'order_sum': basket_sum,
            'products': basket_items,
        }))