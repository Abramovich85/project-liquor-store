from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def index_page(request: HttpRequest):
    return render(request, 'index.html')
