from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import PostForm
from .models import Post


@login_required(login_url='/users/login/')
def create_post(request,user_id):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            Post.objects.create(
                image = instance.image,
                description = instance.description,
                location = instance.location,
                author = request.user.author
            )
            return HttpResponseRedirect('/')

    form = PostForm()
    context = {
        'title': 'Create Post',
        'form':form
    }
    return render(request,'posts/create.html',context)


def single_post(request,pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post,
        'title': 'View post',
    }
    return render(request,'posts/view.html',context)