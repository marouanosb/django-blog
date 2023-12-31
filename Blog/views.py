from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    context = {
        #'title' : 'home',
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title' : 'about'
    }
    return render(request, 'blog/about.html', context)