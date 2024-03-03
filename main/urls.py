from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('time/', views.time_view, name='time'),
    path('script/', views.script_view, name='script'),
]