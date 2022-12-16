from django.shortcuts import render
from .models import Contacts

def contacts(request):
    contacts = Contacts.objects.all
    return render(request, 'contacts/contacts.html', {'contacts': contacts})