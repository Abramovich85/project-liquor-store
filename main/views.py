from django.http import HttpResponse, HttpRequest
from datetime import datetime
from django.shortcuts import render

def index_page(request: HttpRequest):
    return render(request, 'index.html')
    
def time_view(request: HttpRequest):
    return HttpResponse(datetime.now())

def script_view(request: HttpRequest):
    return HttpResponse('''
        <script>alert("hello")</script>
    ''')