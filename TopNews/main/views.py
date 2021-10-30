from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def create(request):
    return render(request, 'main/create.html')


def login(request):
    return render(request, 'main/login.html')


def list_news(request):
    return render(request, 'main/list_news.html')


def top_news(request):
    return render(request, 'main/top_news.html')


def news_frame(request):
    return render(request, 'main/news_frame.html')
