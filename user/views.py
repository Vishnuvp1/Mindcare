from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'user/home.html')

def service(request):
    return render(request, 'user/services.html')
