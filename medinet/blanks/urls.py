from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blanks'

urlpatterns = [

    path('', views.blanks, name='blanks'),
    #path('<int:price_change_id>', views.detail, name='detail')

]