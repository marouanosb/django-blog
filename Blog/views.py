from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        'author': 'Merouane',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date': '25/12/2023'
     },
     {
        'author': 'Merouane',
        'title': 'Blog post 2',
        'content': '2nd post content',
        'date': '24/12/2023'
     },
     {
        'author': 'Amine',
        'title': 'Blog post 3',
        'content': '3rd post content',
        'date': '23/12/2023'
     },
     {
        'author': 'Hamid',
        'title': 'Blog post 4',
        'content': '4th post content',
        'date': '22/12/2023'
     }
]

def home(request):
    context = {
        #'title' : 'home',
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title' : 'about'
    }
    return render(request, 'blog/about.html', context)