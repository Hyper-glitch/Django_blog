from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'mr.Smirnov',
        'title': 'Blog post 1',
        'content': 'First post content',
        'data_posted': 'August 29, 2021'
    },
    {
        'author': 'mr.Twister',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'data_posted': 'August 30, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
