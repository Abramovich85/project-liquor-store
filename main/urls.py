from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_page, name='home'),
    path('products/', views.index_page, name='products'),
    path('product/<int:id>/', views.product_view, name='product'),
    path(
        'product/<int:id>/add/',
        views.add_to_basket_view,
        name='add_to_basket'
    ),
    path('basket/', views.basket_view, name='basket'),
]
