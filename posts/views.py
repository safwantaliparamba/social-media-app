from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import EditPostForm, PostForm
from .models import Post


@login_required(login_url='/users/login/')
def create_post(request, user_id):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            Post.objects.create(
                image=instance.image,
                description=instance.description,
                location=instance.location,
                author=request.user.author
            )
            return HttpResponseRedirect('/')

    form = PostForm()
    context = {
        'title': 'Create Post',
        'form': form
    }
    return render(request, 'posts/create.html', context)


def single_post(request, pk):
    is_author = False
    post = Post.objects.get(pk=pk)
    if request.user.author.pk == post.author.pk:
        is_author = True
    context = {
        'post': post,
        'title': 'View post',
        'is_author': is_author
    }
    return render(request, 'posts/view.html', context)


def edit_post(request, pk):
    if request.method == 'POST':
        instance = get_object_or_404(Post, pk=pk)
        form = EditPostForm(
            request.POST, request.FILES or None, instance=instance)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/posts/{pk}/view')
        else:
            return HttpResponseRedirect(f'/posts/{pk}/view')

    post = Post.objects.get(pk=pk)

    if not post.author.pk == request.user.author.pk:
        return HttpResponseRedirect('/')

    edit_post_initial = {
        'image': post.image,
        'description': post.description,
        'location': post.location
    }

    form = EditPostForm(initial=edit_post_initial)

    context = {
        'pk': pk,
        'form': form
    }
    return render(request, 'posts/edit.html', context)


def delete_post(request,pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return HttpResponseRedirect('/')