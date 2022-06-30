from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'title':'Home page',
        'posts':posts
    }
    return render(request,'web/index.html',context)