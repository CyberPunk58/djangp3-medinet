from django.shortcuts import render, get_object_or_404
from.models import News

def home(request):
    news = News.objects.order_by('-date')[:10]
    return render(request, 'news/home.html', {"news":news})

def detail(request, news_id):
    news = get_object_or_404(News, pk = news_id)
    return  render(request, 'news/detail.html', {'news':news})