from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('create', views.create, name='create'),
    path('login', views.login, name='login'),
    path('news_list', views.list_news, name='news_list'),
    path('top_news', views.top_news, name='top_news'),
    path('news_frame', views.news_frame, name='news_frame'),
    path('registration', views.registration, name='registration'),
]
