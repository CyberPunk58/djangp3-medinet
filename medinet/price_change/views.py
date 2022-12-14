from django.shortcuts import render

def price_change(request):
    return render(request, 'price_change/price_change.html')
