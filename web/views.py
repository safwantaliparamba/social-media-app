from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    new_posts = []
    for post in posts:
        new_posts.append({
            'post': post,
            'is_liked':True,
        })
    
    for post in new_posts:
        try:
            is_liked = post['post'].likes.get(pk=request.user.author.pk)
        except:
            is_liked = False
        post['is_liked'] = is_liked

    print(new_posts)
    context = {
        'title':'Home page',
        'posts':new_posts
    }
    return render(request,'web/index.html',context)