from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Posts, Reporters, Likes, Users, Comments, Review
from django.contrib import auth
from time import gmtime, strftime

def index(request):
    posts = Posts.objects.all()
    return render(request, 'main/index.html', {'title': 'Main Page', 'posts': posts})

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(username = email, password = password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/news")

    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/news")

def list_news(request):
    posts = Posts.objects.all()
    return render(request, 'main/news.html', {'title': 'Main Page', 'posts': posts})

def top_news(request):
    posts = Posts.objects.order_by('-viewers')
    return render(request, 'main/news.html', {'title': 'FFF Page', 'posts': posts})

def search(request):
    key = request.GET.get('key')
    posts = Posts.objects.filter(title__contains=key)
    return render(request, 'main/news.html', {'title': 'FFF Page', 'posts': posts})

def news_frame(request, id):
    post = Posts.objects.get(id=id)
    user = request.user
    if user.is_authenticated:
        if not (Review.objects.filter(user = user.id, post = id).exists()):
            review = Review.objects.create(user = user, post = post)
            #print(review.__dict__)
            review.save()
            post.viewers += 1
            post.save()
        
    reporter_obj = Reporters.objects.get(id=post.reporter.id)
    reporter = (reporter_obj.site) if reporter_obj.site != None else reporter_obj.user
    is_site = hasattr(reporter, 'base_url')

    if user.is_authenticated:
        record = Likes.objects.filter(post = post, user = user)
        if (record.exists()):
            rating = record[0].rate
        else:
            rating = None
    else:
        rating = None
   

    print("Rating: {}".format(rating))

    comments = Comments.objects.filter(post_id = post.id)

    return render(request, 'main/news_frame.html', {'post': post, 'reporter_info': {'reporter': reporter, 'is_site': is_site}, 'rating': rating, 'comments': comments})

def registration(request):
    if (request.method == 'POST'):
        email = request.POST.get('login')
        username = request.POST.get('nickname')
        age = request.POST.get('age')
        password = request.POST.get('password')
        image = '/static/img/base_profile.svg'

        user = Users.objects.create_user(name=username, password=password, username=email, age=age, image=image)
        user.save()

        auth.login(request, user)
        return HttpResponseRedirect("/news")

    return render(request, 'registration/registration.html')

def profiles(request, id):
    if request.method == 'GET':
        user = Users.objects.get(id=id)
        return render(request, 'main/profiles.html', {'usr': user})
    if request.method == 'POST':
        return "true"

def comments(request, id):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        message = request.POST.get('message')
        datetime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        user = None
        post = None

        if user_id:
            user = Users.objects.get(id=user_id)
        if id:
            post = Posts.objects.get(id=id)

        comment = Comments(user = user, post = post, date = datetime, text = message )
        comment.save()

        redirect_url = "/news/"+id.__str__()
    return HttpResponseRedirect(redirect_url)

def set_likes(request, id):
    user = request.user
    post = Posts.objects.get(id=id)

    record = Likes.objects.filter(post = post, user = user)

    like = None
    if not (record.exists()):
        like = Likes(post = post, user = user, rate = True)
    else:
        like = record[0]
        like.rate = True
        post.dislike -= 1

    post.like += 1
    like.save()
    post.save()

    redirect_url = "/news/"+id.__str__()
    return HttpResponseRedirect(redirect_url)

def set_dislikes(request, id):
    user = request.user
    post = Posts.objects.get(id=id)

    record = Likes.objects.filter(post = post, user = user)

    dislike = None
    if not (record.exists()):
        dislike = Likes(post = post, user = user, rate = False)
    else:
        dislike = record[0]
        dislike.rate = False
        post.like -= 1
    
    post.dislike += 1
    dislike.save()
    post.save()

    redirect_url = "/news/"+id.__str__()
    return HttpResponseRedirect(redirect_url)
