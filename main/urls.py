from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_page, name='home'),
    path(
        'basket/', 
        views.basket_view, 
        name='basket'),
    path(
        'basket/clear/', 
        views.basket_clear_view, 
        name='basket_clear'),
    path(
        'search/', 
        views.index_page, 
        name='search'),
    path(
        'order/', 
        views.order_view, 
        name='make_order'),
    path(
        'order/<int:id>/', 
        views.get_order_view, 
        name='get_order'),
    path(
        'order/<int:id>/cancel/', 
        views.cancel_order_view, 
        name='cancel_order'),
    
    path(
        'product/<int:id>/', 
        views.product_view, 
        name='product'),
    path(
        '<slug:category_slug>/', 
        views.index_page, 
        name='products'),
    path(
        'product/<slug:product_slug>/', 
         views.product_view, 
         name='product'),
    path(
        'product/<int:id>/add/', 
        views.basket_add_view, 
        name='add_to_basket'),
    path(
        'product/<int:id>/increase/',
        views.basket_increase_view,
        name='basket_increase'
    ),
    path(
        'product/<int:id>/decrease/',
        views.basket_decrease_view,
        name='basket_decrease'
    ),

]
