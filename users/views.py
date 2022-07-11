from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required


from .forms import AuthorForm, EditProfileForm, LoginForm, SignupForm
from .models import Author
from main.functions import generate_form_errors


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        author_form = AuthorForm(request.POST, request.FILES)

        if form.is_valid() and author_form.is_valid():
            instance = form.save(commit=False)
            author_instance = author_form.save(commit=False)
            user = User.objects.create_user(
                username=instance.username,
                password=instance.password,
                email=instance.email,
                first_name=instance.first_name,
                last_name=instance.last_name
            )

            author = Author.objects.create(
                name=author_instance.name,
                profession=author_instance.profession,
                image=author_instance.image,
                bio=author_instance.bio,
                user=user
            )
            user_ = authenticate(username=instance.username,
                                 password=instance.password)
            auth_login(request, user_)
            return HttpResponseRedirect(f'/users/{author.id}/')

        else:
            print(author_form)
            message = generate_form_errors(form)
            message += generate_form_errors(author_form)
            print(message)
            form = SignupForm()
            author_form = AuthorForm()
            context = {
                'title': 'Signup page',
                'error': True,
                'form': form,
                'message': message,
                'author_form': author_form
            }
            return render(request, 'users/signup.html', context)

    else:
        form = SignupForm()
        author_form = AuthorForm()
        context = {
            'form': form,
            'author_form': author_form,
            'title': 'Signup page',
        }
        return render(request, 'users/signup.html', context)


def login(request):
    
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            if username and password:
                user = authenticate(username=username, password=password)
                if user is not None:
                    auth_login(request,user)
                else:
                    print("user is none")
                    context = {
                        'title': 'Login page',
                        'error':True,
                        'message': 'Invalid username or password'
                    }
                    return render(request, 'users/login.html', context)

                return HttpResponseRedirect('/')

        context = {
            'title': 'Login page',
        }
        return render(request, 'users/login.html', context)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/users/login')
def profile(request, pk):
    user = Author.objects.get(id=pk)
    posts = user.post.all()
    is_author = False
    if request.user == user.user:
        is_author = True
    context = {
        'title': user.name,
        'user': user,
        'is_author': is_author,
        'posts':posts,
    }
    return render(request, 'users/profile.html', context)


def edit_profile(request, pk):
    if request.method == 'POST':
        instance = get_object_or_404(Author, pk=pk)
        user_instance = get_object_or_404(User, pk=instance.user.id)

        form = AuthorForm(
            request.POST, request.FILES or None, instance=instance)
        author_form = EditProfileForm(
            request.POST or None, instance=user_instance)

        if form.is_valid() and author_form.is_valid():
            form.save()
            author_form.save()
            return HttpResponseRedirect(f'/users/{pk}/')
        else:
            return HttpResponseRedirect(f'/users/{pk}/')

    else:
        author = Author.objects.get(pk=pk)
        author_instance = {
            'name': author.name,
            'profession': author.profession,
            'image': author.image,
            'bio': author.bio,
        }
        user_instance = {
            'first_name': author.user.first_name,
            'last_name': author.user.last_name,
            'email': author.user.email,
            'username': author.user.username,
        }

        form = EditProfileForm(initial=user_instance)
        author_form = AuthorForm(initial=author_instance, instance=author)
        context = {
            'title': 'Edit Profile',
            'form': form,
            'author_form': author_form,
            'author': author
        }
        return render(request, 'users/edit_profile.html', context)


def search(request):
    q = request.GET.get('q')
    try:
        users = User.objects.filter(username__contains=q)
    except:
        users = None
    context = {'users': users}
    return render(request, 'users/search.html',context)