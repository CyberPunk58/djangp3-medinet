from django.urls import path
from . import views

urlpatterns = [

    path('', views.price_change, name='price_change')

]