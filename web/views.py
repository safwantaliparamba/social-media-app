from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from posts.models import Post

# Create your views here.
@login_required(login_url='/users/login/')
def index(request):

    following_users = request.user.author.following.all()
    posts = []

    for user in following_users:
        user_posts = user.post.all().order_by('-created_at')
        for post in user_posts:
            posts.append({
            'post': post,
            'is_liked':True,
        })

    
    for post in posts:
        try:
            is_liked = post['post'].likes.get(pk=request.user.author.pk)
        except:
            is_liked = False
        finally :
            post['is_liked'] = is_liked

    print(posts)

    context = {
        'title':'Home page',
        'posts':posts
    }
    return render(request,'web/index.html',context)