from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('create', views.create, name='create'),
    path('login', views.login, name='login'),
    path('list_news', views.list_news, name='list_news'),
    path('top_news', views.top_news, name='top_news'),
    path('news_frame', views.news_frame, name='news_frame'),
]
