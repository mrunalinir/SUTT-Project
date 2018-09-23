from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import News
from django.contrib import auth
from django.utils import timezone
from django.contrib.auth.models import User

def home(request):
    return render(request, 'news/home.html')

@login_required
def newsfeed(request):
    news = News.objects
    return render(request,'news/newsfeed.html',{'news':news})


@login_required (login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['image']:
            news = News()
            news.title = request.POST['title']
            news.body = request.POST['body']
            news.image = request.FILES['image']
            news.pub_date = timezone.datetime.now()
            news.source = request.user
            news.save()
            return redirect('/news/' + str(news.id))
        else:
            return render(request, 'news/create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'news/create.html')

@login_required
def detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news/detail.html',{'newzz':news})



