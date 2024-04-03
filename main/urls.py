from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_page, name='home'),
    path('basket/', views.basket_view, name='basket'),
    path('basket/clear/', views.basket_clear_view, name='basket_clear'),
    path('order/', views.order_view, name='order'),
    path('product/<int:id>/', views.product_view, name='product'),
    path('<slug:category_slug>/', views.index_page, name='products'),
    path('<slug:category_slug>/<int:page>/', views.index_page, name='products'),
    path('product/<slug:product_slug>/', views.product_view, name='product'),
    path('product/<int:id>/add/', views.add_to_basket_view, name='add_to_basket'),

]
