from django.http import HttpResponse, HttpRequest
from datetime import datetime

def home(request: HttpRequest):
    return HttpResponse(f'''
        <h1>Hello!</h1>
    ''')
# return HttpResponse(render(request, 'index.html', {}))
    
def time_view(request: HttpRequest):
    return HttpResponse(datetime.now())

def script_view(request: HttpRequest):
    return HttpResponse('''
        <script>alert("hello")</script>
    ''')