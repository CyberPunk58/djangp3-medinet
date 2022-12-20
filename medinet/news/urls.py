from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'news'

urlpatterns = [

    path('', views.home, name='news'),
    path('<int:news_id>', views.detail, name='detail')

]