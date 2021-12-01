from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as authViews

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('create', views.create, name='create'),
    path('accounts/login', views.login, name='login'),
    path('exit/', authViews.LogoutView.as_view(next_page='news'), name='exit'),
    path('news', views.list_news, name='news'),
    path('news/top', views.top_news, name='top_news'),
    path('news/<int:id>', views.news_frame, name='news_frame'),
    path('accounts/registration/', views.registration, name='registration'),
    path('profiles/<int:id>', views.profiles, name='profiles'),
    path('news/comments/<int:id>', views.comments, name='comments')
]

# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)