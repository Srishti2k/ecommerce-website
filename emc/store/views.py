from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def store(request):
    return render(request , 'store/store.html')

def cart(request):
    return render(request , 'store/cart.html')

def checkout(request):
    return render(request, 'store/checkout.html')