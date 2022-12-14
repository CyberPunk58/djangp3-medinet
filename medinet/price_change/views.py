from django.shortcuts import render, get_object_or_404
from .models import Price_change

def price_change(request):
    price_change_info = Price_change.objects.order_by('-date')[:10]
    return render(request, 'price_change/price_change.html', {'price_change':price_change_info})


def detail(request, price_change_id):
    price_change_detail = get_object_or_404(Price_change, pk = price_change_id)
    return  render(request, 'price_change/detail.html', {'price_change':price_change_detail})