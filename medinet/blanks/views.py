from django.shortcuts import render
from .models import Blanks

def blanks(request):
    blanks= Blanks.objects.order_by('-date')
    return render(request, 'blanks/blanks.html', {'blanks':blanks})