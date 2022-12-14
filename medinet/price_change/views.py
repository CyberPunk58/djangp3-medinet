from django.shortcuts import render
from .models import Price_change

def price_change(request):
    price_change_info = Price_change.objects.all()
    return render(request, 'price_change/price_change.html', {'price_change':price_change_info})
