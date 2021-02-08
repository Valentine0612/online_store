from django.shortcuts import render
from django.http import HttpResponse

from .models import Item

def items_list(request):
    context = {
        'items':Item.objects.all()
    }
    return render(request, 'home.html', context)

def checkout(request):
    return render(request, 'checkout.html')


def product(request):
    return render(request, 'product.html')