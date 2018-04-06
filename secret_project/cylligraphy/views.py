from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    return render(request, 'contact.html')
