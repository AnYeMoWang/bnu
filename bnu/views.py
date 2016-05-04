from django.shortcuts import render
from apps.trade.models import Trade


def index(request):
    news = Trade.objects.filter(type=1).order_by('-submit_time')[:4]
    notices = Trade.objects.filter(type=2).order_by('-submit_time')[:4]
    trades = Trade.objects.all().order_by('-submit_time')[:4]
    resp = {
        'trades': trades,
        'notices': notices,
        'news': news
    }
    return render(request, 'index.html', resp)
