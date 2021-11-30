from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('create', views.create, name='create'),
    path('login', views.login, name='login'),
    path('news', views.list_news, name='news'),
    path('news/top', views.top_news, name='top_news'),
    path('news/<int:id>', views.news_frame, name='news_frame'),
    path('registration', views.registration, name='registration'),
]

# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



