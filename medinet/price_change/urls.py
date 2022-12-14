from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'price_change'

urlpatterns = [

    path('', views.price_change, name='price_change'),
    path('<int:price_change_id>', views.detail, name='detail')

]