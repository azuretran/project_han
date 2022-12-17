from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def store(request):
    return render(request,'store.html')
def checkout(request):
    return render(request, 'checkout.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def index(request):
    return render(request, 'index.html')
def product(request):
    products=Product.objects.all()
    return render(request, 'product.html',{'products':products})
def services(request):
    return render(request, 'service.html')
def single(request):
    return render(request, 'single.html')