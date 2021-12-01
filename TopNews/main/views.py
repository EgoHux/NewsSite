from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Posts, Reporters, Likes, Users, Comments
from django.contrib import auth


def index(request):
    posts = Posts.objects.all()
    return render(request, 'main/index.html', {'title': 'Main Page', 'posts': posts})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    return render(request, 'main/create.html')


def login(request):
    print("start")
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(username = email, password = password)
        print(user)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/news")
    # validate = True
    # if request.method == "POST":
    #     login = request.POST.get('login')
    #     password = request.POST.get('password')
    #     # пользователь не зарегистрирован
    #     # Логин и пароль не валидны
    #     count_user = Users.objects.filter(login = login, password = password)
    #     if not (Users.objects.filter(login = login, password = password)):
    #         validate = False
    #     if (validate == True):
    #         user = Users.objects.filter(login=login, password=password).values()[0]
    #         response = HttpResponseRedirect('news')
    #         response.set_cookie('user', user)
    #         return response

    return render(request, 'registration/login.html')


def list_news(request):
    posts = Posts.objects.all()
    return render(request, 'main/news.html', {'title': 'Main Page', 'posts': posts})


def top_news(request):
    return render(request, 'main/top_news.html')


def news_frame(request, id):
    post = Posts.objects.get(id=id)
    post.viewers += 1
    post.save()
    reporter_obj = Reporters.objects.get(id=post.reporter.id)
    reporter = (reporter_obj.site) if reporter_obj.site != None else reporter_obj.user
    is_site = hasattr(reporter, 'base_url')

    # Запихать сюда кол-во лайков/дизлайков и какой статус у авторизованного пользователя(bool)
    likes = len(Likes.objects.filter(post = post.id, rate = True))
    dislikes = len(Likes.objects.filter(post = post.id, rate = False))
    user_is_rating = False # Получить ID пользователя и узнать какая оценка у авторизованного пользователя к этому посту
    rating = {'likes': likes, 'dislikes': dislikes, 'user_is_rating': user_is_rating}

    comments = Comments.objects.filter(post_id = post.id)

    return render(request, 'main/news_frame.html', {'title': 'title...', 'post': post, 'reporter_info': {'reporter': reporter, 'is_site': is_site}, 'rating': rating, 'comments': comments})


def registration(request):
    if (request.method == 'POST'):
        email = request.POST.get('login')
        username = request.POST.get('nickname')
        age = request.POST.get('age')
        password = request.POST.get('password')
        image = '/static/img/base_profile.svg'

        user = Users.objects.create_user(name=username, password=password, username=email, age=age, image=image)
        user.save()
        print(login)
    return render(request, 'registration/registration.html')
