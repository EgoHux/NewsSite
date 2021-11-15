from django.shortcuts import render
from django.http import HttpResponse
from . models import Posts


def index(request):
    posts = Posts.objects.all()
    return render(request, 'main/index.html', {'title': 'Main Page', 'posts': posts})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    return render(request, 'main/create.html')


def login(request):
    return render(request, 'main/login.html')


def list_news(request):
    posts = Posts.objects.all()
    return render(request, 'main/news_list.html', {'title': 'Main Page', 'posts': posts})


def top_news(request):
    return render(request, 'main/top_news.html')


def news_frame(request):
    return render(request, 'main/news_frame.html')


def registration(request):
    return render(request, 'main/registration.html')
