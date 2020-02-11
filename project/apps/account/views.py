from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Authentication'
    }
    return render(request, 'account/auth.html', context)
