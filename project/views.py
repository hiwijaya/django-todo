
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>This is Home</>')

def about(request):
    return HttpResponse('<h1>DJANGO-TODO</h1>')
